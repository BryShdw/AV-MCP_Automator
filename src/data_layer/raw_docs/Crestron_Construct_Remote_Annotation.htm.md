

# Remote Annotation - DGE -100 & DGE-1000

Remote Annotation allows multiple users to write on a single, shared whiteboard screen -or- draw over a single, shared video image. The input on one touch panel combines itself with the output of another panel.

Remote annotation signals are broadcast messages from one Crestron graphics engine to another(s). These messages are transmitted to devices that are defined in the IP Table entries of the remote annotator as PEER connections.

A Remote Annotation Solution can be further extended.  A maximum of 16 devices can be connected together.  In addition,  two video streams can be simultaneously viewed on screen.

**Note**: The DGE-100 supports both video and whiteboard; the DGE-1000 supports only video.

## Steps

1. Create a Remote Annotation System in SIMPL Windows based on either a DGE-100 or DGE-1000.

2. In SIMPL, add the Remote Annotation Reserved Joins Device Extender to the System:



![](https://help.crestron.com/construct/Content/Resources/Images/Remote%20Annotation/Remote%20Annotation%20Windows.jpg)



In Construct, the Remote Annotation Project's Components will be individually linked to the applicable Reserved Joins in the SIMPL System via the Graphic User Interface Extender that is generated when the Project is compiled.

3. In Construct, create the applicable Project Page(s) and populate the Project Page with the Components that will be linked to the corresponding Reserved Joins in the SIMPL System. Components will include the Video Component and Buttons that are linked to the individual, corresponding Reserved Joins.



For example, a Button labeled Enable would be added and linked to the Annotation Enable Reserved Join:



![](https://help.crestron.com/construct/Content/Resources/Images/Remote%20Annotation/Construct%20Annotation%20Project.jpg)

The above UI is a turnkey UI featuring Buttons that link to all the critical SIMPL-based Reserved Joins.


1. In the Properties Grid under Interactions, set the Link Send & Receive property to False:



![](https://help.crestron.com/construct/Content/Resources/Images/Remote%20Annotation/Link%20Send%20&%20Receive.jpg)


1. Assign the Reserved Joins to the Components:



![](https://help.crestron.com/construct/Content/Resources/Images/Remote%20Annotation/Reserved%20Joins.jpg)