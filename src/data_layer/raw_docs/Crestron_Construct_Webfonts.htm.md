

# Webfonts

Crestron Construct supports the following third-party webfonts:

- \*.ttf

- \*.eot

- \*.woff

- \*.woff2

- \*.svg


Webfonts must be manually copied into the following directory:

C:\\Users\\USER\\Documents\\Crestron\\Crestron Construct\\Webfonts

Note: Anytime webfonts are installed or modified Construct must be restarted.

Installed webfonts can be selected from the Font Family drop-down under the Component's Interactions - Label section in the Property Grid:

![](https://help.crestron.com/construct/Content/Resources/Images/Webfonts/Font%20Family%20drop-down.jpg)

## Label Mode -Advanced

1. If Label Mode has been set to advanced, then click on the ellipsis to the right of the Label to enter the Label Text Editor:



![](https://help.crestron.com/construct/Content/Resources/Images/Webfonts/Interactions%20Label.jpg)

2. In the Label Text Editor type and then select the Label text:

3. From Font drop-down select the webfont:



![](https://help.crestron.com/construct/Content/Resources/Images/Webfonts/LTE%20-%20Font%20drop-down.jpg)

4. Webfonts typically do **not** support in-line styling: bold, italics or underline.

5. Therefore, select the applicable webfont whose name includes the desired font style. The font style designation appears at the end of the webfont name. For example, CascadiaCode-Italic.

6. Use the Size and Color drop-down to size and color the Label text:



![](https://help.crestron.com/construct/Content/Resources/Images/Webfonts/Size%20and%20Color.jpg)

7. Click the Save button to apply the Label text and styling and exit the Label Text Editor:



![](https://help.crestron.com/construct/Content/Resources/Images/Webfonts/Label%20Example.jpg)


NOTE: The default font: Roboto and Crestron-based such as Crestron General and Crestron Icon fonts (for example: Crestron Lighting-HVAC) do support in-line styling: bold, italics or underline:

## Webfont Runtime File Location

When the Project is built, its webfonts are stored for the runtime environment in the following file location:

C:\\...\\working\\app\\project\\assets\\fonts

## Importing Projects with Webfonts

When an exported Crestron Construct Project is imported, its webfonts are copied to the following file location:

C:\\Users\\USER\\Documents\\Crestron\\Crestron Construct\\Webfonts

These imported fonts are then available for use in any new or existing Projects.

If the archive contains any fonts that already exist in the fonts directory (see above), they will be ignored and not imported--and the following message will be displayed:

The following fonts in the archive already exist in the font directory and were not imported: Font1, Font2