

# Create A New Solution - UI Project

The Solutions Quick Links window allows the user to Create New Solution or Open Existing Solution. The Open Recent Solution pane displays recent Solutions and allows the user to search for Solutions.

## \+ Create New Solution

A Solution is a collection of one or more UI projects. For example, a Home Solution might include separate UI projects for the touch screens or devices used to control the devices in each room or living space. The Living Room UI project could control the Smart TV, sound system, lighting and shades.

A Project is an UI design for a touch screen or device.

![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Solutions%20Quick%20Links_v3.jpg)

1. Click the + Create New Solution button:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20New%20Solution%20button.jpg)

2. In the left-hand Select Project Type pane under User Interfaces, select UI Project:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Select%20Project%20Type.jpg)

3. In the right-hand User Interfaces > UI Project pane, enter a Solution Name and Project Name in the Solution Name and Project Name text fields respectively.



Crestron Construct will initially assign the Project Name the same name as the Solution Name. The Project Name can be modified.



**Note**: Construct supports spaces and hyphens in Solution, Project, Page, Widget and Asset names. Assign informative and readable names that indicate use or purpose. Avoid the commonly restricted characters: < > : " / \ \| ? \*. These are not supported.



For more information; See [Naming Solutions, Projects, Pages, Widgets & Assets](https://help.crestron.com/construct/Content/Topics/UI%20Editor/Solutions,%20Projects%20&%20Pages/Naming%20Solutions.htm).



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Create%20UI%20Project_v6.jpg)
4. Select the inherited Project Name, press Del and then type an unique Project Name: **![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Project%20Selected_v2.jpg)**



**![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Create%20UI%20Project_v5.jpg)**

**Note:**

Both the Solution Name and Project Name will be initially assigned the same value that is first typed by the user in either field. If the user moves from one field to the other and changes the value, then the tracking behavior stops.

A user can start typing in Project Name text field first and the Solution Name will track the same value until the user enters the Solution Name text field and changes the value.

1. In Location, click the File Folder smart icon to modify the default file location for the Solution and its Project(s):



![](https://help.crestron.com/construct/Content/Resources/Images/Location.jpg)

2. Under Location, select the Put solution and project in the same location check box, if applicable, to put both the Solution and Project in the same directory:



![](https://help.crestron.com/construct/Content/Resources/Images/Location%20Checked.jpg)

3. Under CH5 Version, click on the drop-down to select the CH5 Version or to [Manage CH5 Versions](https://help.crestron.com/construct/Content/Topics/UI%20Editor/CH5%20Versioning.htm#Manage_CH5_Versions):



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/CH5%20Version_V2.jpg)

Crestron Construct displays a notification when a new CH5 Version is available for installation:

![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/New%20CH5%20version%20available.jpg)

For more information on CH5 Versions and the CH5 Version Manager see: [CH5 Versions & Managing CH5 Versions](https://help.crestron.com/construct/Content/Topics/UI%20Editor/CH5%20Versioning.htm).

4. Select the Theme drop-down to modify the Theme:



![](https://help.crestron.com/construct/Content/Resources/Images/Theme%20Drop%20Down.jpg)
5. Click in the Theme text field to display the Theme drop-down.
6. In the Theme drop-down, select the applicable Theme(s) check box:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Choose%20Theme.jpg)

Upon selection the number of Themes selected and the default Theme will be displayed:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Number%20of%20Themes.jpg)

The Project Theme(s) can be modified afterward during Project design.

1. Select the Project and right-click.
2. From the Project's right-click menu, Select Project Properties:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Select%20Theme%20Project%20Properties.jpg)


- Select the Project Theme(s) accordingly and click the Save Changes button:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Project%20Properties%20-%20Modify%20Theme.jpg)



**Notes:**
  - The Theme files must be located in a fixed directory called Themes that will be created by the UI Plugin installer.
  - Construct will verify that the Theme file (.zip) is valid.
  - One or more Themes can be selected when a new Project is added to a Solution.
  - Any Theme can be selected that is included in the current Project at design time using the Project Properties > Theme drop-down list. Select a default Theme via the right-hand pencil smart icon and review it.
  - The Override Theme Color check box and Theme Page Color color picker will only be visible when a single Theme is selected. If multiple Themes are selected, these controls will be hidden.
  - The Project compiled output file contains all of the Themes that are selected in the Project and the serial Runtime Theme Join can be used to change the different Themes at runtime.

11. Click in the Device Resolution(s)\* text field and select the applicable device resolutions from the scroll box:



    ![](https://help.crestron.com/construct/Content/Resources/Images/Device%20Resolutions%20Scroll%20Box.jpg)

12. Scroll to the bottom of the Solutions Quick Links window to display the Resulting Project Structure's file path:



    ![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Resulting%20Project%20Structure_v3.jpg)

13. Click the Create button to create the Solution and its Project and to open the UI Editor Workspace:



    ![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Create%20Button_v3.jpg)


## UI Editor Workspace - Layout

The UI Editor Workspace is divided into functional sections and panes--which can be re-sized, locked (pinned), and collapsed, as needed, to increase the size of the Workspace.

![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/UI%20Workspace%20Layout-V2.jpg)

- TheUI Editor Toolbarprovides the following smart icons--when a page is opened:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/UI%20Editor%20Toolbar%20May%202025.jpg)


  - Save

  - Save All

  - Open

  - Copy

  - Paste

  - Paste Special

  - Undo

  - Redo

  - Build

  - Reset

  - Zoom In, Zoom 100%and Zoom Out

  - Code </>

  - Vertical and Horizontal page centering

  - Top, Middle and Bottom vertical page alignment

  - Left, Center and Right horizontal page alignment

  - SameWidth **,** SameHeight andSameW&H componentsizing

  - EqualizeVertical andEqualizeHorizontal spacing between components

  - DigitalAssign,AnalogAssign andSerialAssign assign **Digital**, **Analog** and **Serial** joins


When a Solution is initially opened no Project Page is opened. In this case, only the Save All, Open and Build smart icons are available for use:

![](https://help.crestron.com/construct/Content/Resources/Images/Initial%20UI%20Toolbar.jpg)

To display the smart icon names/functions:

1. From the Menu bar, select Tools > Options: **![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Tools%20Options.jpg)**

2. In the left-hand pane expand Environment and selectGeneral.

3. In the right-hand Toolbar pane select the Show text labels in toolbar check box and click Save:



     ![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Options_v3.jpg)



     **Note:** By default, the smart icon names/functions are **not** displayed.


- The Solution Explorer lists the Solution Name, Project Name(s), Hard Buttons, Project Pages, Assets and Widgets:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Solution%20Explorer%20Annonated_v2.jpg)

In this example, Equipment Room is theSolutionName.

Equipment Room and Lab are **Project** **Names** and the Lab Project has a Page named Main Menu.



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/PROPERTIES.jpg)

