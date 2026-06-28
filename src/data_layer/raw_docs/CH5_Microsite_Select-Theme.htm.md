

# Select a Theme

Themes can be changed during project runtime by selecting the droplet icon in the header bar (or elsewhere in the project if configured this way) to display the **Select Themes** dialog box.

![Droplet Icon in Header Bar](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Resources/Images/2-8-Header-Icons-Droplet.png)

![Select Theme Dialog Box](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Resources/Images/2-8-Theme.png)

Additionally, the project theme can be set using control system joins via the **project-config.json** file. Refer to the following sample code:

Copy

```
  "customSignals": {
    "receiveStateTheme": "templateTheme",
    "sendEventTheme": "templateTheme"
  },
```