

# Theme Editor

Crestron Construct v1.4001 running CH5 v2.14 or later support custom theme creation via the Theme Editor.

The Theme Editor is a separate, on-line only tool located on the CH5 Showcase website.

It can be launched from the Construct Tools Menu: Tools > Open Theme Editor:

![](https://help.crestron.com/construct/Content/Resources/Images/Theme%20Editor/Open%20Theme%20Editor.jpg)

**-OR-** from the CH5 Showcase website: [https://sdkcon78221.crestron.com/downloads/ShowcaseApp/index.html](https://sdkcon78221.crestron.com/downloads/ShowcaseApp/index.html) by clicking on the palette icon:

![](https://help.crestron.com/construct/Content/Resources/Images/Theme%20Editor/palette%20icon.jpg)

![](https://help.crestron.com/construct/Content/Resources/Images/Theme%20Editor/Showcase.jpg)

Press the push pin icon to vertically tile the Theme Editor with the CH5 Showcase:

![](https://help.crestron.com/construct/Content/Resources/Images/Theme%20Editor/Push%20Pin.jpg)

![](https://help.crestron.com/construct/Content/Resources/Images/Theme%20Editor/Theme%20Editor.jpg)

![](https://help.crestron.com/construct/Content/Resources/Images/Theme%20Editor/Theme%20Editor%20Tiled.jpg)

## To Create a Custom Theme

1. Enter the theme name in the Theme Name text field and click the CREATE THEME button:



![](https://help.crestron.com/construct/Content/Resources/Images/Theme%20Editor/Create%20theme%20Name.jpg)

![](https://help.crestron.com/construct/Content/Resources/Images/Theme%20Editor/Create%20Theme.jpg)

**Recommendation:** Select an existing CH5 theme to use as a template (or starting point) and then give the custom Theme an unique name.

2. Use the assorted fields, drop-downs and filters to configure the Theme's Colors, Numbers, Lists and Units as applicable.



Click on the top-centered Colors, Numbers, List or Units buttons to configure the corresponding theme attributes:



![](https://help.crestron.com/construct/Content/Resources/Images/Theme%20Editor/Center%20buttons.jpg)





![](https://help.crestron.com/construct/Content/Resources/Images/Theme%20Editor/MyCustomTheme.jpg)

3. Click the + CREATE NEW THEME button when finished:



![](https://help.crestron.com/construct/Content/Resources/Images/Theme%20Editor/Create%20New%20Theme%20button.jpg)



The Theme data is stored within the browser cache and can be edited at any time. The editor limits the number of cached Themes to three. If three Themes have already been cached, a new custom theme cannot be created until one is removed.



To remove a Theme, click the DELETE THEME button:



![](https://help.crestron.com/construct/Content/Resources/Images/Theme%20Editor/DELETE%20THEM%20button.jpg)



To export a Theme, click the DOWNLOAD THEME button:

![](https://help.crestron.com/construct/Content/Resources/Images/Theme%20Editor/Download%20Theme.jpg)



To upload a Theme, click the UPLOAD THEME button:

![](https://help.crestron.com/construct/Content/Resources/Images/Theme%20Editor/UPLOAD%20THEME%20button.jpg)


## Themes & Buttons

The Theme Editor dialog exposes all the supported CH5 CSS variables. The top colors section allows colors to be applied globally to all components and their styles:

![](https://help.crestron.com/construct/Content/Resources/Images/Theme%20Editor/colors.jpg)

Button components support three states: Normal, Pressed and Selected. When a CSS variable does not contain a state name, it is implied to be used with the “normal” state of a button.

In addition to states, button components support styles: Default, Primary, Info, Text, Danger, Warning, Success and Secondary.

- When a button’s Theme Mode is set to “custom”, the only style that is used is the “default” style.

- When a button’s Theme Mode is set to “theme” all styles are exposed and supported but none of the style values can be overridden.


Leaving a component’s Theme Mode set to “custom” allows the component to inherit the theme styling but still allow the values to be overridden.

For example:

**“--theme-colors--danger-background-color” value** will be used when the button’s style is “danger” and it is on the “normal” state.

**“--theme-colors--danger-pressed-background-color” value** will be used when the button’s style is “danger” and it is on the “pressed” state.

To style individual components using the Theme Editor, use the left-side menu to select a component. The Theme Editor will automatically open the corresponding CSS variable section for the selected component.

**Hint:** To preview button styles, click the “type” in the “Attributes” section after selecting “CH5 Button” from the menu.

Values entered in the custom theme are applied immediately to the components in the CH5 Showcase.

Once all of the custom properties have been applied to the custom theme, export the file. This will create an archive file (.zip) on the computer hard disk.

There are limitations with themes created using the theme editor when they are intended to be used with a Crestron Construct project:

- Not all CSS variable units in the theme editor are supported in Crestron Construct. As a result, using a non-default unit may result in inconsistent or unexpected behavior when using the theme in Crestron Construct.

- The Theme Editor provides limited validation of user-entered values. As a result, the value may cause unexpected results when using the Theme in Crestron Construct.


**Note:**  Custom Themes in SmartGraphics Projects cannot be imported.