

# Segmented Gauge

The <ch5-segmented-guage> component is used to display feedback from an analog join by scaling the analog value on a touch screen instead of via control system programming.

For interactive examples using the <ch5-segmented-gauge> component and CSS classes, refer to the [Showcase Application](https://sdkcon78221.crestron.com/downloads/ShowcaseApp/ch5-segmented-gauge/ch5-segmented-gauge-gauge-led-style.html).

## Features

The <ch5-segmeneted-gauge> attributes provide the following features:

- Allows a digital join to send a value to the control system. The value goes high when a user presses on the gauge and goes low when the press is released. Repeat digital joins are not supported.
- Allows an analog join to receive feedback from the control system. If no join is selected, the position of the gauge does not change.
- Controls whether or not the gauge is touch settable.
- Sets the number of segments displayed on the gauge (the maximum is 50).
- Set a minimum and maximum analog value to reflect the lowest and highest points of the gauge, respectively.

## Design Considerations

For programmers coming from VT Pro-e® software, the segmented gauge component in CH5 behaves differently than the segmented gauge in VT Pro-e and will require different programming.