In this example, the Page named Main Menu is the Project Page and the Properties Grid is displayed.

In the SolutionExplorer tree:


  - Single-Click to select a Solution, Project, Page **,** HardButton **,** Asset or Widget **.**

  - Double-Click to open it.

  - Ctrl+Click or Shift+Click to select multiple items in the Solution Explorer tree.

## Add a Page

1. In the Solution Explorer, select the applicable Project, right-click, and select Add Page from the drop-down:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20PAge.jpg)

2. In the Add New Page window, enter the Page Name:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20New%20Page/Add%20New%20Page.jpg)

3. Select the Set this page as the Start Page for the Touch Screen check box, if applicable:



![](https://help.crestron.com/construct/Content/Resources/Images/Set%20this%20page%20check%20box.jpg)

4. Select the following additional New Page options as applicable:
   - **Preload Page**: when selected/enabled, Preload Page will prioritize resource loading of elements on the page. This will slow-down initial project load, but provide a better overall user experience. Preload does not cache the page.

   - **Cache Page**: when selected/enabled, Cache Page will cache the page elements in memory. In order to prevent excessive runtime memory usage, page caching should only be enabled on the most used pages in a project.

   - **Page Background Colo** r **:** sets the Page Background Color.

1. Cache Page must be selected to enable the Page Transition drop-downs:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20New%20Page/Transition.jpg)



**Note:** Select the Cache Page check box and unselect the Preload Page check box to ensure first view of pages that have animations shows the animation(s) on the page and/or widgets on the page **.**


1. Use the Transition In and the Transition Out drop-downs to set the corresponding Page Transition(s):



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20New%20Page/Transition%20Drop%20Down.jpg)



Available Page Transitions for Transition In and Transition Out, as of this writing, include:
   - None

   - fade in

   - fade in fast

   - fade in slow

   - fade in up big

   - fade in up big fast

   - fade in down big

   - fade in down big fast

   - zoom in
2. Click on the Transition (In/Out) Time and the Transition (In/Out) Delay spin up or down arrows to set the corresponding Transition Time and Transition Delay:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20New%20Page/Transition%20Time.jpg)

Or type the Transition Time and the Transition Delay directly into their corresponding text fields.


1. In the SolutionExplorer, double-click the newly added Page to open it, the Workspace (Body/Canvas), the PropertiesGrid, BlockManager and Layer Manager panes:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Added%20as%20Start%20Page.jpg)

The staricon indicates that the selected Page is the Start Page for the touch screen or device:





![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20New%20Page%20Window.jpg)

The added Page named Server Room 4 is shown above with a blank Workspace (Body/Canvas).



Double-click on a Page in the Solution Explorer to display it:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Pages.jpg)



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Page%20Initial%20Design.jpg)

In this example, the **Project** named Lab is displaying the **Page** named: Main Menu after the Page's initial design.

2. Click the AddPage smart icon and follow [Add New Page Steps 1-7](https://help.crestron.com/construct/Content/Topics/UI%20Editor/Create%20A%20Solution.htm#Create_New_Page) (see above) to create additional Pages:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20PAge.jpg)

Use the EditPage and Delete **Page(s)** smart icons respectively to edit or delete ProjectPages:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Edit%20Delete%20Page.jpg)

The Edit Page window allows the user to rename the Page via the New Name text field.

Use the JoinSelector orContractGenerator smart icon to assign the Page's Page Visibility Join number or the Page'sPageVisibilityContract Join respectively:

![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20New%20Page/Edit%20Page.jpg)

