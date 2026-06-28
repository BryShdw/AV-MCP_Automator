

# Toggle

The <ch5-toggle> component is displayed as a two-state switch with simple transition between states. The component has the functionality of an HTML checkbox-type input element.

Like other input-based components, <ch5-toggle> can be part of a [Form](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/CO-Form.htm) that will cache state change until a submit method is called when attribute feedbackMode="submit".

For interactive examples using the <ch5-toggle> component and CSS classes, refer to the [Showcase Application](https://sdkcon78221.crestron.com/downloads/ShowcaseApp/ch5-toggle/label.html).

## Features

The <ch5-toggle> attributes provide the following features:

- Sets the on and off labels and icon classes
- Sets the shape of the toggle handle
- Sets the orientation of the toggle
- Sets the size of the toggle (x-small, small, regular, large, x-large, or custom)
- Sets the initial value of the component
- Sets a sync timeout between the user releasing the toggle handle and the time the toggle will check if the value is equal with the value from the signal
- Receives the value of the switch via control system state
- Sends a signal to the control system on a click or tap event