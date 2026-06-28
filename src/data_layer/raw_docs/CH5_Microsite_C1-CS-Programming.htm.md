

# Control System Programming

Similar to what exists for physical touch screens, a distinct SIMPL symbol and SIMPL# Pro class have been created for the Crestron ONE app that includes special device extenders to gather and set information for the app.

To facilitate multiple distinct Crestron HTML5 User Interface projects communicating to the same control system from the same mobile application, the control system program must include the name of the project associated with the program IP ID.

A special subslot exists where the control system programmer must provide the project name. The project name should match exactly one of the projects loaded to the control system as described in [Deploy the Project](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Platforms/C1-Deployment.htm).

## SIMPL Symbol

The following images show the Crestron ONE app symbol as it appears in SIMPL. For more information, refer to the [SIMPL help file](https://help.crestron.com/simpl/#Device_Library/Touchpanels/Crestron%20One/Project%20Name.htm).

![](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Resources/Images/SIMPL-1.png)

![](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Resources/Images/SIMPL-2.png)

## SIMPL\# Pro Class

The following code sample shows the SIMPL# Pro class for the Crestron ONE app. For more information, refer to the SIMPL# Pro help file.

NOTE: The output file can be renamed by modifying the -p parameter in the build:archive script. The value of cone.ParameterProjectName.Value must match the project name exactly. For more information, refer to [Create and Deploy CH5 Archives](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/UI-CH5-Archives.htm).

Copy

```
using Crestron.SimplSharpPro.UI;

namespace CrestronOneProgram
{
    public class ControlSystem : CrestronControlSystem
    {
        private static CrestronOne cone;

        public override void InitializeSystem()
        {
            try
            {
                CreateCrestronOneApp(0x03);
            }
            catch (Exception e)
            {
                ErrorLog.Error("Error in InitializeSystem: {0}", e.Message);
            }
        }

        private void CreateCrestronOneApp(uint ipId)
        {
            cone = new CrestronOne(ipId, this);
            // This must match project name on control system exactly
            cone.ParameterProjectName.Value = "shell-template";

            cone.Register();
        }
    }
}
```