In this example, the Main Menu is the Page's CurrentName; its NewName will be Menu as shown above. Using the JoinSelector's smart icon ( **#**), the PageVisibilityJoin was set to 1. The Page Visibility Join can also be set by typing in the corresponding text field.



To use the Join Selector, click on the **#** smart icon and then select a join number from the table:



![](https://help.crestron.com/construct/Content/Resources/Images/Join%20Selector.jpg)

Select the HIDE ALL # IN USE check box to display only available join numbers not already in use.

To use theContract Generator, click on the **C** smart icon. The ContractGenerator generates Contract Joins in the namespace of a Control Join ID when the Solution is built. See [Contract Generator](https://help.crestron.com/construct/Content/Topics/UI%20Editor/Contract%20Generator.htm).



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20New%20Page/Edit%20Page%20Contract%20Enabled.jpg)

In this example, the PageVisibilityJoin has been ContractEnabled **.**


## Page Design

1. From the UI Editor Toolbar, click on the Touch Screen smart icon drop-down and select the applicable touch screen or device:

![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Select%20Touchscreen%20from%20Toolbar.jpg)

For best results, design the user interface (UI) for the highest resolution screen first. This is known as a Desktop First approach.

![](https://help.crestron.com/construct/Content/Resources/Images/touch%20screen%20drop-drop%20resolutions.jpg)

In this example, the TSW-1070 was selected because it has highest resolution of the two touch screens that were selected during Solution creation. The TSW-1070's resolution is 1280 x 800; whereas, the TSW-570's resolution is 640 x 360.

Additional supported resolutions can be added viaEdit>ResolutionSettings (Alt+Ctrl+S). Resolutions can be searched for, filtered, included or excluded:

![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Resolution%20Settings.jpg)

Or via the **Project's** right-click menu:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Right_Click%20Resolution%20Settings.jpg)



See [Resolution Settings](https://help.crestron.com/construct/Content/Topics/UI%20Editor/Resolutions%20Settings.htm).



Breakpoints control how PageDesign and PageDesign modifications are inherited between resolutions—as well as how and when Page Design modifications are resolution specific. See [Breakpoints](https://help.crestron.com/construct/Content/Topics/UI%20Editor/Breakpoints.htm).

2. From the BlockManager pane, select and drag and drop Components onto the ProjectPageWorkspace.

In the Block Manager, Components are organized into Component categories. For example, the Keypad Component category includes the Dpad and the Keypad Components:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Component%20Category.jpg)



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Page%20Design%20Sample.jpg)



Sample Project Page



Components can be manually positioned and aligned -or- aligned via the UIEditor Toolbar's alignment smart icons:



![](https://help.crestron.com/construct/Content/Resources/Images/Toolbar%20Alignment%20SmartIcons%20Revised.jpg)

3. On the Workspace, click on the Component to select it. Use Ctrl+Clickto multi-select Components -or- click and drag over the Components to lasso select them:



![](https://help.crestron.com/construct/Content/Resources/Images/Multiselect%20Revised_v2.jpg)

Selected **Components** are framed indark blue.



![](https://help.crestron.com/construct/Content/Resources/Images/Lasso%20selected.jpg)

The highlighted **Components** are being lasso selected and will be framed in dark blue after they are selected.



![](https://help.crestron.com/construct/Content/Resources/Images/Left%20Aligned_v2.jpg)

In this example, the Buttons were multi-selected and then Left aligned on the Page via the UI Editor Toolbar's Left alignment smart icon. The Left alignment is determined by the last selected Component—the Component displaying its adorners. Therefore, the On button will determine the other selected Component's  Left alignment.



The Off button was given the same Left alignment as the On button because the On button was the last selected Component.

4. Use theUI Editor Toolbar'ssame size smart icons to set selected Components to the Same Width, Same Height or Same W&H (width and height):



![](https://help.crestron.com/construct/Content/Resources/Images/Same%20Width.jpg)

![](https://help.crestron.com/construct/Content/Resources/Images/Different%20Width%20and%20Height_v2.jpg)

The above Components have different widths and heights.

Click the Same W&H smart icon to give the selected Components the same width and height:



![](https://help.crestron.com/construct/Content/Resources/Images/Same%20W_H%20Revised.jpg)

The width and height is determined by the last selected Component—the Component displaying its adorners. Therefore, in the above example, the On button will determine the other selected Component's  width and height.





![](https://help.crestron.com/construct/Content/Resources/Images/Set%20To%20Same%20Width_Height_v2.jpg)

In this example, the Off button was given the same width and height as the On button because the On button was the last selected Component.

5. Use the UI Editor Toolbar's Equalize Vertically and Equalize Horizontal smart icons to equalize the vertical and horizontal space between selected Components respectively:





![](https://help.crestron.com/construct/Content/Resources/Images/Not%20Verticallly%20Equalized_v2.jpg)

In this example, the Components have inconsistent vertical space between them; the Components are being lasso selected.



Click the Equalize Vertical smart icon to give the selected Components consistent (equalized) space between them vertically:



![](https://help.crestron.com/construct/Content/Resources/Images/Equalize.jpg)



![](https://help.crestron.com/construct/Content/Resources/Images/Vertically%20Equalized_v2.jpg)

In the above example, the vertical space between the Components has been equalized.

Similarly, if Components are lined up horizontally, then the horizontal space between them can be equalized by selecting the Components and clicking the Equalize Horizontal smart icon:



![](https://help.crestron.com/construct/Content/Resources/Images/Equalize%20Horizontal.jpg)

![](https://help.crestron.com/construct/Content/Resources/Images/Equalized%20Horizontally_v2.jpg)

In the this example, the horizontal space between the Components has been equalized.

6. Use the Component Toolbar above the selected Component to change the selected Component's Z-order by pressing the up-arrow á.

In addition, use the ComponentToolbar to drag and drop the Component(s) to a new position, copy and paste the Component(s) or delete the Component(s); this affects all the selected Components:



![](https://help.crestron.com/construct/Content/Resources/Images/Component%20Toolbar.jpg)

Alternatively, to delete a Component(s) select it and right-click. From the right-click menu, select Delete Object.



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Z-Order/Right%20click%20delete.jpg)

Components can be multi-selected and deleted.





![](https://help.crestron.com/construct/Content/Resources/Images/Multiselect%20with%20copy.jpg)

In this example, the upper two Buttons were multi-selected and the Component Toolbar's Copy & Paste smart icon was clicked; this pasted two additional Buttons below the existing Buttons on the Project Page.





**Note:**



Select a Component and press the applicable Arrow key to reposition it vertically or horizontally four (4) pixels per key press.



Similarly, select a Component and press Ctrl+Arrow key to reposition it vertically or horizontally one (1) pixel per key-combination press, as applicable.

7. Use the Component's adorners' white squares to re-size the Component manually on the fly; when Components are multi-selected only the Component that displays the ComponentToolbar above it will be affected:



![](https://help.crestron.com/construct/Content/Resources/Images/Adorners.jpg)

**Note:**



Select a Component and press the Shift+ Arrow key to re-size its width or height four (4) pixels per key-combination press, as applicable.



Similarly, select a Component and press Ctrl+Shift+Arrow key to re-size its width or height one (1) pixel per key-combination press, as applicable.


## Add New Page

1. In the Solution Explorer, select the applicable Project, right-click , and select Add Page from the drop-down:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20PAge.jpg)

2. In the Add New Page window, enter the Page Name:

![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20New%20Page/Add%20New%20Page.jpg)

3. Select the following NewPage options as applicable:
   - **Set this page as the Start Page for the Touch Screen:** designates the New Page as the Start Page for the Touch Screen.

   - **Preload Page**: when selected/enabled, Preload Page will prioritize resource loading of elements on the page. This will slow-down initial project load, but provide a better overall user experience. Preload does not cache the page.

   - **Cache Page**: when selected/enabled, Cache Page will cache the page elements in memory. In order to prevent excessive runtime memory usage, page caching should only be enabled on the most used pages in a project.

   - **Page Background Colo** r **:** sets the Page Background Color:



     ![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Page%20Background%20color.jpg)



     Color names are supported in the text field.


     1. In the Background Color text field enter the color name.

     2. Click the right hand drop-down arrow to display the color picker.

     3. Click on the color palette or color slider to pick the color:



        ![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Color%20Pick%20-%20page%20background.jpg)

     4. Click the left-hand spin arrows to switch to RGB format:



        ![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/RGB.jpg)


The PageBackgroundColor can be set on a page by page basis. Or a default ThemePageColor can be set via the ProjectProperties. Individual PageBackgroundColors can be set that override the default ThemePageColor.

By default, the first Project Page when added is designated as the Start Page for the Touch Screen, Preload Page is selected and CachePage is unselected.

On subsequent NewPages, initially--by default--Preload Page will be selected and CachePage will be unselected. Unless changed otherwise.
4. Cache Page must be selected to enable the Page Transition drop-downs:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20New%20Page/Transition.jpg)

**Note:** Select the Cache Page check box and unselect the Preload Page check box to ensure first view of pages that have animations shows the animation(s) on the page and/or widgets on the page **.**

5. Use the Transition In and the Transition Out drop-downs to set the corresponding Page Transition(s):



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20New%20Page/Transition%20Drop%20Down.jpg)



Available Page Transitions for Transition In and Transition Out, as of this writing, include:
   - None

   - fade in

   - fade in fast

   - fade in slow

   - fade in up big

   - fade in up big fast

   - fade in down big

   - fade in down big fast

   - zoom in
6. Click on the Transition (In/Out) Time and the Transition (In/Out) Delay spin up or down arrows to set the corresponding Transition Time and Transition Delay:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20New%20Page/Transition%20Time.jpg)

Or type the Transition Time and the Transition Delay directly into their corresponding text fields.

7. Click the Add button:

![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20button-%20new%20page.jpg)

8. The NewPage will be displayed in the Editors pane:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Editor%20pane%20-%20new%20page.jpg)


**Note:** Users should avoid applying a Background Color to the Page or a Widget if the Video Component is used at any level in the hierarchy.

For example:

- If the Video Component is used on the Page, a Background Color should not be applied to the Page.

- If the Video Component is used within a Widget, and that Widget is used on the Page, a Background Color should not be applied at any level.


The Video Component will not function correctly if a Background Color is applied.

### Properties Grid

Select a Component and in the Properties Grid use the applicable text fields, drop-downs and spin boxes to set the Component'scorresponding properties.

#### Interactions

![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Properties%20Interactions%20-%20New.jpg)

In this example, a light bulb icon was set using the Icon Class drop-down.

#### Interactions - Label Mode

Set the Label Mode property to advanced to enable advanced text properties and functionality for the Button, Advanced Button and FormattedText Components:

1. Click on the Label Mode drop-down and select advanced:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Label%20Mode%20Advanced.jpg)

2. In the Label property click on the ellipses button to open the Label Text Editor:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Label%20Mode%20ellispics%20new.jpg)

3. Type the Label text on the Canvas and style the text using the Label Text Editor toolbox's smart icons:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Label%20Text%20Editor%20new.jpg)

4. Click on the ANALOG, SERIAL or DIGITAL buttons to set join numbers and conditions that dynamically control the Label text that is displayed at runtime:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Label%20Mode%20Digital%20Join%20new.jpg)

In this example, a Digital Join Number was set to 1. If the digital join is True , then the Label text: On will be displayed. If the digital join is False, then the Label text: Off will be displayed.



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Set%20Digital%20New.jpg)

5. Click on the HTML button to display the HTML code associated with the configured Join:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/HTML%20Code.jpg)

    See [Label Text Editor](https://help.crestron.com/construct/Content/Topics/UI%20Editor/Label%20Text%20Editor%20with%20Language%20Support.htm).

**Note**: Advanced label settings are lost when the Label Mode is changed from advanced to simple.


#### Theme Mode - Button Styles

Buttons in Crestron Construct provide both the ability for customization as well as pre-set, theme-based properties. The Theme Mode property will determine if the Button can be customized or will use theme-based properties.

1. From the Theme Mode property drop-down, select custom or theme as applicable:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Theme%20Mode.jpg)

Note: custom is the default when a Button is added.
   - custom allows the Button to be fully customized.

   - theme designates that the Button will use only pre-set, theme-based properties as determined by the corresponding Button Style.
2. From the Button Style property drop-down, select the applicable Button Style:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Button%20Styles-new.jpg)



If no customization is required, then the Button Style property can be set to one of the following theme-based values:
   - default

   - primary

   - info

   - text

   - danger

   - warning

   - success

   - secondary

#### Receive Feedback

![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Button%20Receive%20Feedback.jpg)

**Receive Feedback** allows the user to set the following input joins that receive signals from the control system:

- Receive Analog Feedback
  - Mode
    - Sets the Component mode.

    - Current mode matches the signal given.

- Receive Digital Feedback


  - Visibility
    - Enables Component visibility.

    - High/1 = Component visible; Low/0 = Component not visible.

  - Enable
    - Enables the Component.

    - High/1 = Component enabled; Low/0 = Component disabled.
  - Selected
    - Sets the Component, typically a Button, to the Selected State.

    - High/1 = Component (Button) in SelectedState; Low/0 = Component (Button) not in Selected State.
- Receive Serial Feedback
  - Indirect Text:
    - Sets the Component’s text.
  - Indirect Rich Text
    - Sets the Component’s text with additional formatting options.
  - Icon:
    - Sets the Component’s Icon Class. Icon Class.

#### Setting Joins

1. To set an input join, click in the applicable feedback join's text field and assign it a join number -or- click on the Join Selector smart icon number sign **#**:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Joins%20Assigned.jpg)



From the menu bar, select Tools > Join Manager to view assigned and available join numbers. See [Join Manager.](https://help.crestron.com/construct/Content/Topics/UI%20Editor/Join%20Manager.htm)

2. To set a Contract Join for the input join, click on the Contract Generator smart icon **C**(see above). See [Contract Generator](https://help.crestron.com/construct/Content/Topics/UI%20Editor/Contract%20Generator.htm).

**Note:** Widgets can be set to global or non **-** global via the Global Contract drop-down property.



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Widget%20Global%20Contract.jpg)


   - Global means that the Widget only needs to be programmed once. Global Widgets are best used for something that needs to appear on multiple pages--such as a Page header or footer.

   - Non-global means that each reference needs to be programmed.
3. To set a Reserved Join for the input join, click on theReserved Joinssmart icon **R** (see below). Select the applicable Reserved Join from the active resolution's Reserved Joins scroll box. See [Reserved Joins](https://help.crestron.com/construct/Content/Topics/UI%20Editor/Reserved%20Joins.htm).


1. ClickAssign allows the user to set input and output joins automatically for the following Components:


   - Button

   - Color Chip

   - Formatted Text

   - Image

   - Segmented Gauge

   - Slider

   - Textinput

   - Toggle

   - Wifi Signal Level Gauge


1. To set input joins automatically, click on the Digital Assign, Analog Assign or Serial Assign smart icons, as applicable on the UI Editor Toolbar:



      ![](https://help.crestron.com/construct/Content/Resources/Images/Click%20Assign.jpg)

2. This puts the application workspace into Click Assign mode and disables all the Managers until the Esc key is pressed or another Project Page is selected.

3. By default, joins will be set starting at the first unused join. Otherwise, select the applicable join assignment radio button and click the SET button (see below):



      ![](https://help.crestron.com/construct/Content/Resources/Images/Set%20joins%20automatically.jpg)

      Digital Assign, Analog Assign and Serial Assign have identical join assignment radio buttons/options.

4. Click on each Component on the Project Page to set the input joins based on the join assignment option selected above.

5. If the Component already has been assigned a join, then the Object Already Joined window is displayed,:



      ![](https://help.crestron.com/construct/Content/Resources/Images/Object%20Already%20Joined.jpg)

6. Click the REPLACE button to replace the existing join with an automatically assigned join -or- click the CANCEL button to retain the existing join.


1. To exit Click Assign press the Esc key or select another Project Page.


See [Click Assign](https://help.crestron.com/construct/Content/Topics/UI%20Editor/Click%20Assign.htm).

#### Send Digital Command

**Send Digital Command** allows the user to set the following output joins that are sent to the control system:

- Visibility
  - Reports the Component’s visibility.
- Press
  - Reports if the Component is being pressed.

  - High/1 = Component being pressed; Low/0 = Component not being pressed

![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Send%20Dgital%20Command.jpg)

1. To set an output join, click in the applicable output join's text field and assign it an unique join number -or- click on the Join Selector smart icon number sign **#** (see above).

2. To set a Contract Join for the output join, click on the Contract Generator smart icon **C**(see above). See [Contract Generator](https://help.crestron.com/construct/Content/Topics/UI%20Editor/Contract%20Generator.htm).

3. To set a Reserved Join for the output join, click on the Reserved Joins smart icon **R** (see below). Select the applicable Reserved Join from the active resolution's Reserved Joins scroll box. See [Reserved Joins](https://help.crestron.com/construct/Content/Topics/UI%20Editor/Reserved%20Joins.htm).



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Send%20Command%20Reserved%20Join.jpg)

4. To set output joins automatically, click on the Digital Assign, Analog Assign or Serial Assignsmarticon, as applicable on the UI Editor Toolbar:



![](https://help.crestron.com/construct/Content/Resources/Images/Click%20Assign.jpg)

See above (Receive Feedback: [Step iv](https://help.crestron.com/construct/Content/Topics/UI%20Editor/Create%20A%20Solution.htm#Click_Assign))


#### Position

![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Properties%20Position.jpg)

The Position spin boxes will dynamically change if the Component is dragged and dropped to a new position on the Workspace. Similarly, the Size spin boxes will also dynamically change if the Component is re-sized using its adorners.

#### Size

![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Properties%20Size.jpg)

The Size spin boxes will dynamically change if the Component is re-sized using its adorners.

#### Appearance  ![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Properties%20Appearance.jpg)

#### Label styles  ![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Properties%20Label%20Styles.jpg)

#### Icon styles  ![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Properties%20Icon%20Styles.jpg)

#### Checkbox styles  ![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Properties%20Checkbox%20Styles.jpg)

Use the Position, Size, Appearance, Label styles, Icon styles and Checkbox styles sections' drop-downs, spin boxes and text fields to define the Component's corresponding properties and styles.

### Layer Manager

1. TheLayerManager displays the Component Z-order:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Layer%20Manager.jpg)

2. Select a Component and click the Hide/Show smart icon (eye ball) to hide or show the Component:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Hide%20On%20Button.jpg)

In this example, the On button will be hidden.





![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/On%20Button%20hidden.jpg)

The On button has been hidden as indicated by its entry in the Z-order being grayed out and a diagonal line through the Hide/Show smart icon (eye ball).

3. Select the Component or Widget (see below [Widgets - Layer Manager & Z- Order](https://help.crestron.com/construct/Content/Topics/UI%20Editor/Create%20A%20Solution.htm#Widgets_Layer_Manager)) and right-click to change its Z-order position.

4. From the drop-down select the options as follows:
   - Delete Object: Deletes the Component.

   - Move to Front (Alt+=): Moves the Component or Widget to the Front of the Z-order and positions it at the forefront.

   - Move to Back (Alt+-): Moves the Component or Widget to the Back of the Z-order and positions it furthest back.

   - Move Forward (=) : Moves/steps the Component or Widget forward through the Z-order.

   - Move Back (-): Moves/steps the Component or Widget backward through the Z-order.



     ![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Z-Order/Z-order%20Menu.jpg)

     In this example, Button 1 will be moved from the back of the Z-order to the front.



     ![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Z-Order/Layer%20Manager%20Button%201%20Before%20Move.jpg)

     ![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Z-Order/Button%20Front%20Z-order.jpg)

     ![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Z-Order/Layer%20Manager%20Button%201%20After%20Move.jpg)

     As shown above, Button 1 has been moved to the front of Z-order(and forefront on the Canvas) via the right-click menu's Move to Front (Alt++) option. Its new position is shown in the Layer Manager.



     **Note:** The right-click Z-order Move menu options are only available if one Component is selected. These options will be grayed out and unavailable if multiple Components are selected:



     ![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Z-Order/Multiple%20Selected.jpg)

     In this example, multiple Components have been selected. Therefore, the right-click Z-order Move menu options are grayed out and unavailable. However, Delete Object is still available and the multi-selected Components can be deleted.
5. Alternatively, select a Component's Z-order entry's Move cursor (four-arrow cursor) and drag the Component to the applicable position in the Z-order:

![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Order%20original%20position.jpg)

In this example, the Dim button has been selected and its Move cursor has been clicked.





![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/New%20Z%20order%20position.jpg)



In this example, the green line displays the Dim button's new target location in the Z-order.

**Note**: In the Layer Manager Components are listed by their Component Name versus their Label.



The Dim Button's Component Name is Button\_2 and its Label is Dim:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Component%20Name%20new.jpg)



The Component Name could be revised and appended to include the Component Label and reflect the Component's function:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Component%20Name_Label.%20newjpg.jpg)



This would then be reflected in the Layer Manager:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Layer%20Manager%20Component%20Name_Label%20new.jpg)


## Adding & Configuring Keypads and Dpads

1. Select either the Dpad or the Keypad from the BlockManager **and drag and drop it onto the Project Page:**



**![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Keypad%20Components.jpg)**

2. Use the Properties grid to set the Keypad's or Dpad's top-level properties in the Interactions, Receive Feedback, Send Command, Position, Button Styles and Pressed Button Styles sections.



**Note:**



Use the Layer Manager to set button-level properties ( [See below: Adding & Configuring Keypads and Dpads - Steps 5- 6](https://help.crestron.com/construct/Content/Topics/UI%20Editor/Create%20A%20Solution.htm#configure)).



Two noteworthy top-level properties include Size under Interactions and DigitalStart under SendCommand.

3. Under Interactions, select the Keypad or DPad size. As of this writing, the only following fixed sizes: regular, x-small, small, large and x-large are supported. This ensures the best possible proportional scaling and alignment of Button labels and icons:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Keypad%20Size.jpg)

_Custom sizing may be supported at a later date._

4. Under Send DigitalCommand, set the Digital Start join number. The Digital Start join sets the starting digital join number for the keys in the Keypad or Dpad order:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Keypad%20Digital%20Start.jpg)

The Keypad's keypad order is 0-9, \* and #.



![](https://help.crestron.com/construct/Content/Resources/Images/Keypad%20Component.jpg)



    Therefore, if its Digital Start number is set to 100, then the keypad's **digital join**numbers are as follows:



0 = 100 (Digital Start join)

1 = 101

2 = 102

3 = 103

4 = 104

5 = 105

6 = 106

7 = 107

8 = 108

9 = 109

\\* = 110

\# = 111





Similarly, the Dpad's keypad order is Up, Down, Left, Right and Enter (center key).



![](https://help.crestron.com/construct/Content/Resources/Images/Dpad%20Component.jpg)



Therefore, if its Digital Start number is set to 100, then the keypad's **digital join**numbers are as follows:



Up    = 100 (Digital Start join)

Down  = 101

Left  = 102

Right = 103

Enter = 104

5. To configure a button/key, select it in the Layer Manager:



**Keypad**

![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Keypad%20Layer%20Manager%20Button%202.jpg)



**Dpad**

![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Dpad%20Layer%20Manager%20Down.jpg)

6. Select the button/key in the LayerManager. In the Properties Grid **'s** Interactions section set the button's/key's Icon Class, Label Minor, Label Major and Pressed( State).



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Configure%20Key%202.jpg)

In this example, three Keypad buttons/keys have been configured. Specifically, Button 2's properties are shown above.



Button 2's Icon Class was set to display a locked lock. The Label Minor was set to Lock.



In addition, if a valid Icon Class is set, then the Label Major will not be displayed. Therefore, the Label Major does not necessarily need to be deleted. In this case, if the Icon Class is deleted and reverts to none, the Label Major will be displayed again:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Label%20Major%20not%20deleted.jpg)

In this example, a valid Icon Class is set. The Label Major is not displayed, but the property value is still set. Therefore, as stated, if the Icon Class is deleted and reverts to none, then the Label Major will be displayed again:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Icon%20Class%20deleted.jpg)

In this example, the Icon Class was deleted; the result: the Label Major is displayed again; in this case the number 1.


## Adding Button Modes & Configuring Button States

The Button Component can have multiple Button Modes.

Each Button Mode will have a normal, pressed and selected Button State; each Button State can be separately configured in the Properties Grid.

1. Select the Button **.** On the Component Toolbar above the Button, click on the plus sign ( **+**) to add Button Modes:

![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20Button%20Mode_v3.jpg)

![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Button%20Modes_v2.jpg)

In this example, five Button modes. as shown in the Layer Manager, have been added: mode 0 through mode 4. Mode 4 has been selected and expanded to display its normal, pressed and selected button states.

2. Select a Button mode in the Layer Manager. Expand the Button Mode and select the applicable Button State to configure its properties in the Properties Grid.



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/mode%200%20normal.jpg)



In this example, mode 0's normal Button State was selected in the Layer Manager. In the Properties Grid, its Label property was set to On and its Fill Color was set to green.



On the Component Toolbar, normal is shown in dark blue, indicating that the normal Button State has been selected and has the active focus.






## Deleting Button Modes


1. Select the applicable Button andits correspondingButton Mode in the Layer Manager **:**



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Layer%20Manager%20Delete%20Button%20Mode-V1.jpg)

2. On the Workspace Body/Canvas, press the delete smart icon (garbage pail) above the corresponding Button and Button Mode:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Delete%20Button%20Mode-v2.jpg)

This deletes only the selected Button Mode; all other Button Modes remain in place and intact. In this example, only mode 1 will be deleted; mode 2 will remain intact.

The remaining Button Modes will be renumbered in sequence: mode 2 now becomes mode 1; mode 3 now becomes mode 2; etc.


## Adding an Asset

1. In the Solution Explorer, right-click on the Project and select Add Assets from the right-click menu:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20Assets/Add%20Assets.jpg)

2. In the Add Project Asset window, enter the Asset's name in the Asset Name field and select the corresponding Asset Source radio button: File or URL:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20Assets/Add%20Project%20Asset.jpg)

3. Click the File Folder smart icon to browse to the Asset, if the Asset Source is a File.

4. Navigate to the Asset's file location, select it and click the Open button:

![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20Assets/Add%20Single%20Asset.jpg)

Press Ctrl+click to select multiple Asset files.



If multiple Assets are selected their file names will be used instead of the Asset Name entered in the Add Project Asset window;



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20Assets/Add%20Multiple%20Assets.jpg)

Valid Image Files include \*.svg, \*.png, \*.jpg, \*.jpeg and \*gif.


1. In the Add Project Asset window, click the ADD button:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20Assets/Add%20Project%20Asset%20Window.jpg)

2. In the Properties Grid, select the Asset to add it to the selected Component::



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Asset%20Added%20to%20Canvas.jpg)

In this example, the Files ImageAsset was added to the ImageComponent **.**





Assets are listed in the Solution Explorer after they are added:

![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20Assets/Asssets%20Added.jpg)

3. Similarly, an Asset can be added from an URL.

4. Type the Asset's name in the Asset Name text field. Select the Asset Source URL radio button, enter the URL's Username and Password in the corresponding text fields. And enter the Asset's URL in the URL window, and click the ADD button:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20Assets/Add%20URL%20Asset.jpg)


### Include All Assets with Compile

All Assets can be included in the compiled output regardless of whether or not they are being used. Assets can be dynamically selected at runtime using a control system program via a Serial join or Contract join.

1. From the Project's right-click menu, select Project Properties and then select the Include All Assets with Compile checkbox:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Inlcuded%20All%20Assets%20with%20Compile.jpg)


## Adding a Widget

A Widget is a sub-page container that contains Components.

After it is configured with Components, a Widget can be added to a Project Page. For example, a Widget that controls the Smart TV could be added to the Project's Living Room Page.

1. In the SolutionExplorer, click on the Project's right-click menu and selectAddWidget **:**

![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20Widget.jpg)

2. In the Add New Widget window, type a Widget name in the Widget Name text field:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Addd%20New%20Widget%20Dialog.jpg)

**Note:** The Widget Name populates the read-only Widget Name property in the Proprieties Grid:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Widget%20Name/Widget%20Name%20Short.jpg)

    (see below: [Widget Name & The Properties Grid](https://help.crestron.com/construct/Content/Topics/UI%20Editor/Create%20A%20Solution.htm#Widget_Name_&_The_Properties_Gird)).

3. Under Canvas, use the Width(px) and Height (px) spin boxes to set the Widget size:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Widget%20Canvas%20Size.jpg)

The Widget size can be modified during Page design.

4. Select the Widget Background Color check box to set the Widget Background Color.



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Widget%20Background%20Color.jpg)



Color names are supported in the text field.


1. In the Background Color text field enter the color name.

2. Click the right hand drop-down arrow to display the color picker.

3. Click on the color palette or color slider to pick the color:



      ![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20Widget%20-%20BK%20Color%20-%20Color%20Picker.jpg)


1. Click the left-hand spin arrows to switch to RGB format:



      ![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20Widget%20-%20BK%20Color%20Hex.jpg)


Press the ADD button when finished.

5. From the Block Manager pane, add the applicable Components to the Widget via drag and drop.



Use the Properties Grid to configure each Component as required:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Widget%20Containter.jpg)

In this example, two FormattedTextComponents were added: Smart TV and Volume. Two Buttons were added to turn the Smart TV: On and Off. A Silder was added to adjust the volume.

6. Click the Save or Save All smart icon on the UI Editor Toolbar to save the configured Widget. The saved Widget will be listed under Widgets in the Solution Explorer; it will also be listed under the Widget Components in the Block Manager when a Project Page is selected for Widget placement:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Widgets%20in%20Solution%20Explorer.jpg)



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Block%20Manager%20Widget%20Components.jpg)

7. From the Solution Explorer, select the applicable Project Page for Widget placement.

8. Drag and drop the WidgetfromtheBlock Manager's WidgetComponents pane to its position on theProjectPage **.**



**![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Widget%20dragged%20and%20dropped.jpg)**



**Note:**



For Project Page placement, a Widget can be selected from **only** the Widget Components pane.





![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Widget%20added%20to%20Page.jpg)

In this example, the Smart TV Widget has been dragged and dropped from the WidgetComponents pane to the LivingRoomProject **'s** Main Menu Page.

9. Select and double-click on the Widget in the Solution Explorer to edit it:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Edit%20Widget.jpg)



