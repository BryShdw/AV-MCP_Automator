

# Custom Resolutions

supports user-based custom portrait and landscape resolutions. These Custom Resolutions can be added to new and existing UI and Zoom Projects and are tied to the respective Project type.

The user can add and delete Custom Resolutions. These Custom Resolutions are stored in the user's local Crestron Construct application. They are displayed in the Edit Device Resolutions window and are available for all Project use.

If a Project that includes a Custom Resolution(s) is added to a Solution, then that Custom Resolution will be added to the local Crestron Construct application, if the resolution is currently not there.

## Add a Custom Resolution to a Project

1. Open the Project and the applicable Project Page.

2. From the Menu bar, select Edit > Resolution Settings (Alt+Ctrl+S):



![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Custom%20Resolutions/V2/Edit%20Resolutions.jpg)

Or from the Project's right-click menu, select Resolution Settings:



![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Custom%20Resolutions/V2/Resolution%20Settings.jpg)

3. At the bottom of Edit Device Resolutions window, under Add Custom Resolution, type an unique Custom Resolution name in the Name text field:



![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Custom%20Resolutions/V2/Add%20Custom%20Resolution%20-%20no%20x60.jpg)

**Note:** the Custom Resolution name must not start with TSW, TST or DGE, these are reserved for Crestron devices. Furthermore, the Custom Resolution name, as stated, must be unique and cannot be identical to an existing Resolution name:



![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Custom%20Resolutions/V2/Resolution%20unique%20name.jpg)

4. In the Width (px) and Height (px) text fields, type the applicable width and height in pixels or use the corresponding spin up or spin down arrows:



![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Custom%20Resolutions/V2/Add%20Custom%20Resolution%20Detail.jpg)

**Best Practice:** The difference between Widths and Heights of Custom Resolutions should be greater than plus or minus 1 pixel in Crestron Construct.

For example, if one Custom Resolution is 1200x800 and a second Custom Resolution's Width and Height are 1201x800 or 1200x801, then the second Custom Resolution should not be added.

Similarly, if one Custom Resolution is 1200x800 and a second Custom Resolution's Width and Height are 1199x800 or 1200x799, then this second Custom Resolution should not be added.



The Width (px) value is compared against the Height (px) value to determine if the Custom Resolution is landscape or portrait; the corresponding orientation will appear in the Device Resolutions list box.

5. Click the ADD button when done:



![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Custom%20Resolutions/Add%20Button.jpg)

The Custom Resolution will be displayed in the Device Resolutions list box:



![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Custom%20Resolutions/V2/Resolution%20Listed.jpg)

In the Device Resolution list box, Landscape resolutions are sorted by Width; Portrait resolutions are sorted by Height, as shown above.






1. Click the upper-right **X** button in the Edit Device Resolutions window to close the window:



      ![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Custom%20Resolutions/V2/Close%20Window.jpg)


The Custom Resolution will also be listed in the workspace's smart-icon Resolution drop-down:

![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Custom%20Resolutions/V2/Resolution%20Drop%20down.jpg)

In the drop-down, Resolutions that have identical widths and heights are listed next to each other and are separated by a comma:

![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Custom%20Resolutions/V2/idenitcal%20size.jpg)

6. Float the mouse pointer over any Resolution in the drop-down to see its respective Width and Height in parenthesis:



![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Custom%20Resolutions/V2/Float%20Mouse.jpg)


## Adding Projects with Custom Resolutions

When a Project with a Custom Resolution is added to a Solution, the Project's Custom Resolution is added to the local Crestron Construct application--if the Custom Resolution is not already present.

If the Custom Resolution is present, the existing Custom Resolution is left intact. The new Custom Resolution is renamed via auto-incrementation:

![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Custom%20Resolutions/Duplicate%20Custom%20Resolution.jpg)

In the above example, the Project being added has a duplicate Custom Resolution named TS-1080; the local Crestron Construct application already has an identically named Custom Resolution.

Therefore, the added Project's Custom Resolution was renamed to TS-1080-1 via auto-incrementation.

## Deleting Custom Resolutions

A Custom Resolution cannot be deleted if it is used in any Project in an open Solution.

01. In the open Solution's Projects, remove the Custom Resolution from each Project's Resolution Settings.

02. Select each Project Page that uses the Custom Resolution.

03. From the Project's right-click menu select Resolution Settings:



    ![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Custom%20Resolutions/V2/Resolution%20Settings.jpg)

04. In the Edit Device Resolutions window, deselect the Custom Resolution:



    ![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Custom%20Resolutions/V2/Delete%20-Deselect.jpg)

05. Read the Warning - Change is permanent dialog box. As stated deselecting the referenced Custom Resolution will "remove all customizations made for this resolution across all pages and widgets, and may not be undone." Therefore, proceed with due caution.

06. Press the OK button to proceed.

07. Press the garbage pail smart-icon to the far right of the applicable Custom Resolution to delete it:



    ![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Custom%20Resolutions/V2/Delete%20-%20Custom%20Resolution.jpg)

08. Again read the Warning - Change is permanent dialog box--and proceed with due caution.

09. Press the OK button to proceed.

10. Click the upper-right X button in the Edit Device Resolutions window to close the window.