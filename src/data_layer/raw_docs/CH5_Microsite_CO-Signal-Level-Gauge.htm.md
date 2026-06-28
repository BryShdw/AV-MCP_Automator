

# Signal Level Gauge

The <ch5-signal-level-gauge> component is used to display a signal level using feedback from an analog join that is represented by bars using a predefined scale. The <ch5-signal-level-gauge> component is also used to scale an analog value on a touch screen without requiring any control system programming.

For interactive examples using the <ch5-signal-level-gauge> component and CSS classes, refer to the [Showcase Application](https://sdkcon78221.crestron.com/downloads/ShowcaseApp/ch5-signal-level-gauge/ch5-signal-level-gauge-orientation.html).

## Features

The <ch5-signal-level-gauge> attributes provide the following features:

- Receives feedback from the control system (via analog join) to update the signal level gauge position.
- Also receives feedback from the control system (via digital join) to disable or hide the object if the digital join is returned as false.
- Sets the style (graphical presentation and appearance) of the signal level gauge.
- Sets the orientation of the signal level gauge (horizontal or vertical).
- Determines the lowest and highest possible positions of the signal level gauge.
- Determines the number of bars (up to 15) that will be represented on the signal level gauge.
- Determines the spacing (in pixels) between the bars within the signal level gauge.
- Sets the size of the signal level gauge (small, medium, large, or x-large).

## Design Considerations

The number of bars shown in the signal level gauge must be a multiple of the maximum number of values that will be represented by the gauge. For example, if 12 values will be represented, the number of bars shown could be 2, 3, 4, 6, or 12. For programmers coming from VT Pro-e® software, differences may be observed between how values are represented within the VT Pro-e and CH5 signal level gauges.