The Widget will be displayed on the Workspace **:**



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Widget%20Editing.jpg)


### Setting Widget Transitions

1. Select the Widget on the Project Page.

2. In the Property Grid's Transitions section select the Widget's Transition In and Transition Out from the corresponding drop-downs:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Widget%20Transitions.jpg)

3. Set the Widget Transition Time and Transition Delay (in seconds) in the corresponding text fields:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Wdiget%20Transition%20Time.jpg)


### Widgets - Layer Manager & Z-Order

1. Select the Widget on the Project Page and right-click to change its Z-order position.

2. From the drop-down select the options as follows:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Widget%20right-click.jpg)


   - Delete Object: Deletes the Widget.

   - Move to Front (Alt+=): Moves the Widget to the Front of the Z-order and positions it at the forefront.

   - Move to Back (Alt+-): Moves the Widget to the Back of the Z-order and positions it furthest back.

   - Move Forward (=) : Moves/steps the Widget forward through the Z-order.

   - Move Back (-): Moves/steps the Widget backward through the Z-order.
3. The Widget's Z-Order can also be changed by dragging and dropping it into position in the Layer Manager.

4. In the Layer Manager, select the Widget's Move cursor (four-arrow cursor) and drag the Widget to the applicable position in the Z-order:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Widget%20Drag%20in%20Layer%20Manager.jpg)

