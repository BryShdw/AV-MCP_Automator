

# Breakpoints

**Breakpoints** are created when a Page is designed in one resolution and then the user switches to a second resolution and modifies the Page Design in this second resolution.

The second resolution initially inherits the first resolution’s original design. Modifications made in the second resolution are **not** inherited backward by the first resolution—a Breakpoint is created on the second resolution.

The first (original) resolution maintains its original design.

For example, the first resolution has a Button at position 10,10. The user switches to a second resolution and moves the Button to position 15,15. On the second resolution, the user specifically designated a new Button position, thereby, creating a Breakpoint.

When the user switches back to the first resolution, the same Button is still at position 10,10.

A modification made for a specific resolution will persist for that specific resolution.

Furthermore, the second resolution will continue to inherit modifications from the first resolution until these modifications are changed on the second resolution; thereby, creating additional Breakpoints.

For example, on the first resolution Formatted Text is re-positioned at position 30,30. On the second resolution, the Formatted Text will initially be at position 30,30 because on the second resolution the FormattedText's position has not be modified yet. If on the second resolution, the Formatted Text is moved to position 40,40, then a Breakpoint is established.