

# WebKit Design Considerations (iOS/Safari/Crestron ONE App)

The WebKit™ HTML rendering engine is used by the iOS® software version of the Crestron ONE app and by the Safari® web browser on iOS or macOS® devices (for HTML5 Web XPanel projects). While WebKit strives to implement the same HTML5 and W3C standards as the Chromium and Mozilla® Gecko rendering engines, there are differences that you should be aware of while creating a cross-platform project.

## Component Rendering

WebKit renders standard components differently than other HTML rendering engines. WebKit produces events from HTML elements in a different order than other rendering engines. Test your projects on the WebKit platform even if it works as expected on Chromium-based platforms (TSW series touch screens and the Chrome® browser).

## Assign Focus to a Text Entry Field

WebKit does not allow JavaScript that is not directly associated with a user interaction in the browser to assign focus to a text entry field, which includes CH5 <ch5-textinput> components. This behavior is by design, as it prevents a web application to display an on-screen keyboard without the user requesting the change.

Refer to [https://stackoverflow.com/questions/32449870/programmatically-focus-on-a-form-in-a-webview-wkwebview/48623286](https://stackoverflow.com/questions/32449870/programmatically-focus-on-a-form-in-a-webview-wkwebview/48623286) for details.

## Vertical <ch5-button> Does Not Get Ellipses Properly

A <ch5-button orientation=”vertical” label=”very long label”> will not properly truncate with an ellipsis \[...\] because of [WebKit issue 116413](https://bugs.webkit.org/show_bug.cgi?id=116413).

## Notches for iPhone® X and Above

With the introduction of the iPhone X, all subsequent iPhone device releases have provided “notches” for speakers and forward-facing cameras to reduce the bezel on the phone. WebKit provies special CSS and meta tags to allow your project to support the notches. Refer to [https://webkit.org/blog/7929/designing-websites-for-iphone-x/](https://webkit.org/blog/7929/designing-websites-for-iphone-x/) for details.