

# Add a Custom Theme to the Template Project

Custom themes can be added to the Crestron Template Project so that they can be selected alongside the default supplied themes.

To add a custom theme to the Crestron Template Project:

01. Create a custom theme and download it to your local computer using the Theme Builder tool in the Showcase Application. For more information, refer to [Theme Builder](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Theme-Builder.htm).
02. Extract the downloaded ZIP file.
03. Create a new folder named "custom-themes" at the **\\shell-template\\app\\project\\assets\\scss\** path in the Crestron Template Project.
04. Move the extracted project CSS file to the **custom-themes** folder at the path specified above.
05. Create a custom theme object in the project configuration themes array located within **app\\project-config.json**.

NOTE: The theme object name must match the name of the project CSS file exactly.

Refer to the following example:

Copy

```
"themes":[\
    {\
        "name": "ThemeOne-theme",\
        "brandLogo": {\
            "url": "./app/template/assets/img/ch5-logo-light.svg",\
            "alt": "Crestron Logo"\
            "receiveStateUrl": ""\
    }\
]
```

Once the theme has been added using the procedure above, it can be selected during project runtime as described in [Select a Theme](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/CH5-Components/Select-Theme.htm).