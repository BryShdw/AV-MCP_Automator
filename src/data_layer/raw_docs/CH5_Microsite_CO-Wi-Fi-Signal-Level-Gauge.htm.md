

# Wi‑Fi Signal Level Gauge

The <ch5-wifi-signal-level-gauge> component is used to display feedback from an analog join that indicates the current Wi‑Fi® network signal strength. The <ch5-wifi-signal-level-gauge> component is a feedback-only control where a signal graphic indicates the Wi-Fi signal level strength.

For interactive examples using the <ch5-wifi-signal-level-gauge> component and CSS classes, refer to the [Showcase Application](https://sdkcon78221.crestron.com/downloads/ShowcaseApp/ch5-wifi-signal-level-gauge/ch5-wifi-signal-level-gauge-size.html).

## Features

The <ch5-wifi-signal-level-gauge> attributes provide the following features:

- Assigns a join number to the feedback analog join to receive feedback from the control system.
- Determines the graphical presentation and appearance of the gauge. This style can contain any number of states that each represent a different signal strength level. Gauge styles do not support themes.
- Sets the gauge orientation (up, down, left, or right)
- Set a minimum and maximum analog value to reflect the lowest and highest points of the gauge, respectively. The gauge will show an off state when receiving a value below the minimum and will show the maximum signal strength when receiving a value above the maximum.
- Sets the gauge size (small, regular, large, and x-large).

## Design Considerations

The bars representing the signal strength in the Wi‑Fi signal level gauge will increment or decrement when the signal moves between the three defined percentage groupings (0–33%, 34–66% and 67–100%). For example, the gauge will decrement from 3 to 2 bars when the signal decreases from 67–100% to 34–66%. For programmers coming from VT Pro-e® software, differences may be observed between how values are represented within the VT Pro-e and CH5 Wi‑Fi signal level gauges.