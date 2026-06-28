

# D-Pad

The <ch5-dpad> component consists of top, bottom, left, right, and center buttons arranged in a grid. The D-Pad has a default theme associated with it. The center button can contain custom text, and each button can send signals on click or touch events.

For interactive examples using the <ch5-dpad> component and CSS classes, refer to the [Showcase Application](https://sdkcon78221.crestron.com/downloads/ShowcaseApp/ch5-dpad/ch5-dpad-types.html).

## Features

The <ch5-dpad> attributes provide the following features:

- Applies button, label, receiveStateEnable, and receiveStateShow values to the D-Pad based on a defined contract.
- Sets the D-Pad button type (default, info, text, danger, warning, success, primary, secondary).
- Sets the overall D-Pad shape to a plus or circle.
- Allows individual D-Pad buttons to be hidden.
- Sets stretch properties of the button relative to its container.
- Determines whether the values received from the contract enable the D-Pad and its buttons.
- Determines whether the values received from the contract will show or hide the D-Pad.
- Determines whether the contract will provide a custom class or style for the D-Pad.
- Sends signals to the control system on click or tap events.