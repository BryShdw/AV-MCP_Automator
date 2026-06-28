

# Color Chip

The <ch5-color-chip> component provides additional feedback for an RGB color combination (potentially from <ch5-color-picker>), but can be any source of Red, Green and Blue values. The <ch5-color-chip> component also acts as a simple, flat color image that can be selected by a user and provides a digital join to a control system to indicate it has been selected.

For interactive examples using the <ch5-color-chip> component and CSS classes, refer to the [Showcase Application](https://sdkcon78221.crestron.com/downloads/ShowcaseApp/ch5-color-chip/ch5-color-chip-preview-color.html).

## Features

The <ch5-color-chip> attributes provide the following features:

- Sets the Red, Green, and Blue (RGB) color values (0–256) for the color chip.
- Sets a maximum value to use for changing the current RGB color values for a color chip.
- Sets a color that is used to review the initial (preview) color of the color chip.
- Changes the RGB values based on feedback from the control system.
- Sends feedback to the control system based on digital join or a reserved join (for a corresponding touch screen action)

## Design Considerations

For programmers coming from VT Pro-e® software, expect standard RGB values for each color set through the control system. Differences may be observed between the VT Pro-e and CH5 color chips because VT Pro-e uses a nonstandard RGB representation.