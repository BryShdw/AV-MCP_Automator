

# Slider

The <ch5-slider> component allows a user to provide input by dragging a handle on a slider. One or two numeric values can be visualized with this component. If two values are used, two handles are provided.

For interactive examples using the <ch5-slider> component and CSS classes, refer to the [Showcase Application](https://sdkcon78221.crestron.com/downloads/ShowcaseApp/ch5-slider/handle-shape.html).

## Features

The <ch5-slider> attributes provide the following features:

- Sets the shape and size of the handle(s)
- Sets a range of values for the slider
- Sets the initial value(s) for the slider
- Sets minimum and maximum values for the slider
- Sets the size and orientation of the slider
- Sets the interval between selectable slider values
- Sets stretch properties for the slider
- Sets the behavior for ticks on the slider (can be nonlinear or logarithmic)
- Allows a tooltip to be displayed when using the slider
- Sets a sync timeout between the user releasing the toggle handle and the time the toggle will check if the value is equal with the value from the signal
- Allows a handle to jump to a location on the slider when that location is tapped
- Changes the value(s) on the slider when state is received from the control system
- Sends signals to the control system on slider change
- Provides advanced slider functionality, including the ability to send signals to the control system from the upper or lower parts of the slider, a child on/off button that can be shown with or without the slider, and a customizable slider label area
- Allows padding to be set on the slider for easier control when the handle or gauge is small