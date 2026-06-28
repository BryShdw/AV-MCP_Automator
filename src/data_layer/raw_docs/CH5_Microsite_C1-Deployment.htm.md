

# Deploy the Project

The ch5-cli deploy utility can be used deploy .ch5z archive files to a control system. The -t/--deviceType parameters of ‘mobile’ and ‘controlsystem’ will deploy to a control system to make that project available to the Crestron ONE app. For more information, refer to [Create and Deploy CH5 Archives](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/UI-CH5-Archives.htm).

NOTE: For Crestron Virtual Control (VC-4) installations, the .ch5z archive utility is loaded directly to the control system along with the SIMPL program using the **XPanel (Web)** option. For more information, refer to the [Crestron Virtual Control Product Manual](https://docs.crestron.com/en-us/8912/Content/Topics/Home.htm "https://docs.crestron.com/en-us/8912/Content/Topics/Home.htm").

To deploy a Crestron Template Project for the Crestron ONE app to a control system:

1. Within the **package.json** file, copy the following command line into the “scripts” object, which must be updated to include the host name or IP address of your control system.

Copy

```
build:deploymobile": "ch5-cli deploy -H [ip address]-p -t mobile dist/prod/shell-template.ch5z
```

5. Update the existing build:onestep command in the “scripts” object to reference the build:deploymobile script, or create a copy of build:onestep named build:onestepmobile.
6. Issue the npm run build:onestep or build:onestepmobile command in the terminal, or select the run one-click NPM script. This command will compile, archive, and deploy the project to the control system.
7. Enter the administrator username and password for your control system when prompted. Refer to [Create and Deploy CH5 Archives](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/UI-CH5-Archives.htm) for alternative methods to enter control system credentials on each deployment.

The archive can also be deployed via Crestron Toolbox software using the **Web Pages and Mobility Projects** function as shown in the image below. Select the **shell-template.ch5z** file, which is located in the **/project/dist/prod** folder.

![](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Resources/Images/Web-Mobility.png)