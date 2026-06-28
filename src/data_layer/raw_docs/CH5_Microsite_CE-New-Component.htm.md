

# Add a New Component

Once a contract has been created, programming components can be added to the contract. These components form the basis of the programming logic that connect touch screen UI elements to control system programs.

To add a new component to a contract:

1. Select the **Component Details** button from the side navigation menu to open the **Component Details** screen.
2. Select the **+** (plus) button next to the **Name** text field on the left side of the screen. The new component is added and an **Attributes** section is displayed under **Component Details**.

![](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Resources/Images/CE4.png)

NOTE: The new component is added as a tab under **Component Details**. Multiple components can be open at the same time and can be accessed by clicking the appropriate tab.

5. Enter a component name in the **Component Name** text field.
6. Enter a description for the component in the **Component Description** text field.
7. Click the fields under **Attributes** to enter the following information as needed.

NOTE: Multiple attributes can be added to a single component. Click and hold the grid icon on the left of the attribute to move its position in the order.

   - **Type**: Use the drop-down menu to select a command type ( **Boolean**, **Numeric**, or **String**).
   - **State**: Enter a programming state (attribute) for the component (for example, "Power\_On"). State is the feedback going from the control system to the touch screen user interface.
   - **State Notes**: Enter any notes for programming state with the component.
   - **Event**: Enter an event to use with the command. Events are commands sent from the touch screen user interface to the control system.
   - **Event Notes**: Enter any notes for programming the event.

Multiple components can be added to the same contract. Additionally, subcomponents can be added to a component for inclusion in the programming output. For more information, refer to [Add a Subcomponent](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/CE-Subcomponent.htm).