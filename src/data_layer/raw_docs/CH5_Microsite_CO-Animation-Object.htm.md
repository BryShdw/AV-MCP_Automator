

# Animation Object

The <ch5-animation-object> component is a theme-based object that supports variable frame rates and automatic playback at runtime. The <ch5-animation-object> component provides the same functionality as the animation object in Smart Graphics® technology.

For interactive examples using the <ch5-animation-object> component and CSS classes, refer to the [Showcase Application](https://sdkcon78221.crestron.com/downloads/ShowcaseApp/ch5-animation/ch5-animation-start-animating.html).

## Features

The <ch5-animation-object> attributes provide the following features:

- Starts or stops playing the animation object.
- Sets an integer value representing the number of frames played per second (3–100).
- Sets the size of the animation object (small, regular, large, or x-large).
- Determines whether the animation is started or stopped based on feedback from the control system.
- Determines whether a pressable button will be displayed based on feedback from the control system.
- Determines the animation style that will be displayed based on feedback from the control system.

## Design Considerations

When an animation object is positioned above controls such as buttons or toggles, those controls cannot be selected by a user without clicking outside of the area covered by the animation object.