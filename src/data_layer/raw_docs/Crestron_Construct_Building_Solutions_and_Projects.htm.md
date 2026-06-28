

# Building Solutions & Projects

## Solution

A Solution is a collection of one or more UI projects. For example, a HomeSolution might include separate UI projects for the touch screens or devices used to control the devices in each room or living space.

Every Solution has at least one Project. Building a Solution builds all its Projects **.**

![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Solutions%20and%20Projects.jpg)

In this example, when the Home Solution is built each of its individual Projects will be built.

## Project

A **Project** is a single UI design for a touch screen or device.

![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Building%20Solutions/Project%20Active.jpg)

To give a Project the active focus, select one of its Pages.

In this example, the Home Solution's Game Room Project currently has the active focus on the workspace because its ConsolesPage is selected. Therefore, when BuildCurrentProject is selected from the Build menu only the Game Room Project will be built.

## Build the Solution

1. From the menu bar, click on Build > Build the Solution (F12)-or- click the Build smart icon from the UI Editor Toolbar to build the current Solution:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Build%20the%20Solution.jpg)

![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Build%20Smart%20Icon.jpg)

2. The Build Output window is launched and displays the Build status:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Build%20Output.jpg)


1. In the Build Output window, click the Errors tab to review any Errors, Warnings or Messages, if applicable:



      ![](https://help.crestron.com/construct/Content/Resources/Images/Errors%20tab_v2.jpg)


1. Double click on Errors, Warnings or Messages to display the corresponding information:



      ![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Build%20Messages.jpg)

      In this example, the Messages are displayed.



      **Out-of-Bounds Warnings**



      If any Components fall out of bounds of the Project Page for a specific resolution, these Components will be noted on the Warnings tab:



      ![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Warnings.jpg)

      In this example the Warnings tab notes that on the Project Page - Menu, the custom Environment Widget Component falls out of bounds of the Project Page.

       Similarly on the Project Page - Main Menu, the Button\_2 Component falls out of bounds of the Project Page

      This can be seen and subsequently corrected on the Project Pages themselves by repositioning the Components within the Project Page bounds:



      ![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Out%20of%20Bounds%20Example%20&%20Fix%201.jpg)

      In this example, the custom Environment Widget Component has been repositioned back within the Project Page bounds.



      ![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Out%20of%20Bounds%20Example%20&%20Fix%202.jpg)

      And in this example, the Button\_2 Component has been repositioned back within the Project Page bounds.


3. Click the Output tab to return to the default Build Output window view.

4. In the Build Output window, take note of each Project's output file location:



![](https://help.crestron.com/construct/Content/Resources/Images/Build%20Output%20window%20file%20location_v4.jpg)

5. Click the X in the Build Output's window's upper right-hand corner to close the Build Output window:



![](https://help.crestron.com/construct/Content/Resources/Images/X%20to%20close.jpg)

6. If any Errors are encountered during the Build, close the Build Output window--and select Clean the Solution and then select Rebuild the Solution.

7. From the Build drop-down menu, select Clean the Solution:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Clean%20the%20Solution.jpg)

Cleaning the Solution, removes the ch5z file(s) and all Project working files.

8. After the Solution is cleaned, from the Build drop-down menu, select Rebuild the Solution (Shift+F12):



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Rebuild%20the%20Solution.jpg)


## Build the Project

1. From the menu bar, click on Build > Build Current Project (Ctrl+B) to build the CurrentProject:



![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Building%20Solutions/Build%20Current%20Project.jpg)

TheCurrentProject must have one of its Project Pages selected to designate that Project as the Current Project:



![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Building%20Solutions/Project%20Active.jpg)

In this example, Game Room is the Current Project because one of its Pages is selected--the Consoles Page.


1. The Build Output window is launched and displays the Build status:





![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Building%20Solutions/Build%20Single%20Project.jpg)



Upon Build completion, take note of the Project outputfile location:



![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Building%20Solutions/Single%20Project%20output%20location.jpg)

2. Click the **X** in the Build Output's window's upper right-hand corner to close the BuildOutput window:



![](https://help.crestron.com/construct/Content/Resources/Images/X%20to%20close.jpg)

3. If any Errors are encountered during the Build, close the BuildOutput window--and select Clean CurrentProject and then select Rebuild the current project.

4. From the Build drop-down menu, select CleanCurrentProject: **![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Building%20Solutions/Clean%20Current%20Project.jpg)**

5. After the Project is cleaned, from the Build drop-down menu, select Rebuild the current project (Alt+F12):



![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Building%20Solutions/Rebuild%20the%20current%20project.jpg)


## Sending the Solution's Projects

1. Launch Crestron Toolbox.

2. From the menu bar, select Tools > EasyConfig **-** or-on the menu bar click on the EasyConfig smart icon:



![](https://help.crestron.com/construct/Content/Resources/Images/EasyConfig%20Tool.jpg)

![](https://help.crestron.com/construct/Content/Resources/Images/EasyConfig%20Icon.jpg)

3. Click on the Pencil smart icon in the EasyConfig window's lower left-hand corner:



![](https://help.crestron.com/construct/Content/Resources/Images/Pencil%20icon.jpg)

4. In the EditAddress window. enter the target device's Address (IP address), Username and Password and then click the OK button:





![](https://help.crestron.com/construct/Content/Resources/Images/Edit%20Address.jpg)

5. In the populated EasyConfig window, click on the DisplayProject button:



![](https://help.crestron.com/construct/Content/Resources/Images/Display%20Project_v2.jpg)

6. In the Open window, select CH5 Projects (\*.ch5z) from the project type drop-down and navigate to the applicable Project in the Solution:



![](https://help.crestron.com/construct/Content/Resources/Images/Open%20Solution%20Toolbox.jpg)

7. In the Project window, click the Send button:



![](https://help.crestron.com/construct/Content/Resources/Images/Project%20Send.jpg)

**Note:**



A touch screen can run only one Project. In a multi-projectSolution **,** each Project must be sent to a separate touch screen or device to run that specific Project.



    For example, the LivingRoomProject might be sent to a hand-held touch screen remote \[control\]. Whereas, the Kitchen Project might be sent to table top or wall mounted touch screen.





![](https://help.crestron.com/construct/Content/Resources/Images/Send%20Progress.jpg)

_**TheFileTransfer..****.** progress is displayed in the center of the **Project**_ window (see above).


1. Upon successful completion, the Project is listed in the Project window's LoadedProjectInformation scroll box:



![](https://help.crestron.com/construct/Content/Resources/Images/Loaded%20Project%20Information.jpg)



Click the Close button to return to the EasyConfig window.



In the EasyConfig window, the Project Name and Timestamp of the Project is displayed to the right of the Display Project button:



![](https://help.crestron.com/construct/Content/Resources/Images/Living_Room%20on%20Display%20Project%20pane.jpg)