

# CH5 Image Credential Migration

The CH5 component library has traditionally supported displaying credential-protected images and video streams (such as security camera snapshots) using custom Crestron URL schemes (for example, "ch5-img-auths://") that were embedded directly into the auth section of the URL.

**Example:** ch5-img-auth://test:Crestron1!@<server-url>.com/test/teaser1.jpg

However, recent Android SDK releases introduced a security change that blocks image URLs that use custom or nonstandard schemes originating from the CH5 app content. Therefore, the previous URL schemes no longer render on Android devices, including the Crestron ONE™ app for Android OS and TSW series touch screens. Additionally, embedding credentials in the URL auth section (for example, "http://user:pass@host/image.jpg") is also blocked by Android WebView regardless of the scheme used.

The following sections detail the changes made to CH5 image credentials to support Android OS platforms.

## URL Format Changes

The internal URL construction logic of the <ch5-image> and <ch5-video> components was updated in CrComLib as of CH5 version 2.17.3. When an affected component has user and password attributes set, CrComLib now constructs the URL using standard HTTP/HTTPS schemes with credentials passed as query parameters rather than using the custom Crestron scheme.

- **Old URL Format**: ch5-img-auth://test:Crestron1!@<server-url>/test/teaser1.jpg

- **New URL Format**: http://<server-url>/test/teaser1.jpg?cres\_username=test&cres\_password=Crestron1!


The key differences between the old and new URL formats are as follows:

- A standard "http://" or "https://" scheme is used instead of "ch5-img-auth://" or "ch5-img-auths://".

- Credentials are passed as URL query parameters (cres\_username and cres\_password) instead of being embedded in the auth section of the URL.

- The new URL must be properly URL-encoded.


NOTE: Using credentials in the URL argument is not secure. Crestron recommends using this method only if the network is secure and isolated and if the connection between the user interface and control system is secure (over CIPS/HTTPS). For more information about security best practices for a 4-Series control system, refer to the [4-Series Control System Security Reference Guide](https://www.crestron.com/getmedia/092281be-65d9-40e8-983b-926a174c007a/mg_sr_4-series-control-systems "https://www.crestron.com/getmedia/092281be-65d9-40e8-983b-926a174c007a/mg_sr_4-series-control-systems").

## Migration Instructions

The recommended approach for displayed credential-protected images and video streams is to either use the user and password attributes on the <ch5-image> and <ch5-video> components, or by adding the cres\_username and cres\_password query strings to the URL. CrComLib handles the URL construction internally.

NOTE: Either attributes or query strings can be used to encode image credentials, but do not use both methods at once.

Refer to the following examples for HTTP and HTTPS sources:

Copy

```
<!-- Example using attributes -->
<ch5-image
    url="http://<server-url>/test/teaser1.jpg"
    user="test"
    password="Crestron1!">
</ch5-image>

<!-- Example using query string -->
<ch5-image
    url="http://<server-url>/test/teaser1.jpg?cres_username=test&cres_password=Crestron1!">
</ch5-image>
```

NOTE: The user and password attributes are only supported by Crestron devices. The device firmware is responsible for handling the authentication.

When the image URL is provided dynamically from a control system via signal joins, use the receivestateurl attribute along with the user and password attributes:

Copy

```
<!-- URL received from control system signal, credentials as attributes -->
<ch5-image
    receivestateurl="1"
    user="test"
    password="Crestron1!">
</ch5-image>
```