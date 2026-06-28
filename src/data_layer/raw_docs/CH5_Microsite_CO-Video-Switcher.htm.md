

# Video Switcher

The <ch5-video-switcher> component combines a scrolling list with drag-and-drop functionality that is geared toward controlling video sources in a switcher matrix. Assigning a contract join enables full control over the number of screens and source assignments, and feedback is provided to the control system when a source changes on the touch screen.

For interactive examples using the <ch5-video-switcher> component and CSS classes, refer to the [Showcase Application](https://sdkcon78221.crestron.com/downloads/ShowcaseApp/ch5-video-switcher/ch5-video-switcher-display-screen-label.html).

## Features

The <ch5-video-switcher> attributes provide the following features:

- Sends signals to the control system when an icon is dropped or changed in the virtual switcher matrix.
- Receives feedback from the control system regarding the selected source.
- Sets the position of the drag-and-drop list in relation to the area where the virtual switcher matrix is rendered.
- Sets whether the icons in the drag-and-drop list will be endless (first item follows last and last item precedes first for infinite swiping) or finite (first and last items are absolute ends of list).
- Sets the number of rows or columns for the drag-and-drop list.
- Sets whether a scroll bar will be visible for the drag-and-drop list.
- Determines the number of sources that are displayed in the drag-and-drop list.
- Configures the styled graphics and font style that determine the look and feel of the source icon images and text labels.
- Sets the number of columns for the virtual switcher matrix.
- Enables or disables the display of labels on the screen.
- Sets the aspect ratio of the virtual switcher matrix.
- Sets the maximum number of screens that can be controlled.

## Design Considerations

When dragging and dropping a video source into the virtual switcher matrix, the video source selection list may be scrolled during the drag operation. This is expected behavior.