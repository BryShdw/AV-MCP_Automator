

# Hard Button Manager

The Hard Button Manager sets Digital Joins and Reserved Joins at the Project-level and at the Resolution- or Touch Screen-level for Hard Buttons and Page Flips.

A Page Flip file switches the display screen from one page to another when a button is pressed or clicked.

Hard Button configuration settings are not inherited from one Project to another Project in a Solution with multiple Projects.

Hard Buttons do not support Contract Joins.

## Setting Hard Buttons

1. In the Solution Explorer, select the applicable Project and expand the Hard Buttons sub-folder:



![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Hard%20Button%20Manager/Hard%20Button%20Folder.jpg)

2. Select either Project Level, the applicable Resolution Level or Page Level.

3. On the Project Level, select the applicable Hard Button from the Project Level Controls pane:



![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Hard%20Button%20Manager/Project%20Level%20Hard%20Button%20selection.jpg)

In this example, Project Level Hard Buttons are being set. The Home Hard Button has been selected.

**Notes**



Project Level Hard Buttons apply across all Device Resolutions in the Project. Device Resolution Level and Page Level Hard Buttons can also be set.







Page Level Hard Buttons at the Project Level will override the Project Level Hard Buttons **when navigated to that page on a panel**...and Pages at the Device Resolution Level will override everything **when on that page**.

4. Click on JoinSelector smart icon number sign **#** or the ReservedJoins smart icon **R** to set either a Join Number or Reserved Join respectively:



![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Hard%20Button%20Manager/Hard%20Button%20join%20number%20set.jpg)

In this example, the Home Hard Button was assigned the Join Number **1** using the Join Selector smart icon number sign **\#** and was assigned a Page Flip to the Page: Top Menu.



![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Hard%20Button%20Manager/Hard%20Buttons%20Reserved%20Joins%20selected.jpg)



In this example, the Home Hard Button was assigned the Reserved Join: Hard\_Button\_2\_On by using the ReservedJoins smart icon **R** and then selecting the Reserved Join from the Reserved Joins scroll box:



![](https://help.crestron.com/construct/Content/Resources/Images/Hard%20Button%20Reserved%20Join%20Scroll%20Box.jpg)

**Note:** Only Send Event (output joins) Reserved Joins are supported for Hard Buttons at the Project, Device and Page levels.

5. Click on the Page Flip drop-down to select and assign a Page Flip to the Hard Button:



![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Hard%20Button%20Manager/Hard%20Button%20Select%20Page%20Flip.jpg)

![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Hard%20Button%20Manager/Page%20Flip%20selected.jpg)

In this example, the Page: Top Menu was selected as the Page Flip for when the Home Hard Button is pressed.

6. On the Device Resolution Level , select the applicable Device Resolution in the Solution Explorer from its corresponding Project:



![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Hard%20Button%20Manager/Hard%20Buttons%20Touch%20Screen.jpg)

In this example, the TSW-1070 was selected and its Hard Buttons will be configured.


1. Click on JoinSelector smart icon number sign **#** or the ReservedJoins smart icon **R** to set either a Join Number or Reserved Join respectively:



![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Hard%20Button%20Manager/Hard%20Button%20Touch%20Screen%20Configure.jpg)

In this example, the TSW-1070's Home, Up, and Down Hard Buttons have Join Numbers and Reserved Joins added. The Home Hard Button was also assigned a Page Flip to the Page: Top Menu.


1. On the Page Level , select the applicable Project Page:



![](https://help.crestron.com/construct/Content/Resources/Images/Project%20&%20Pages/Hard%20Button%20Manager/Page%20Level%20Hard%20Buttons.jpg)

In this example, the Top Menu Page's Mic Hard Button was configured with a Join Number and Page Flip.