

# Viewport

A **viewport** is the visible area of a web page on a touchscreen or other device, measured in CSS pixels, that displays content. This visible area excludes user interface elements such as menus and scrollbars.

A viewport is typically smaller the touchscreen's or other device's native resolution. The result, the web page or UI has a consistent display/appearance across screens with different resolutions.

The following Crestron Touchscreens have the same viewport size:

- TSW-770

- TSW-1070

- TST-1080


Therefore, a project created for one of these touchscreens will work natively on any of the others without any modifications.

## Creating a Custom Viewport Size

1. Use the sample project included in the Construct installation called **resolutionheightwidth.ch5z** to calculate the viewport size. The sample project works with the [CRESTRON ONE](https://help.crestron.com/construct/Content/Topics/UI%20Editor/Browsers%20&%20XPanel.htm#CRESTRON_ONE) application.





resolutionheightwidth.ch5z can be found at these file locations:
   - Windows = C:\\Users\\Public\\Documents\\Crestron\\Crestron Construct\\SampleProjects

   - macOS = /Users/\[username\]/Documents/Crestron/Crestron Construct/SampleProjects
2. In the Solution Explorer, right-click on the Project and select Resolution Settings from the menu:



![](https://help.crestron.com/construct/Content/Resources/Images/Viewport/Resolution%20Settings.jpg)

3. In Edit Device Resolution window under Add Custom Resolution, add the resolution that corresponds to the desired custom viewport size:



![](https://help.crestron.com/construct/Content/Resources/Images/Viewport/Add%20Resolution.jpg)

4. Click the ADD button.



The custom resolution with the custom viewport size will appear in the pick list:



![](https://help.crestron.com/construct/Content/Resources/Images/Viewport/Custom%20viewport.jpg)