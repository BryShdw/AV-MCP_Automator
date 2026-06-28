

# Reserved Joins

Reserved Joins can be set for input and output joins. Reserved Joins in Construct are not filtered based on the active resolution. The user simply selects the applicable Reserved Joins.

## Setting Reserved Joins

1. To set a Reserved Join for an input or output join, click on the ReservedJoins smart icon **R** (see below).



![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Reserved%20Joins/Reserved%20Join%20Smart%20icon.jpg)

2. Select the applicable Reserved Joins from the active resolution's/touch screen's Reserved Joins scroll box:



![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Reserved%20Joins/Reserved%20Join%20Scroll%20Box.jpg)

![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Reserved%20Joins/Reserved%20Join%20Example.jpg)

In this example, ReservedJoins have been set for Received Digital Feedback - Enable and for Receive Serial Feedback - Indirect Text


1. To clear a Reserved Join, either enter or select a Join Number or select a Contract Join.


## Properties : Interactions - Link Send & Receive

Under Interactions in the Properties Grid, the Button, Slider and Textinput Components have a property called Link Send & Receive set, by default, to True. Link Send & Receive dynamically links specific Receive Feedback and Send Command joins to each other.

When Link Send & Receive is set to True, specific linked Receive Feedback and Send Command joins cannot be set using Reserved Joins. Whereas, unlinked Receive Feedback and Send Command joins can be set using Reserved Joins.

For example, the Button Component links Received Digital Feedback - Selected with Send Digital Command - Press:

![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Reserved%20Joins/Reserved%20Joins%20Linked.jpg)

In this example, Reserved Joins cannot be set for Received Digital Feedback - Selected and Send Digital Command - Press as denoted by the Reserved Joins smart icon being disabled and grayed out.

However, join numbers and Contract Joins can be set. These are set in the linked Send Digital Command - Press join and will be duplicated in the corresponding linked Receive Feedback - Selected join:

![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Reserved%20Joins/Linked%20Joins%20example%20set.jpg)

In this example, the Send Digital Command - Press join was set to the join number **1**. This join number was automatically duplicated in the linked Receive Digital Feedback - Selected join. The same functionality applies to ContractJoins **.**

**Note:**

- The Slider Component links Receive Analog Feedback - Lower Touch fb with Send Analog Command - Lower Touch:



![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Reserved%20Joins/Slider%20Linked%20Joins.jpg)


The Textinput Component links Receive Serial Feedback - Indirect Text with Send Serial Command - Output Text **:**

**![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Reserved%20Joins/Textinput%20Links%20Joins.jpg)**