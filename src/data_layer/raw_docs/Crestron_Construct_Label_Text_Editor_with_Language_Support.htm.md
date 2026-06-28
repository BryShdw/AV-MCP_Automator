

# Label Text Editor

The LabelTextEditor configures advanced Label text properties and functionality for Button and Formatted Text Components. The Label Text Editor can set join numbers and conditions that dynamically control the Label text that is displayed at runtime.

## Using Label Mode & The Label Text Editor

1. In the Properties Grid's Interactions section, click on the Label Mode drop-down and select advanced:







![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Label%20Text%20Editor/Label%20Text%20Editor.jpg)

2. In the Label property click on the ellipses button to open the Label Text Editor:







![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Label%20Text%20Editor/Label%20Mode%20ellispics.jpg)

3. Type the Label text on the Canvas and style the text using the Label Text Editor toolbox's Font, Size and Color drop-down and smart icons:







![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Label%20Text%20Editor/Label%20Text%20Editor%20Window.jpg)


1. Webfonts typically do **not** support in-line styling: bold, italics or underline. See [Webfonts](https://help.crestron.com/construct/Content/Topics/UI%20Editor/Webfonts.htm)

2. Therefore, select the applicable webfont whose name includes the desired font style. The font style designation appears at the end of the webfont name. For example, CascadiaCode-Italic.

3. Use the Size and Color drop-down to size and color the Label text.

**NOTE:** The default font: Roboto and Crestron-based such as Crestron General and Crestron Icon fonts (for example: Crestron Lighting-HVAC) do support in-line styling: bold, italics or underline:





![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Label%20Text%20Editor/Crestron%20Font.jpg)


#### ANALOG, SERIAL, DIGITAL & HTML

1. Click on the ANALOG, SERIAL or DIGITAL buttons to set join numbers and conditions that dynamically control the Label text that is displayed at runtime:







![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Label%20Text%20Editor/LTE-%20Join%20Buttons.jpg)

2. Click the ANALOG button to set an analog join number; use the Format Type drop-drop to set the corresponding Format Type:







![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Label%20Text%20Editor/LTE%20-%20Analog%20Join.jpg)


|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| Format Type | Description | Example | HTML | **Value** | Formatted<br>Text |
| Floating point | Displays the analog join value as a floating point number, adding trailing and leading zeros if necessary. | <A$91?%3.5f> | <p><ch5-jointotext-numeric receiveStateValue="1" decimalLength="5" length="3" type="float"></ch5-jointotext-numeric></p> | 23415 | 000.23415 |
| Signed Integer | Displays the analog join value as a signed integer, adding leading zeros to the number if necessary. | <A$91?%5d> | <p><ch5-jointotext-numeric receiveStateValue="1" length="5" type="signed"></ch5-jointotext-numeric><ch5-jointotext-numeric receiveStateValue="1" decimalLength="3" length="5" type="float"></ch5-jointotext-numeric></p> | 9999 | 0009999 |
| Unsigned Integer | Displays the analog join value as an unsigned integer, adding leading zeros to the number if necessary. | <A$91?%7u> | <p><ch5-jointotext-numeric receiveStateValue="1" length="7" type="unsigned"></ch5-jointotext-numeric><ch5-jointotext-numeric receiveStateValue="1" length="5" type="signed"></ch5-jointotext-numeric><ch5-jointotext-numeric receiveStateValue="1" decimalLength="3" length="5" type="float"></ch5-jointotext-numeric></p> | 65535 | 65535 |
| Percentage | Displays the analog join value as a percentage from 0 to 100. | <A$91?%1.1p> | <p><ch5-jointotext-numeric receiveStateValue="1" decimalLength="1" length="1" type="percentage"></ch5-jointotext-numeric><ch5-jointotext-numeric receiveStateValue="1" length="7" type="unsigned"></ch5-jointotext-numeric><ch5-jointotext-numeric receiveStateValue="1" length="5" type="signed"></ch5-jointotext-numeric><ch5-jointotext-numeric receiveStateValue="1" decimalLength="3" length="5" type="float"></ch5-jointotext-numeric></p> | 500 | 50 |
| Raw | Displays the analog join value **as is** without any formatting. | <A$91?%r> | <p><ch5-jointotext-numeric receiveStateValue="1" type="raw"></ch5-jointotext-numeric><ch5-jointotext-numeric receiveStateValue="1" length="7" type="unsigned"></ch5-jointotext-numeric><ch5-jointotext-numeric receiveStateValue="1" length="5" type="signed"></ch5-jointotext-numeric><ch5-jointotext-numeric receiveStateValue="1" decimalLength="5" length="3" type="float"></ch5-jointotext-numeric></p> | 55 | 55 |
| Time | Display the analog join value as time in hours, minutes and seconds (hh:mm:ss). The incoming analog join value is assumed to be in units of seconds. | <A$91?%t> | <p><ch5-jointotext-numeric receiveStateValue="1" type="time"></ch5-jointotext-numeric><ch5-jointotext-numeric receiveStateValue="1" type="raw"></ch5-jointotext-numeric><ch5-jointotext-numeric receiveStateValue="1" length="7" type="unsigned"></ch5-jointotext-numeric><ch5-jointotext-numeric receiveStateValue="1" length="5" type="signed"></ch5-jointotext-numeric><ch5-jointotext-numeric receiveStateValue="1" decimalLength="5" length="3" type="float"></ch5-jointotext-numeric></p> | 3200 | 53:20 |
| Hexadecimal | Convert and displays the analog join value from decimal to a hexadecimal value, adding leading zeros to the number if necessary. | <A$91?%h> | <p></p> | 15 | 0F |
|  |  |  |  |  |  |


1. Click on the SERIAL button to set a serial join number and the default text:







![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Label%20Text%20Editor/LTE%20-%20Serial%20Join%20set.jpg)







![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Label%20Text%20Editor/LTE%20-%20Serial%20Join%20set_example.jpg)



In this example, the Serial Join Number was set to **1** and the Default Text was set to On.



Corresponding HTML: <p><ch5-jointotext-string receiveStateValue="1" textWhenEmpty="On"></ch5-jointotext-string></p>.


1. Click on theDIGITAL button to set a digital join number:





![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Label%20Text%20Editor/Label%20Mode%20Digital%20Join.jpg)







![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Label%20Text%20Editor/Label%20Text%20Editor%20digital%20join%20set.jpg)



In this example, a Digital Join Number was set to 1. If the digital join is True , then the Label text: On will be displayed. If the digital join is False, then the Label text: Off will be displayed.

**Corresponding HTML:** <p><ch5-jointotext-boolean receiveStateValue="1" textWhenTrue="On" textWhenFalse="Off"></ch5-jointotext-boolean></p>.



**Note**: Advanced label settings are lost when the Label Mode is changed from advanced to simple.


#### LANGUAGE

The LANGUAGE button allows users to define CIP tags for both the language key and the text, allowing them to switch languages at runtime.

1. Click on the LANGUAGE button to set the \[Language\] Key and Default Text

2. Enter the Key and the Default Text in the corresponding text fields.





The following rules apply to the Key text field:


   - Key cannot start with a number but can end with a number.

   - Key can contain a period “.” but NOT as the first character or last character.

   - Key can contain “\_” but NOT as the first character or last character.

   - No other special characters are allowed.


![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Label%20Text%20Editor/Language%20Key.jpg)

![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Label%20Text%20Editor/Language%20Key%20LTE%20example.jpg)

In the above example, the CIP View equals <L$MenuTitle?Presentation Sources>, as shown above.

And the CH5 Tags equal <ch5-jointotext-string value="-+MenuTitle+-" textWhenEmpty="Presentation Sources"></ch5-jointotext-string>

**Notes:**

1. Multiple language keys can be added to the same advanced label.



      For example,







      **CIP View:** <L$MenuTitle?Presentation Sources><L$MenuSubTitle?Video>



      **CH5 Tags**: <ch5-jointotext-string value="-+MenuTitle+-" textWhenEmpty="Presentation Sources"></ch5-jointotext-string><ch5-jointotext-string value="-+MenuSubTitle+-" textWhenEmpty="Video"></ch5-jointotext-string>

2. Normal text can also be used along side any language keys.

      For example,

      **CIP View:** <L$MenuTitle?Presentation Sources>Hello World<L$MenuSubTitle?Video>