

# CH5 Versions & Managing CH5 Versions

## CH5 Versions

At Solution and Project creation, the applicable CH5 Version can be selected from the CH5 Version drop-down:

![](https://help.crestron.com/construct/Content/Resources/Images/CH5%20Version/V2/CH5%20Versioning%20Drop-down.jpg)

The drop-down lists the installed CH5 Versions.

### Upgrading The Project CH5 Version

An existing Project can be upgraded to a newer, backward compatible CH5 Version.

1. Click on the Project's right-click menu and select Project Properties:



![](https://help.crestron.com/construct/Content/Resources/Images/CH5%20Version/V2/Project%20Properties.jpg)

2. In the Project Properties Window, select the applicable version from the CH5 Version drop-down:



![](https://help.crestron.com/construct/Content/Resources/Images/CH5%20Version/V2/Project%20Properties%20Window.jpg)

3. Click the Save Changes button.


**Warning:** Projects cannot be downgraded. Any attempt to downgrade a Project will fail and a notification will be displayed:

![](https://help.crestron.com/construct/Content/Resources/Images/CH5%20Version/Warning.jpg)

### Cutting and Pasting CH5 Components Between Projects

In order to cut and paste CH5 Components between Projects, the source Project and the target Project must both have the same CH5 version. Otherwise, the cut and paste will fail and a notification will be displayed:

![](https://help.crestron.com/construct/Content/Resources/Images/CH5%20Version/V2/Cut%20and%20paste%20error.jpg)

Prior to the cut and paste, verify that the two Projects have the identical CH5 Version.

From each Project's respective right-click menu, select Project Properties. The Project's CH5 Version will be displayed in the Project Properties CH5 Version drop-down:

![](https://help.crestron.com/construct/Content/Resources/Images/CH5%20Version/V2/Cut%20and%20paste%20version%20confirm.jpg)

The current CH5 Version is displayed by default. In the drop-down list, the current version is highlighted in gray.

## Manage CH5 Versions

The CH5 Version Manager can be accessed during Solution creation or from the Menu bar.

1. During Solution creation, use the CH5 Version drop-down and select Manage CH5 Versions:



![](https://help.crestron.com/construct/Content/Resources/Images/CH5%20Version/V2/Manage%20CH5%20Versions.jpg)

2. From the Menu bar, select Tools > Options > User Interface Plugin> Ch5 Version Manager:



![](https://help.crestron.com/construct/Content/Resources/Images/CH5%20Version/V2/From%20Menu%20bar.jpg)

3. Click Ch5 Version Manager to display the Installed Versions pane:



![](https://help.crestron.com/construct/Content/Resources/Images/CH5%20Version/V2/Options%20Installed%20Versions.jpg)

A check mark denotes the Installed CH5 Versions. The Installed Versions pane lists the both the installed and available CH5 Versions, their Release Date(s) and their Release Notes.

4. Click the Document smart icon to display the CH5 Version's Release Notes:



![](https://help.crestron.com/construct/Content/Resources/Images/CH5%20Version/V2/Release%20Notes.jpg)

![](https://help.crestron.com/construct/Content/Resources/Images/CH5%20Version/V2/Release%20Notes%20Notes.jpg)

5. Select the check box to install the applicable CH5 Version and click the Save button:



![](https://help.crestron.com/construct/Content/Resources/Images/CH5%20Version/V2/Install%20CH5%20Version.jpg)



A notation is displayed after the installation is complete:



![](https://help.crestron.com/construct/Content/Resources/Images/CH5%20Version/V2/Version%20installed%20successfully.jpg)

6. Similarly, deselect the check box to **un** install the applicable CH5 Version and click the Save button:



![](https://help.crestron.com/construct/Content/Resources/Images/CH5%20Version/V2/Uninstall%20Version.jpg)



![](https://help.crestron.com/construct/Content/Resources/Images/CH5%20Version/V2/Version%20Uninstalled.jpg)


### Install & Uninstall Notes

   - A disabled CH5 Version—as indicated by being grayed out or faded—indicates that the corresponding CH5 Version is incompatible with the currently installed Crestron Construct version.
     - Check that CH5 Version's Release Notes and verify the minimum required Crestron Construct version for that CH5 Version's installation:



       ![](https://help.crestron.com/construct/Content/Resources/Images/CH5%20Version/Minimum%20Version.jpg)

     - Install the required Crestron Construct version as needed.
   - If an installed CH5 Version is selected for uninstallation—but it is disabled—then this indicates that an open Project is currently using the corresponding CH5 Version.

     - Close the open Project first and then proceed with the CH5 Version uninstall.