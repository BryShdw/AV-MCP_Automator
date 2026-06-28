

# Default Font Family

A Default Font Family can be set on a per project basis. The default font will be applied to new Components when they are dragged and dropped onto a Project Page/Widget.

At Project creation, the Default Font Family is set to Roboto.

## Setting the Default Font Family

1. In Solution Explorer, right-click on the Project and select Project Properties from the menu:



![](https://help.crestron.com/construct/Content/Resources/Images/Default%20Font%20Family/Menu.jpg)

2. Click on the Default Font Family drop-down arrow; select a Default Font Family from the drop list and then click Save Changes:



![](https://help.crestron.com/construct/Content/Resources/Images/Default%20Font%20Family/Font%20Drop%20Down.jpg)


The Default Font Family is applied to only new Components dragged and dropped onto a Project Page or Widget. Pre-existing Components and Widgets will retain their original font designation.

**Note:**

If a project is opened that has a project-level default font value for a font that is not installed, a toast message will be generated:

“The project-level default font _font name_ is not installed. Please add it to the Crestron Construct Fonts directory.”

In this instance:

- The default font value will then be set to Roboto.

- The Project will become _dirty_, which allows a user to either save the new type as Roboto or close the Project and fix the issue without losing the original default value.


Furthermore, if the Project-level default font isn’t installed and that font is used in any Pages or Widgets, the Project will be disabled (this is current behavior where if the font used in any Page or Widget is not installed, Project is disabled).