In this example, the green line displays theWidget's new target location in the Z-order.



For more information see above: [Layer Manager](https://help.crestron.com/construct/Content/Topics/UI%20Editor/Create%20A%20Solution.htm#Layer_Manager).


### Hiding Widgets

Widgets on a Project Page can be hidden during both Page design and runtime.

Hide Widgets, as needed, during Page design to work more efficiently while designing the Project Pages. This can prevent Widgets from overlapping.

Hide Widgets, as needed, during runtime depending on the device resolution. As stated, this can be useful when working with multiple resolutions when a Widget needs to be visible in one resolution and hidden in another.

#### Hiding **All** Widgets

1. Click on the Page Body (canvas) to give it the active focus. The Body will be framed in purple when it has the active focus.



![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Hiding%20Widgets/Active%20Focus.jpg)

2. Press Alt+H on a Window-based computer to hide **all** the Widgets on the current Page.

3. Press Option+H on an Apple-based computer to hide **all** the Widgets on the current Page.

4. In the Layer Manager, click the Hide/Show smart icon (eye ball) to the left of an individual Widget to toggle its visibility on and off.





![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Hiding%20Widgets/Layer%20Manager%20High%20Show.jpg)

In this example, Widget1 is shown on the Project Page. Widget2 is hidden as indicated by it being grayed out and there being a diagonal line through the smart icon:



![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Hiding%20Widgets/Hide.jpg)


For more information: See [Hiding Widgets.](https://help.crestron.com/construct/Content/Topics/UI%20Editor/Solutions,%20Projects%20&%20Pages/Hiding%20Widgets.htm)

## Widget Name & The Properties Gird

The Widget Name populates the read-only Widget Name property in the Properties Grid:

![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Widget%20Name/Widget%20Name%20property.jpg)

The Widget Name and Component Name will match.

The Widget Name can only be modified by editing the Widget itself:

1. In the Solution Explorer, click on the Widget's edit (pencil) icon:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Widget%20Name/Edit%20Widget%20Icon.jpg)

2. In the Edit Widget window, enter the new Widget Name in the New Name text field and press the OK button:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Widget%20Name/Edit%20Widget%20window.jpg)

The new Widget Name will be displayed in the Properties Grid and in the Block Manager under Widget Components:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Widget%20Name/New%20Widget%20Name.jpg)

