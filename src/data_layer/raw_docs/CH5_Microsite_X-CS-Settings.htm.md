

# Control System Configuration

Use the following console commands to configure the control system for an HTML5 Web XPanel project deployment.

NOTE: Ensure that the control system is running the minimum required firmware version or higher as described in [Dependencies](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Platforms/X-Dependencies.htm).

## securewebport

HTML5 XPanel requires the use of the HTTPS protocol on the control system. The service port for the HTTPS protocol can be changed from the web standard (443) to another port number using the securewebport command.

**Syntax:** securewebport \[portnumber\]

- portnumber \- Sets the desired port number (in decimal notation)
- No parameter - Displays the current value

You must append the port to the URL to reference the project on the control system if the port was changed from the default. For example, if the port was changed to 8443, the following example URL would change from "https://W.X.Y.Z/shell-template/index.html" to "https://W.X.Y.Z:8443/shell‑template/index.html".

## securewebsocketport

HTML5 Web XPanel is hosted in a web browser and, as a result, cannot communicate to the control system via TLS sockets like touch screens. A service port is made available on the control system to support secure WebSocket communications that are supported in browsers and by the CH5 WebXPanel library. The securewebsocketport console command can change the default port number.

**Syntax:** securewebsocketport \[portnumber\]

- portnumber \- Sets the desired port number (in decimal notation)
- No parameter - Displays the current value

You will need to change the WebXPanel library configuration if you change the WebSocket port from the default value. For more information, refer to [Add or Remove HTML5 Web XPanel Support](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Template-Project/Tasks/Add-Remove-XPanel.htm) and [Add XPanel to Custom (Non‑Template) Project](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Platforms/X-Custom.htm).

## Authentication Commands

Crestron has set high security standards for using the HTML5 Web XPanel feature on a control system.

The control system must require authentication to access resources and must enable secure, encrypted communications. The three commands to control these settings are ssl, authentication, and optionally userpageauth.

NOTE: The syntax for each command is provided at the end of this section.

For 4‑Series control systems and 3‑Series control systems that have been recently purchased or restored to factory defaults, the ssl and authentication commands will be properly configured to use the HTML5 Web XPanel feature. For older 3‑Series control systems, these settings may need to be updated.

NOTE: Issue the ver -v command to view information about your control system. If the FORCED\_AUTH\_MODE setting is false, then you will need to update the SSL and authentication settings for the control system.

For systems that have FORCED\_AUTH\_MODE set to true, the userpageauth command regulates whether web page resources require credentials to be accessed.

- For 3-Series control systems that have the setting available because FORCED\_AUTH\_MODE is true, userpageauth must be set to on.
- For 4-Series control systems, it is recommended to set userpageauth to on to improve the experience for the end user. The user will be prompted for credentials as they load the project initially instead of when the project’s WebXPanel library tries to access the control system via the WebSocket.

The following table summarizes the different authentication permutations.

| Control System Type | Forced Auth Mode Setting | SSL Setting | Authentication Setting | User Page Auth Setting |
| --- | --- | --- | --- | --- |
| 3‑Series | false | Must be set to self or CA | Must be set to on | N/A |
| 3‑Series | true | Always self or CA | Always on | Must be set to on. |
| 4‑Series | Always true | Always self or CA | Always on | Recommended set to on. |

### ssl

**Syntax:** ssl \[OFF\|SELF\|CA\] {TLS1.2ONLY}

- OFF \- Turns SSL off for the control system
- SELF \- Sets SSL to use self-signed certificates
- CA \- Sets SSL to use CA (Certificate Authorities) issued certificates

  - -P \- Used to supply a password for opening the private key file when SSL is set to CA

- TLS1.2ONLY \- Sets TLS 1.2 support exclusively for client and server connections
- No parameter - Displays the current value

### authentication

**Syntax:** authentication \[ON\|OFF\]

- ON \- Turns authentication on for the control system
- OFF \- Turns authentication off for the control system
- No parameter - Displays the current value

### userpageauth

**Syntax:** userpageauth \[ON\|OFF\]

- ON \- Turns user page authentication on for the control system
- OFF \- Turns user page authentication off for the control system
- No parameter - Displays the current value

## webinit

When a control system is received from the factory or restored to factory defaults, entering the control system host name or IP address into a web browser with an "https://" prefix will redirect you to the "/setup" endpoint to allow for device configuration.

If the **Web Pages and Mobility Projects** function in Crestron Toolbox™ software is used at least once to deploy an HTML5 Web XPanel project, the default endpoint will change to the last deployed HTML5 Web XPanel project each time a project is deployed.

However, if the ch5-cli deploy utility is always used to deploy the project, the default will not change from the "/setup" endpoint. To set the last deployed project to become the default without using the **Web Pages and Mobility Projects** function, use the webinit console command. This command must only be sent to the control system once to take effect.

## webserver allowsharedsession

4-Series control systems use session management and session cookies that are sent via a web browser to keep track of a given user's login status. If you host an HTML5 Web XPanel project on an independent web server instead of the one provided by the control system, or if you are using web development tools to host a web server on your workstation during project development, the web browser cannot access the 4 Series control system CIP protocol by default.

For maximum security, the session cookies provided by a 4-Series control system are accessible only by web pages served up by the control system web server and are not accessible by web pages served up by independent web servers. The control system, however, provides controls to turn on a shared session with an independent web server to bypass this restriction.

Therefore, if you plan to deploy your HTML5 Web XPanel project on an independent web server, or if you plan to develop your project using a web server hosted on your workstation, you must manually turn on a shared session by issuing the webserver allowsharedsession on command.

Issue webserver allowsharedsession without a parameter to view the current value for this setting.