

# Tab Button

The <ch5-tab-button> component contains a group of buttons that are aligned to create a column of tabbed buttons. Each button supports an icon, text label, and custom programming via a Smart Object ID.

For interactive examples using the <ch5-tab-button> component and CSS classes, refer to the [Showcase Application](https://sdkcon78221.crestron.com/downloads/ShowcaseApp/ch5-tab-button/ch5-tab-button-contract-name.html).

## Features

The <ch5-tab-button> attributes provide the following features:

- Sets the orientation of the tab button.
- Sets a contract name ID (Smart Object ID) as an encapsulated join type that links a smart control in VT Pro-e software with a CED in SIMPL programming.
- Sets the number of tab buttons in the tab control (between 2 and 15). The default value is "3".
- Allows for a differentiation of each list item via the <ch5-tab-button-label> element.
- Allows the following attributes to be configured for each button in the button tab: type, label alignment, icon position, shape, selected state, pressed state, encoded HTML content, and URL.
- Allows events to be sent to the control system for each button press.
- Allows feedback to be received from the control system following a button press.