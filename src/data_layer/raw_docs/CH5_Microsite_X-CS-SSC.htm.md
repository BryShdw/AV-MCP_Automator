

# Control Systems and Self-Signed Certificates

When testing HTML5 Web XPanel projects served from Crestron® control systems (including VC-4) that use self-signed certificates, not all browsers will allow the secure WebSocket connection. Both the Safari® and Firefox® browsers require the secure WebSocket certificate be accepted manually.

To accept the certificate manually, navigate to the following URL in the browser: "https://<ip‑address>:49200", where "<ip-address>" is the IP address of the control system. Once the WebSocket certificate has been accepted, the HTML5 Web XPanel project will communicate with the control system as expected.