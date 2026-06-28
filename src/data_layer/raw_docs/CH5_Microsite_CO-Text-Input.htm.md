

# Text Input

The <ch5-textinput> component inherits features of the standard <input> HTML tag but also provides extra features unique for CH5. Like other input-based components, <ch5-textinput> can be part of a [Form](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/CO-Form.htm) that will cache state change until a submit method is called when attribute feedbackMode="submit".

For interactive examples using the <ch5-textinput> component and CSS classes, refer to the [Showcase Application](https://sdkcon78221.crestron.com/downloads/ShowcaseApp/ch5-textinput/attribute-placeholder.html).

## Features

The <ch5-textinput> attributes provide the following features:

- Allows users to enter text input
- Sets scaling behavior for the font size.
- Sets masking behavior for the background pattern when the input is focused.
- Sets icon visibility, labels, and position.
- Sets a placeholder value for the input.
- Sets the type, minimum/maximum length, and minimum/maximum value of the input.
- Sets size and stretch behavior for the component.
- Sets text transform behavior as needed.
- Updates the input field upon receiving control system state.
- Sends feedback to the control system after value changes, focus, and blur

## Design Considerations

When using the mask attribute, the following combinations of prebuilt definitions are permitted:

- a: alpha character
- 9: numeric character
- \*: alphanumeric character

No other definitions are valid.

* * *

When using the text input control in a CH5 project loaded on a TSW-60 series touch screen, pressing **Enter** will send an event instead of going to the next line. This behavior is expected.