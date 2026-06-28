

# PROJECT INFORMATION Dialog

The PROJECT INFORMATION  Dialog's Version, WebXPanel and Diagnostics tabs display the corresponding project-related information by their respective category:

![](https://help.crestron.com/construct/Content/Topics/UI%20Editor/GA%201.35/Project%20Information/Project%20Information%20Version.jpg)

![](https://help.crestron.com/construct/Content/Topics/UI%20Editor/GA%201.35/Project%20Information/WebXPanel.jpg)

![](https://help.crestron.com/construct/Content/Topics/UI%20Editor/GA%201.35/Project%20Information/Diagnostics.jpg)

The related information is useful for Project documentation, troubleshooting and diagnostic purposes.

## Enabling the PROJECT INFORMATION Dialog

**ONLY** the Button, Image, Toggle Button and Color Chip Components support displaying the PROJECT INFORMATION Dialog at runtime.

1. Place a Button or Image Component on the Project Page and assign it a digital Press via a Reserved Join as seen in the PROPERTIES Grid's Send Digital Command section:



![](https://help.crestron.com/construct/Content/Topics/UI%20Editor/GA%201.35/Project%20Information/Digital%20Press.jpg)

2. Assign Press the Reserved Join: infoBtn.clicked (112233)

3. Click on the Reserved Join icon **R:**



![](https://help.crestron.com/construct/Content/Topics/UI%20Editor/GA%201.35/Project%20Information/Press.jpg)

4. Select infoBtn.clicked (112233) in the drop-down:



![](https://help.crestron.com/construct/Content/Topics/UI%20Editor/GA%201.35/Project%20Information/Resrved%20Joins%20Drop%20Down.jpg)

![](https://help.crestron.com/construct/Content/Topics/UI%20Editor/GA%201.35/Project%20Information/Join%20Assigned.jpg)

5. Save and Build the Project.

6. After the Project has been built, click on the Component that was assigned the infoBtn.clicked (112233) Reserved Join to display the Project's PROJECT INFORMATION Dialog:



![](https://help.crestron.com/construct/Content/Topics/UI%20Editor/GA%201.35/Project%20Information/Project%20Information%20Version.jpg)