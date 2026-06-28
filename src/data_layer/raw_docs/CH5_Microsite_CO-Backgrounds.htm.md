

# Background

The <ch5-background> component is an extension of the standard HTML <background> element. CH5 video uses alpha blending, where portions of the HTML become invisible to allow video playing below the HTML layer to be visible to the user. The <ch5-background> component works with the <ch5-video> component to support background images and colors of the HTML element views in CH5 projects while allowing video to appear when necessary.

For interactive examples using the <ch5-background> component and CSS classes, refer to the [Showcase Application](https://sdkcon78221.crestron.com/downloads/ShowcaseApp/ch5-background/ch5-background-url.html).

## Features

The <ch5-background> attributes provide the following features:

- Sets a background color
- Sets repeat and stretch behavior for background images
- Sets the image background color when an image does not share the aspect ratio of its container
- Sets transition effects and duration between background images
- Sets the refresh rate, URL attribute, and background color attribute via control system state

## Design Considerations

The <ch5-background> component does not perform optimally when used in conjunction with the Angular router component.

It is recommended that the Angular router component should not be used in projects that use the <ch5-background> component with video.