**Note:** Updating the Widget Name will not update the Component Name.

![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Widget%20Name/Block%20Manager.jpg)


## Saving the Solution and its Project(s)

1. Press the Save (Ctrl+S) smart icon on the UI Editor Toolbar to save **only** the active Editor:



![](https://help.crestron.com/construct/Content/Resources/Images/Save%20smart%20icon.jpg)

2. Press the Save All (Ctrl+Shift+S) smart icon to save the Solution and its Projects:



![](https://help.crestron.com/construct/Content/Resources/Images/Save%20All.jpg)

3. If the Solution is unsaved when exiting Crestron Construct, press the Save button in the Close Solution window:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Close%20Save%20Solution.jpg)


## Save As - Project

A Project can be saved as another Project **.**

1. In the SolutionExplorer, select the applicable Project, right-click and select Save As...:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Save%20As%20Project.jpg)

By default, an -# is appended to the existing Project name and the Project is added to the current Solution:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Project%20Save%20As%20Appended%20Name-v2.jpg)

2. If applicable, select the NewProjectName text field and press Backspace to delete the default Project name.



**Note:** By default, any existing contract signals will remain linked in the Saved As version of the Project (see above). When contract signals are linked, all new components and thus all GUI extenders will not get commented in SIMPL.



Otherwise, select the Unlink the existing signals check box to unlink these signals:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Project%20Save%20As%20Unlink%20Signals.jpg)

