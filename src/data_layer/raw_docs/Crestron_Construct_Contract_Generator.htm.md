

# Contract Generator

The Contract Generator generates Contract Joins in the namespace of a Control Join ID when the Solution is built. These can be assigned to Pages, Widgets, Components or complex Components such as the DPad and the Keypad. Therefore, join availability is never an issue.

## Using the Contract Generator

1. Select the Page, Widget, Component or complex Component as applicable.

2. Click on the **C** smart icon to the right of an input or output join in the Properties Grid's Receive Feedback or Send Command sections as applicable:

![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Contract%20Generator/Contract%20Generator%20Example.jpg)

In this example,a Button Component was selected. Its Receive Digital Feedback Visibility, Enable and Selected input joins and its Send Digital Command Visibility and Press output joins were assigned Contract Joins using the Contract Generator.



Contract Joins can also be assigned when a Page is selected in the Solution Explorer for editing:



![](https://help.crestron.com/construct/Content/Resources/Images/Create%20A%20Solution/Add%20New%20Page/Contract%20Generator%20-%20Page%20Visibility%20Join.jpg)

In this example, the Page's Page Visibility Join has been Contract Enabled.





The actualContract Joins, themselves, are generated  in the namespace of a Control Join ID when the Solution is built.

The Crestron Construct compiler creates a CH5 GUI Extender Definition (.chd) file called <ProjectName.chd _>_ _._

This file will bring in all Contract Joins. The Ch5 (HTML rendered on the panels) will use the contract.cse2j file found in <Solutions Folder>/<Solution>/<Project>/output/contract/mapping.

Every time the Solution is built/compiled, these files are updated.



The resulting output files are compatible with SIMPL Windows and SIMPL#.

The output files include the following:


   - **SIMPL:** <SolutionFolder>\\<SolutionName>\\<ProjectName>\\output\\contract\\programming\\SIMPL\ ProjectName.chd

   - **SIMPL#** : <SolutionFolder>\\<SolutionName>\\<ProjectName>\\output\\contract\\programming\\SIMPLSharp\\ContractSupport\<\*.g.cs>"" The SIMPL# output files include all files in the referenced file location with the <.g.cs>  file extension.

     **Note:** For Apple computers the file location is designated with forward slashes: “/”. Whereas, Windows-based computers can use the conventional back slash “\ “or the forward slash “ /”.


## Special Cases

   - The Button List, Tab Buttons, Widget Lists, and Video Switcher Components are Contract only.

   - Dynamic Text set via the Label Text Editor are join-based only and currently have no Contract option.

   - The Page Visibility Join is accessible by editing the Page.

   - Digital, Analog and Serial Offsets are not applicable for Contract Joins.

   - ComplexComponents—such as the DPad and the Keypad—are all or nothing. They use either onlyJoinNumbers or **only** ContractJoins — but **not** a combination of both.

   - Widgets can be Global or Non-global.
     - Global means that the Widget only needs to be programmed once. Global Widgets are best used for something that needs to appear on multiple pages--such as a Page header or footer

     - Non **-** global means that each reference needs to be programmed.