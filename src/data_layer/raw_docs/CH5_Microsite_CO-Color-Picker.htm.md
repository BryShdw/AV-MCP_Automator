

# Color Picker (Beta)

The <ch5-color-picker> component is a widget that allows users to view and select full 24-bit range of colors similar to the controls provided in image editing software.

For interactive examples using the <ch5-color-picker> component and CSS classes, refer to the [Showcase Application](https://sdkcon78221.crestron.com/downloads/ShowcaseApp/ch5-color-picker/ch5-color-picker-max-value.html). This component is currently in beta.

## Features

The <ch5-color-picker> attributes provide the following features:

- Sets the Red, Green, and Blue (RGB) color values (0–256) for the color picker.
- Sets a maximum value to use for changing the current RGB color values for a color picker.
- Sends changed RGB values to the control system.

## Design Considerations

Upon program restart, if the default control system color is set to black (RGB values 0.0.0), the pointer may not always reset to the bottom left corner of the color picker if black was the last color chosen using the luminance slider.