If contract signals are unlinked and then a program is synchronized to the new chd file, GUI extenders will be commented in SIMPL.

3. Enter a user-friendly Project name and press theSAVE button:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Save%20As%20Project%20New%20Name%20v2.jpg)

The Saved As Project is added to the current Solution:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Save%20As%20in%20Solution%20Explorer.jpg)



Notes:
   - Project can be saved under a different name in the current Solution when the Add to existing solution check box is enabled.

   - Project can be saved under a different name to a manually specified folder by disabling the Add to existing solution check box:



     ![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Save%20As%20Unchecked%20v2.jpg)

     Select the applicable folder in Select a path dialog box and click the Select Folder button:



     ![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Select%20a%20path.jpg)

## Add a New Project to the Current Solution

1. Click on the Solution's hamburger menu and select Add New Project from the drop-down menu:





![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Solution%20Hamburger%20Add%20New%20Project.jpg)



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Solution%20Explorer%20Add%20New%20Project.jpg)

2. In the Create New Project window, assign the new Project a Project Name and then click the Create button:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/New%20Project%20Added.jpg)

In this example, the new Project **:** Server Room has been added to the Solution.


## Add Existing Project- Copy to a Solution

A copy of an existing Project can be added to a Solution.

1. Click on the Solution's hamburger menu and select Add Existing Project - Copy from the drop-down menu:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20Existing%20Project/Add%20Existing%20Project%20Copy.jpg)

