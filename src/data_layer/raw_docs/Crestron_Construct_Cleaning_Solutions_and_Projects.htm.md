

# Cleaning Solutions & Projects

If any errors are encountered when a Solution or Project is built, clean the applicable Solution or Project.

There are several options to Clean Solutions and to Clean Projects available from the Build menu, the Solution-level hamburger menu and the Project-level right-click menu.

Exactly what each Cleaning option cleans and what it does not clean is outlined below. See [Cleaning Solution](https://help.crestron.com/construct/Content/Topics/UI%20Editor/GA%201.35/Clean%20Project/Cleaning%20Solutions%20and%20Projects.htm#Cleaning_Solutions) or [Cleaning Projects](https://help.crestron.com/construct/Content/Topics/UI%20Editor/GA%201.35/Clean%20Project/Cleaning%20Solutions%20and%20Projects.htm#Cleaning_Projects).

Read the Preliminary Notes directly below before Cleaning a Solution or Project.

## Preliminary Notes

### NEW Location for the _temporary_ folder (Working)

As of Crestron Construct v1.36.x and later, the _temporary_ folder has been moved outside the Solutions folder and is now named Working.

The default locations for each operating system are as follows:

- **Windows:** C:\\Users\\USER\\AppData\\Roaming\\crestron-construct\\AppStorage\\working\\uieditor

- **MacOs**: /Users/USER/Library/Application Support/crestron-construct/AppStorage/working/uieditor


Folders inside the new Working directory will be created for each Project and tagged with a unique GUID to prevent project name collision; for example: **\\Working**\\uieditor\demo\_project\_1 (d5b33037-855c-4ae2-bc3d-4596de6498e8).

### Old Location for the _temporary_ folder (\_TEMP)

Previously, the _temporary_ folder was located in the Solutions folder and was named \_TEMP.

For example, Documents\\Crestron\\Crestron Construct\ **Solutions**\\demo\_project\_1\\demo\_project\_1 **\\\_\_TEMP**

Additionally, for older Projects with a \_\_TEMP folder in the Solutions folder, performing a Clean or Clean Everything operation will remove the old \_\_TEMP directory, and the new location will be used for the Working directory/folder.

## Cleaning Solutions

### Build menu  ![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Cleaning%20Projects/Build%20Menu%20clean%20solution.jpg)

- **Clean the Solution:** Cleans **only** the Working folder. It does **not** remove anything from the Output folder of each Project.

- **Clean the Solution - All:** Cleans everything — **both** the Working folder **and** the Output folder in **all** Projects.


## Cleaning Projects

### Build menu  ![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Cleaning%20Projects/Build%20Menu%20clean%20project.jpg)

- **Clean Current Project**: Cleans **only** the Working folder. It does not remove anything from the Output folder of the Project.

- **Clean Current Project - All:** Cleans everything — **both** the Working folder **and** the Output folder in the Project.


### Solution-level right-click menu  ![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Cleaning%20Projects/Solution%20level%20clean%20project.jpg)

- **Clean All Projects:** Cleans **only** the Working folder. It does **not** remove anything from the Output folder of each Project.

- **Clean All Projects - All:** Cleans everything — **both** the Working folder **and** the Output folder in **all** Projects.


### Project-level right-click menu  ![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Cleaning%20Projects/Clean%20Project%20Project%20level.jpg)

- **Clean Project:** Cleans **only** the Working folder. It does **not** remove anything from the Output folder of the Project.

- **Clean Project - All**: Cleans both Working folder as well as the Output folder in the Project.