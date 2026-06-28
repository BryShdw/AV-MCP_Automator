

# Overlay Panel

The <ch5-overlay-panel> component provides a content container for other components that appear on top of and that overlay the main content container. This component allows other overlay panels to be nested.

For interactive examples using the <ch5-overlay-panel> component and CSS classes, refer to the [Showcase Application](https://sdkcon78221.crestron.com/downloads/ShowcaseApp/ch5-overlay-panel/ch5-overlay-panel-closable.html).

## Features

The <ch5-overlay-panel> attributes provide the following features:

- Allows a panel to be hidden if a touch event occurs outside of it
- Allows a close button to be added to the panel
- Applies a background mask
- Sets stretch properties for the panel in relation to its parent component
- Sets the text overflow behavior
- Positions the component in relation to a window or an element (by ID)
- Applies a custom CSS class to the component
- Positions the panel via received control system state
- Sends signals to the control system after panels are shown or hidden

## Design Considerations

When <ch5-modal-dialog> and <ch5-overlay-panel> components are used in Angular templates, the modal dialog or overlay panel will not appear in the UI when triggered unless the relevant code is added to index.html above <app-root></app-root>.

Refer to the following sample code:

Copy

```
<body>
    <ch5-overlay-panel receiveStateShowPulse="trigger_1" closable>
        <p>Sample text</p>
        <ch5-image id="ex1-img" url="https://yourimagelocation.com/1/">
        </ch5-image>
    </ch5-overlay-panel>
    <ch5-modal-dialog receiveStateShowPulse="trigger_3" closable>
        <p>Sample text</p>
        <ch5-image id="ex1-img" url="https://yourimagelocation.com/2/">
        </ch5-image>
    </ch5-modal dialog>
    <app-root>
        <div id="loader"></div>
    </app-root>
</body>
```