Alternatively, from the menu bar select File > Add > Existing Project Copy...



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20Existing%20Project/Add%20Existing%20Project%20Copy%20from%20menu.jpg)

2. In the Select a file window, navigate to the applicable Project file, select it and then click the Open button:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20Existing%20Project/Select%20a%20file%20-%20Existing.jpg)



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20Existing%20Project/Project%20added%20to%20Solution.jpg)

In this example, the existing Project **:** Software Lab was added to the Solution **:** EngineeringasaCopy **.**

**Notes:**


   - The Project is **copied**—not moved—into a new folder under the Solution with the current active focus.

   - The source Project remains unchanged and resides in its original file location.

   - There is no dynamic link or backward inheritance to the source Project. Changes made to the copied Project in this Solution remain only in this Solution.


### Show on Disk

1. In the Solution Explorer, right-click on a Project and select Show on Disk from the right-click menu to display the Project's file location:



      ![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20Existing%20Project/Show%20on%20Disk.jpg)



      ![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20Existing%20Project/Show%20on%20Disk%20File%20Location.jpg)

      In this example, the Software Lab Project is located under the Engineering Solution folder because the Project was added

      to the Engineering Solution via Add Existing Project - Copy (see above).

## Add Existing Project - Reference to a Solution

A Reference to an existing Project—analogous to a hyperlink—can be embedded in a Solution.

1. Click on the Solution's hamburger menu and select Add Existing Project - Reference from the drop-down menu:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20Existing%20Project/Add%20Existing%20Project%20Reference.jpg)

Alternatively, from the menu bar select File > Add > Existing Project Reference...



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20Existing%20Project/Add%20Existing%20Project%20Reference%20from%20menu.jpg)

2. In the Select a file window, navigate to the applicable Project file, select it and then click the Open button:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20Existing%20Project/Select%20a%20file%20-%20Reference.jpg)

![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20Existing%20Project/Project%20added%20to%20Solution%20as%20a%20Reference.jpg)

3. In this example, the existing Project **:** Hardware Lab was added to the Solution **:** EngineeringasaReference **.**

**Notes:**
   - The existing Project is neither copied nor moved. A Reference to the existing Project is embedded in the Solution. Again, this is analogous to a hyperlink.

   - Changes made to the referenced Project in this Solution are made to the source Project in its existing original file location.

   - When Show on Disk is invoked the referenced Project is shown in original location—not under the Solution with the active focus:



     ![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20Existing%20Project/Show%20on%20Disk%20Reference.jpg)

     In this example, the Hardware Lab Project is still located in its original file location because the Project was added

     to the Engineering Solution via Add Existing Project - Reference (see above).

## Build the Solution's Projects

1. From the menu bar, click onBuild > Build the Solution (F12)-or- click the Build smart icon from the UI Editor Toolbar to build the current Solution:



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

       Similarly on the Project Page - Main Menu, the Button\_2 Component falls out of bounds of the Project Page.

      This can be seen and subsequently corrected on the Project Pages themselves by repositioning the Components within the Project Page bounds:



      ![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Out%20of%20Bounds%20Example%20&%20Fix%201.jpg)

      In this example, the custom Environment Widget Component has been repositioned back within the Project Page bounds.



      ![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Out%20of%20Bounds%20Example%20&%20Fix%202.jpg)

      And in this example, the Button\_2 Component has been repositioned back within the Project Page bounds.


3. Click the Output tab to return to the default Build Output window view.

4. In the BuildOutput window, take note of each Project's output file location:



![](https://help.crestron.com/construct/Content/Resources/Images/Build%20Output%20window%20file%20location_v4.jpg)

5. Click the X in the Build Output's window's upper right-hand corner to close the Build Output window:



![](https://help.crestron.com/construct/Content/Resources/Images/X%20to%20close.jpg)

6. If any Errors are encountered during the Build, close the Build Output window--and select Clean the Solution and then select Rebuild the Solution.

7. From the Build drop-down menu, select Clean the Solution:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Clean%20the%20Solution.jpg)

Cleaning the Solution, removes the ch5z file(s) and all Project working files.

8. After the Solution is cleaned, from the Build drop-down menu, select Rebuild the Solution (Shift+F12):



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Rebuild%20the%20Solution.jpg)


## Send the Solution's Projects

1. Launch Crestron Toolbox.

2. From the menu bar, select Tools > EasyConfig-or-on the menu bar, click on the EasyConfig smart icon:



![](https://help.crestron.com/construct/Content/Resources/Images/EasyConfig%20Tool.jpg)

![](https://help.crestron.com/construct/Content/Resources/Images/EasyConfig%20Icon.jpg)

3. Click on the Pencil smart icon in the EasyConfig window's lower left-hand corner:



![](https://help.crestron.com/construct/Content/Resources/Images/Pencil%20icon.jpg)

4. In the Edit Address window. enter the target device's Address (IP address), Username and Password and then click the OK button:



![](https://help.crestron.com/construct/Content/Resources/Images/Edit%20Address.jpg)

5. In the populated EasyConfig window, click on the Display Project button:



![](https://help.crestron.com/construct/Content/Resources/Images/Display%20Project_v2.jpg)

6. In the Open window, select CH5 Projects (\*.ch5z) from the project type drop-down and navigate to the applicable Project in the Solution:



![](https://help.crestron.com/construct/Content/Resources/Images/Open%20Solution%20Toolbox.jpg)

7. In the Project window, click the Send button:



![](https://help.crestron.com/construct/Content/Resources/Images/Project%20Send.jpg)

**Note:**



A touch screen can run only one Project. In a multi-project Solution, each Project must be sent to a separate touch screen or device to run that specific Project.



    For example, the Living Room Project might be sent to a hand-held touch screen remote \[control\]. Whereas, the Kitchen Project might be sent to table top or wall mounted touch screen.



![](https://help.crestron.com/construct/Content/Resources/Images/File%20Transfer.jpg)

The File Transfer... progress is displayed in the center of the Project window (see above).

8. Upon successful completion, the Project is listed in the Project window's Loaded Project Information scroll box:



![](https://help.crestron.com/construct/Content/Resources/Images/Loaded%20Project%20Information.jpg)

Click the Close button to return to the EasyConfig window.



In the EasyConfig window, the ProjectName and Timestamp of the Project is displayed to the right of the DisplayProject button:



![](https://help.crestron.com/construct/Content/Resources/Images/Living_Room%20on%20Display%20Project%20pane.jpg)