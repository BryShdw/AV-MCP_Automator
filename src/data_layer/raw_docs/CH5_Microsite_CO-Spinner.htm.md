

# Spinners

The <ch5-spinner> component is similar to the <ch5-select> component in that it allows a user to select one or more choices from a list of options. The main differences between the components are in the visual representation of each:

- The spinner component presents a vertical list of values centered around one central item, which is considered the single selected item.
- Swiping up and down on the items allows a user to see other selections, and placing an item in the center position selects the item.
- Unlike the <ch5-select> component, only one item can be selected. This component does not support selecting multiple items or no items.
- Receiving state feedback and sending a selected event on a per-item basis is not supported
- The selected item feedback can be set with a 0-based number signal and the user-selected item will be sent as a 0-based number signal.

This component allows the designer to provider an optional template as definition for each item in the list, like the <ch5-list> component, the template uses a {{Index}} moniker that will be substituted with a 0-based index of the item in the selection. When a template is not provided, an implied template containing a label and icon is supplied by the <ch5-spinner> component. The implied template includes Icon and Label subcomponents.

Like other input-based components, <ch5-spinner> can be part of a [Form](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/CO-Form.htm) that will cache state change until a submit method is called when attribute feedbackMode="submit".

For interactive examples using the <ch5-spinner> component and CSS classes, refer to the [Showcase Application](https://sdkcon78221.crestron.com/downloads/ShowcaseApp/ch5-spinner/attribute-size.html).

## Features

The <ch5-spinner> attributes provide the following features:

- Sets the number of entries in a selection
- Sets the position of an icon based on text direction
- Sets the number of items to be visible in the upper/lower container on either side of the selected item conteiner.
- Sets the height of an item
- Sets resizing behavior
- Allows the spinner to loop endlessly (the first item follows the last item and the last item precedes the first item when swiping)
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