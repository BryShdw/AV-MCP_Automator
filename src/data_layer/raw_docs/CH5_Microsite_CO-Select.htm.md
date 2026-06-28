

# Select

The <ch5-select> component allows a user to select one or more choices from a list of options.

This component allows the designer to provider an optional template as definition for each item in the list, like the <ch5-list> component, the template uses a {{Index}} moniker that will be substituted with a 1-based index of the item in the selection. When a template is not provided, an implied template containing a label and icon is supplied by the <ch5-select> component. The implied template includes Icon, Label, and Checkbox subcomponents.

Like other input-based components, <ch5-select> can be part of a [Form](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/CO-Form.htm) that will cache state change until a submit method is called when attribute feedbackMode="submit".

For interactive examples using the <ch5-select> component and CSS classes, refer to the [Showcase Application](https://sdkcon78221.crestron.com/downloads/ShowcaseApp/ch5-select/dimensions.html).

## Features

The <ch5-select> attributes provide the following features:

- Sets the number of entries in a selection
- Sets the position of an icon based on text direction
- Allows multiple items to be selected
- Displays a text prompt if no items are selected
- Sets the height and width of the panel containing the list, including minimum and maximum values
- Sets resizing behavior
- Allows the menu mode to be chosen (plain, which allows to menu to be opened and closed by a user, or panel, which forces the menu to stay open even when it is not in focus)
- Sets a sync timeout between the user releasing the toggle handle and the time the toggle will check if the value is equal with the value from the signal
- Changes the value of the index (0-based) based on received control system state
- Sets the selection size based on received control system state
- Sends a signal to the control system on a focus event
- Sends a signal to the control system when the selection value changes

## Design Considerations

Standard-issue Angular uses {{ variable }} in HTML markup to allow the markup to display a value of the variable in the typescript/JavaScript. HTML5 UI also uses the double mustache {{ index }} as a counter in lists. However, Angular can be directed not to interpret the {{ }} and to leave them for interpretation by HTML UI via the [ngNonBindable directive](https://ngrefs.com/latest/templates/ngnonbindable "https://ngrefs.com/latest/templates/ngnonbindable").

Refer to the sample code below from the Showcase Application as an example:

Copy

```
<!--When using a computed property <b>{{ idx }}</b>, Angular tries to process it as an embedded expression, adding ngNonBindable to the template will force Angular to ignore it.-->

<ch5-list id="demo-list-1" size="500" maxHeight="400px" indexId="idx">
    <template ngNonBindable>
        <div class="horizontal-list-item">
            <span>item_{{idx}}</span>
        </div>
    </template>
</ch5-list>
```