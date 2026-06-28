

# Common Attributes

This section describes attributes and signals that are common across all components.

For interactive examples using common attributes and CSS classes, refer to the [Showcase Application](https://sdkcon78221.crestron.com/downloads/ShowcaseApp/common-attributes/append-class-when-in-viewport.html).

## Attributes

- **id**: A standard HTML identifier attribute.
- **customClass**: A list of space-delimited CSS class names that are applied to the component.
- **customStyle**: A list of semicolon-delimited CSS directives applied on the component.
- **show**: A Boolean value that determine if the component is seen by the user.
- **noshowType**: Reflects the type of visibility applied to the item. Refer to data‑ch5‑noshow‑type in [Custom Attributes](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/UI-QS-Custom-Events.htm) for more information.
- **disabled**: A standard HTML attribute. Directs the component to change CSS and event listeners to reflect a disabled state when true.
- **debug**: Used to print diagnostic information to the console logs. Can be appended to a CH5 component in order to receive additional information in the browser console (for example, <ch5-button type="default" label="oval" debug>).
- **class**: A standard HTML attribute.
- **style**: A standard HTML attribute.
- **role**: An accessibility attribute implemented by all CH5 components and added automatically if not set by the user. Where possible, represents the closest supported standard HTML attribute for a CH5 component.

## Signals Received from CH5

- **receiveStateCustomClass**: The value of this signal will be applied equally as a property on customClass. The value change removes the prior value and applies the new value.
- **receiveStateCustomStyle**: The value of this signal will be applied equally as a property on customStyle. The value change removes the prior value and applies the new value.
- **customStyle**: A list of semicolon-delimited CSS directives applied on the component.
- **receiveStateShow**: When true, the Boolean value of the signal determines if the component is seen by the user.
- **receiveStateShowPulse**: On a transition from false to true, this signal directs the component to become visible.
- **receiveShowHidePulse**: On a transition from true to false, this signal directs the component to no longer be visible.

NOTE: The receiveStateShowPulse and receiveShowHidePulse attributes will not work with the numeric join number attributes.

- **receiveStateEnable**: When true, the Boolean value of this signal determines if the component is enabled.

NOTE: The signal name is provided, and the value of the signal has the opposite convention of the disabled attribute. This is to provide consistency with current programming practices.

## Signals Sent to CH5

- **sendEventOnShow**: The Boolean value is true when the component is visible and false when the component is not visible.

NOTE: A component is still considered visible even if it is covered completely by other visible elements.

## Component Configuration Functions

CH5 components can be configured with default values for attributes and templatevariables. This configuration can be done using Ch5Config and its API methods:

- **loadConfig(config:TCh5Config)**: Loads a new configuration and overrides the existing one.
- **setAttributeForId(elementId:string, attributeName:string, attributeValue:string)**: Sets an attributeValue for an attributeName of the specified HTML elementId.
- **setAttributeForComponent(componentName:string, attributeName:string, attributeValue:string)**: Sets an attributeValue for an attributeName of the specified CH5 component (component name).
- **setTemplateVarsForId(elementId:string, tempVarsItems:any\[\])**: Sets the template variables for the CH5 components that have the specified elementId.
- **getConfig()**: Returns the current configuration object.
- **getAttributesForId(elementId:string):TCh5ConfigAttributes**: Returns the configured attributes for the components that have the specified elementId.
- **getAttributesForComponent(componentName:string):TCh5ConfigAttributes**: Returns all configured attributes for the component specified in **componentName** (for example 'ch5-button').
- **getTemplateVarsForElementById(elementId:string):TCh5ConfigTemplateVars\[\]**: Returns the configured template variables for the components that have the specified elementId.
- **getAttributesForElement(cr:Ch5Common):TCh5ConfigAttributes**: Returns all configured attributes for a CH5 component.
- **getTemplateVarsForElement(cr:Ch5Common):TCh5ConfigTemplateVars\[\]**: Returns all configured tempaltevariables for a CH5 component.