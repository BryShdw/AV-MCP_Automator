

# Known Limitations

The following CH5 limitations are known at this time. More information and workarounds (if possible) are provide for each limitation.

## [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Components](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Known-Limitations.htm\#)

Vertically-oriented buttons do not render correctly in the Safari® or FireFox® browsers at this time. This occurs because of an issue caused by webkit implementation and is not something that can be addressed on the CH5 side.

* * *

The <ch5-background> component does not perform optimally when used in conjunction with the Angular router component.

It is recommended that the Angular router component should not be used in projects that use the <ch5-background> component with video.

* * *

There is currently no functionality added to the <ch5-button> component or similar components that provides audible feedback when the button is pressed. This functionality may be added in a future release of Crestron HTML5 User Interface.

* * *

When using the text input control in a CH5 project loaded on a TSW-60 series touch screen, pressing **Enter** will send an event instead of going to the next line. This behavior is expected.

* * *

Snapshot mode with authentication does not work on <ch5-image> because of updated browser security controls. Use <ch5-video> snapshot mode instead if you need to capture images when authentication is required.

* * *

Button colors may extend outside of their defined borders in web browsers when corner border radius is applied. This issue is caused by variations in subpixel rendering, antialiasing, zooming, and border-radius rendering between web browsers. The effectiveness of any masking techniques will also vary depending on the browser, zoom level, and specific CSS properties of the component, and the issue may not be fully resolvable via CSS.

## [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)Reserve Joins](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Known-Limitations.htm\#)

Older TSW-x60 firmware versions did not implement the reserve join names listed below correctly. This issue has been fixed as of firmware version 3.000.0014.

- Csig.Light\_Sensor\_Value\_fb
- Csig.Ip\_Address\_fb
- Csig.MAC\_Address\_fb
- Csig.All\_Control\_Systems\_Online\_fb
- Csig.Control\_Systems\_Offline\_fb
- Csig.DialBuffer\_fb
- Csig.CameraStreamURL\_fb
- Csig.CameraSnapshotURL\_fb
- Csig.ConnectedToServer\_fb
- Csig.Dialing\_fb
- Csig.Busy\_fb
- Csig.CallActive\_fb
- Csig.Ringing\_fb
- Csig.Incoming\_fb
- Csig.Hold\_fb
- Csig.Call\_Terminated\_fb
- Csig.Ringback\_fb
- Csig.Voice\_Recording\_dB\_fb
- Csig.Voice\_Capture\_Result\_fb
- Csig.Voice\_Capture\_in\_Progress\_fb
- Csig.Voice\_Capture\_Recording\_fb
- Csig.Voice\_Capture\_Decoding\_fb
- Csig.Voice\_Capture\_Complete\_fb
- Csig.Voice\_Capture\_Error\_fb
- Csig.Voice\_Recognition\_Service\_Online\_fb
- Csig.In\_Progress\_fb
- Csig.Authentication\_On\_fb
- Csig.Authenticated\_fb
- Csig.Not\_Authenticated\_fb
- Csig.Admin\_fb
- Csig.Not\_Admin\_fb
- Csig.LedAccessoryConnected\_fb
- Csig.Username\_fb
- Csig.User\_Groups\_fb
- Csig.System\_WiFi\_IP\_Address\_fb
- Csig.System\_WiFi\_Signal\_Strength\_fb
- Csig.System\_WiFi\_Link\_Status\_fb

## [![Closed](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Skins/Default/Stylesheets/Images/transparent.gif)HTML5 Web XPanel](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Known-Limitations.htm\#)

Running projects in a web browser opens the ability to reference web API endpoints to gather data. CORS (Cross-origin resource sharing) restrictions in browsers require that the servers that implement the web API endpoints provide specific HTTP headers to inform the browser that the service is designed to be accessed by web pages served up by different web servers.

For more information on CORS, refer to [https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).

* * *

Support for passing credentials to a web API endpoint, including the prevalent use case of security cameras, as https://user:password@host is no longer supported by many browsers, including Chrome since version 59. This affects the ability of the <ch5-image> component to work to gather images with credentials in the browser.

* * *

Chrome and other browsers no longer play video and sounds automatically. This can cause issues if you are using the browser as a virtual panel and want to trigger a sound from the control system without requiring user interaction.

Refer to [https://developers.google.com/web/updates/2017/09/autoplay-policy-changes#mei](https://developers.google.com/web/updates/2017/09/autoplay-policy-changes#mei) for information on Chrome browser policy and possible workarounds.

* * *

As of the initial release of the HTML5 Web XPanel functionality (January 2021), the XiO Cloud® service does not support providing a CH5 archive (.ch5z) file as a web project destined for a control system. This issue will be rectified in a subsequent release of XiO Cloud.

* * *

If the XPanel disconnected from and then reconnected to the control system, the Xpanel may not reflect the analog join value of the control system after reconnecting. This occurs if the analog join value was changed on the control system during the disconnected state.

To rectify this issue, refresh the web browser running the XPanel.