

# Import or Export a Contract

The import function allows the contents of an archived contract to be extracted to a specific location on the workstation. The export function allows a contract to be packaged as an archive for easy transmission and storage.

## Import a Contract

To import a contract archive (.ccz file):

1. From the home screen,select **Import Archived Contract** under the **Start** section, or select the **Import Archive Contract** button on the top menu. A pop‑up dialog box is displayed.

![](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Resources/Images/CE6.png)

3. Select the icon to the right of **Archive location** to select the archived .ccz file from the workstation file system.
4. Select the icon to the right of **Archive destination** to select an extraction location on the workstation.
5. Select **Import**.

If the import is successful, the following files will be extracted to the archive destination:

- A Contract Editor (.cce) file that can be opened in Contract Editor.
- An output folder with the following subfolders:
  - A **ch5ContainerApp** folder with a .cse2j file for use with CH5 projects.
  - A **SIMPL** folder with a .chd file for use with SIMPL projects.
  - An **SS** folder with multiple .g.cs files for use with SIMPL# PRO projects.

## Export a Contract

To export a contract as an archive (.ccz) file:

1. Select the **Archived Contract** button on the top menu. A pop-up dialog box is displayed showing the workstation file system.
2. Navigate to a location on the workstation where the archived contract should be saved.
3. Select **Select Folder**. An archive file of the contract is placed in the selected folder.