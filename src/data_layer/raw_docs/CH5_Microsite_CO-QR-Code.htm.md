

# QR Code

The <ch5-qrcode> component is a programmable control used to store alphanumeric data in a QR image as implemented by the designer. QR codes can be added to pages or widgets to direct users to specific content or data.

For interactive examples using the <ch5-qrcode> component and CSS classes, refer to the [Showcase Application](https://sdkcon78221.crestron.com/downloads/ShowcaseApp/ch5-qrcode/ch5-qrcode-qrcode.html).

## Features

The <ch5-qrcode> attributes provide the following features:

- Can receive feedback from the control system via a serial join to programmatically change the data stored in the generated QR code image.
- Sets the alphanumeric data that is stored in the generated QR code image.
- Sets the size of the QR code via its width in pixels. The supported range is 160–10000, and the default value is 200. Any entered values that fall outside of this range will default the minimum or maximum supported sizes, respectively.
- Sets the foreground and background colors of the QR code image.

## Design Considerations

The QR code component is not supported on TSW‑x60 series touch screens.

* * *

The following table shows the maximum number of storable characters for each supported encoding mode.

| Encoding Mode | Maximum Characters |
| --- | --- |
| Numeric | 3057 |
| Alphanumeric | 1852 |
| Byte | 1273 |
| Kanji | 784 |

NOTE: The supported maximum characters may vary if using mixed modes.