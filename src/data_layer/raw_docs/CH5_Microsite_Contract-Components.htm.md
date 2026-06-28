

# Contract Components

The following components are provided within the AVF-CH5 contract.

## Command

The **Command** component is used to control events that can be executed in .AV Framework. The **Execute** event is set to **true** when the command execution begins and set to **false** when the execution finishes. Typically, a command begins and then immediately ends execution, such as when commanding the control system to mute the microphone. There are other usages where execution can begin without ending immediately, such as ramping the volume.

In addition to the **Execute** event, **Command** has two state attributes as described in the following table.

| Attribute | Type | Description |
| --- | --- | --- |
| CanExecute | Boolean | Sets when command can be executed.<br>**CanExecute** is a flag indicating that a condition or state of the system is preventing the execution of the Command. **CanExecute** can be used with CH5 controls to bind to the “enable” property, which indicates the capability is currently unavailable.<br>For example, when the system is in the **Off** power state, certain commands will have the **CanExecute** flag set to false, indicating that if the **Execute** event is sent, it will be ignored. |
| Supports | Boolean | Sets when this command is supported by its parent component.<br>Similar to **CanExecute**, when the **Supports** flag is **false**, this indicates a nontemporary state of the system is preventing the execution of the command.<br>**Supports** is commonly used when indicating which media commands are supported by the device that is being presented on the output device. **Supports** can be used with CH5 controls to bind to the “visible” property, which indicates that the capability is not available. |

## Device

The **Device** component encapsulates details for repeated attributes associated with source and display components and future device types described by the system.

The **Device** attributes are described in the following table.

| Attribute | Type | Description |
| --- | --- | --- |
| Icon | String | The device icon that is assigned in the configuration screen. |
| Name | String | The device name that is assigned in the configuration screen. |
| Model | String | The device model (optional). |
| Type | String | The device type (optional). |

The **Type** and **Model** attributes are used to indicate to the touch screen which control page to display for a source device. For example, if the **Type** is **AirMedia**, the AirMedia pages are shown when presenting this source.

## TimeDate

The **TimeDate** component encapsulates the common formats for presenting time and dates, taking into account the locale settings and formatting set in the .AV Framework system settings.

The **TimeDate** attributes are described in the following table.

| Attribute | Type | Description |
| --- | --- | --- |
| DateFormatted | String | The formatted date string. |
| TimeFormatted | String | The formatted time string excluding AM and PM. |
| TimeFormattedAMPM | String | The formatted time string including AM and PM. |

The **Type** and **Model** attributes are used to indicate to the touch screen which control page to display for a source device. For example, if the **Type** is **AirMedia**, the AirMedia pages are shown when presenting this source.