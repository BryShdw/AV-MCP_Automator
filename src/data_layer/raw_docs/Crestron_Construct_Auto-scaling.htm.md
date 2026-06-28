

# Auto-Scaling Support

Starting with version 1.4101 and CH5 version 2.15, Construct projects support runtime auto-scaling. This exciting new feature will scale the user interface based on the resolutions and devices that have been defined in the project. It is always enabled and part of the compiled project.

This feature implements a hybrid approach where the calculated scaling factor is always based on the higher parent resolution that was defined and defined resolutions bypass scaling.

For example:

If the project contains a resolution for a 4K device (2560x1440), TSW-1070 (1280x800), and iPhone 15 Plus Landscape (808x407).

1. When the user interface CSS viewport is 2560x1440, no scaling factor will be applied.

2. When the user interface CSS viewport is less than 2560x1440 (4K) and greater than 1280x800 (TSW-1070) the calculated scaling factor will be based on 2560x1440 (4K) since that is the parent resolution to this CSS viewport.

3. When the user interface CSS viewport is 1280x800 (TSW-1070), no scaling factor will be applied.

4. When the user interface CSS viewport is less than 1280x800 (TSW-1070), the calculated scaling factor will be based on 1280x800 (TSW-1070) since that is the parent resolution to this CSS viewport.


Auto-scaling **only** scales resolutions downward from highest to lowest. Attempting to auto-scale upward, for example from a TSD-1080 to 4K device, creates a disproportional amount of empty blank space. Therefore, as stated, auto-scaling effectively **only** scales resolutions downward.

Auto-scaling can determine when to use a Breakpoint and when to use scaling.

Upgrade older Projects to CH5 version 2.15 to enable auto-scaling.

**Note**: In order to support both landscape and portrait scaling, a landscape and portrait resolution must be defined in the Construct project.