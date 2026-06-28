

# Button

The <ch5-button> component is an extension of the standard HTML button element with icons and simple formats.

For interactive examples using the <ch5-button> component and CSS classes, refer to the [Showcase Application](https://sdkcon78221.crestron.com/downloads/ShowcaseApp/ch5-button/ch5-button-types.html).

## Features

The <ch5-button> attributes provide the following features:

- Applies a custom CCS class for runtime.
- Sets the button label value.
- Sets the button icon class, position, and orientation.
- Sets the button shape and size.
- Sets stretch properties of the button relative to its container.
- Sets the button type (default, info, text, danger, warning, success, primary, secondary)
- Sets the state of the component when selected (applies the ch5-button--selected CSS class if true).
- Receives selection and label state from the control system.
- Sends signals to the control system on click or tap events.
- Allows an image to be displayed as the background for a button.

## Design Considerations

Vertically-oriented buttons do not render correctly in the Safari® or FireFox® browsers at this time. This occurs because of an issue caused by webkit implementation and is not something that can be addressed on the CH5 side.

When using **iconUrl** and **backgroundImageUrl** together, ensure their respective image files share the same aspect ratio. If the images have different aspect ratios, then one image may appear to be overlaid on top of the other incorrectly.

Button colors may extend outside of their defined borders in web browsers when corner border radius is applied. This issue is caused by variations in subpixel rendering, antialiasing, zooming, and border-radius rendering between web browsers. The effectiveness of any masking techniques will also vary depending on the browser, zoom level, and specific CSS properties of the component, and the issue may not be fully resolvable via CSS.