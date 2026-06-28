

# Subpage Reference List

The <ch5-subpage-reference-list> component contains a collection of widgets that can be used within a CH5 project.

For interactive examples using the <ch5-subpage-reference-list> component and CSS classes, refer to the [Showcase Application](https://sdkcon78221.crestron.com/downloads/ShowcaseApp/ch5-subpage-reference-list/ch5-subpage-reference-list-center-items.html).

## Features

The <ch5-subpage-reference-list> attributes provide the following features:

- Sets the orientation of the subpage reference list (the scroll and pan direction for adjacent objects).
- Allows the list to be set as endless (the last and first item of the list will scroll next to one another). This is available only for single row and column lists.
- Allows objects to be centered in the list.
- Allows the list to show more than one object within each list item (for horizontal and vertical orientations).
- Increments the digital, analog, and serial joins for each subpage reference in the list. The join values are different from the CH5 offset.
- Allows enable and visibility joins to be to be used on each list item. When the list item join is driven high, the list item will be disabled or hidden, respectively.
- Specifies a number of subpage references to be used within the list. A maximum of 600 objects is currently enforced at runtime.
- Scrolls the page to the position of the subpage reference list.
- Allows the subpage reference list to be stretched to meet the size of its container.
- Allows background styles and color, scroll bar positions, margins, and height/width to be set for list items.

## Design Considerations

- All lists (buttons, subpage reference lists, tab buttons, and so forth) are not recommended as controls for subpage reference lists.
- The following VT Pro-e software attributes are not supported by the CH5 subpage reference list. Refer to the following workarounds.
  - **clickHoldTime**: The click and hold attribute will not be supported by CH5 control in the widget.
  - **useSetNumberOfItems**: The **receiveStateNumberOfItems** attribute will determine if the control system overwrites the number of list items.
  - **showBackground**: CSS classes will be used instead to display a chosen background color.
- When using this component with the Contract Editor, a list size of 1 will not work within CH5. A list size of 2 or more must be specified.
- When using a horizontal subpage reference list, it is not recommended to use an internal control with a horizontal slider (such as a segmented gauge). The top‑level slider (list) will take precedence over the internal control in this scenario.
- It is possible to add a list control within a subpage reference list. However, performance issues may arise when cascading a list within a list. If using nested lists, designers should take performance best practices into account as described in [Crestron Template Project Performance Optimization](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/Performance-Optimization.htm) and test the project thoroughly for performance.