

# Create a Custom Crestron Template Project Component

The Crestron Template Project includes support for widgets, which are a reusable collection of HTML and CSS that can be used across pages and other widgets. Widgets, like VTPro-e ® software subpages, do not require any JavaScript programming.

The following sections describe how to create a new component in the Crestron Template Project that does not comprise existing components and HTML5 elements. These sections should be reviewed in sequential order.

## Prerequisites

This documentation assumes that you have a strong understanding of HTML, CSS, and JavaScript.

Additionally, the following topics should be reviewed prior to attempting the procedures in this topic.

- [Add a Project-Wide JavaScript Module](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Template-Project/Tasks/Add-Project-Wide-JS.htm)
- [Add Project-Wide CSS Styles and Classes](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Template-Project/Tasks/Add-Project-Wide-CSS.htm)
- [Publish Events and Send Joins to a Control System](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Advanced/Events-Joins-CS.htm)
- [Receive Control System State and Joins](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Advanced/Joins-Received-CS.htm)

## Determine the Component Appearance

First, determine what HTML elements and what CSS will provide the appearance of this component. You should provide a way to change the look of the component as the user interacts with it and when the control system updates its state. Tools like [jsfiddle](https://jsfiddle.net/) or [codepen](https://codepen.io/) can be used to draft the HTML and CSS.

## Add Project-Wide CSS Classes

Project-wide CSS classes and styles can be added to your project to style your component as described in [Add Project-Wide CSS Styles and Classes](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Template-Project/Tasks/Add-Project-Wide-CSS.htm).

Refer to the following best practices:

- Name your SASS .scss file so it is clearly related to the component. For example, if your component is named ‘My Component’, name your .scss file **mycomponent.scss**.
- Follow [BEM (Block, Element, Modifier)](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/BEM.htm) for the names of your CSS classes. For example, if your component has a base of .mycomponent{} classname and if your component has a “selected” view when feedback is received from the control system, use .mycomponent--selected{} class name. An embedded label element could be .mycomponent\_\_label{} classname.

## Add Project-Wide JavaScript

Project-wide JavaScript modules can be added to your project to define your component logic as described in [Add a Project-Wide JavaScript Module](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Template-Project/Tasks/Add-Project-Wide-JS.htm).

A best practice is to name your JavaScript .js file so it is clearly related to the component. For example, if your component is named ‘My Component, name your .js file **mycomponent.js**.

## Set Up a JavaScript Function

Set up a function as a constructor of an instance of your custom component.

In your JavaScript module, use the document.getElementById() or document.querySelector() to find a target element that can be populated with other HTML elements and/or can listen to document events.

Refer to the following example code:

Copy

```
function myComponentModule(id, label, eventName, stateName) {

   // find the element by parameter id
   const myComponentElement = document.getElementById(id);
   // TODO check for null return for invalid input.

   // add class=”mycomponent”
   myComponentElement.classList.add(‘mycomponent’);
   // add a child element ‘label’
   // create the element as an HTML <span>
   const myComponentLabel = document.createElement(‘span’);
   // add the parameter label as <span>${label}</span>
   myComponentLabel.textContent = label;
   // add the class to the label <span class=”mycomponent__label”>
   myComponentLabel.classList.add(‘mycomponent__label’);
   // add the label to the provided element
   myComponentElement.addChild(myComponentLabel);

}
```

## Listen for and Take Actions on Control System Join Values

Listen for changes in join values from the control system and take actions on that change as described in [Receive Control System State and Joins](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Advanced/Joins-Received-CS.htm)

In the example below, the subscription callback function adds or removes a ‘--selected' class from the classlist.

Copy

```
function myComponentModule(id, label, eventName, stateName) {

   // see earlier example
   const myComponentElement = document.getElementById(id);

   // the second parameter to subscribeState is a string even if it’s a join number.
   const stateSignalName = typeof(stateName) === 'number' ? stateName.toString() : stateName;
   const SELECTED_STATE_CLASSNAME = 'mycomponent--selected';

   // subscribe to change in Digital Join with name stateName
   const subscriptionId = CrComLib.subscribeState('b', stateSignalName, (value) => {
        // this function is called each time join changes in control system
        if (value) {
            // <xxx id=”id” class=”mycomponent mycomponent--selected">
            myComponentElement.classList.add( SELECTED_STATE_CLASSNAME );
        }
        else {
            // <xxx id=”id” class=”mycomponent">
            myComponentElement.classList.remove( SELECTED_STATE_CLASSNAME );
        }
    });

}
```

## Send Events to a Control System

Send events to the control system based on document events as described in [Publish Events and Send Joins to a Control System](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Advanced/Events-Joins-CS.htm).

In the example below, an event listener has been set up on ‘click’. When it is processed, a digital pulse (for example, Digital true followed by Digital false) is sent to the control system.

Copy

```
function myComponentModule(id, label, eventName, stateName) {

   // see earlier example
   const myComponentElement = document.getElementById(id);

   // the second parameter to publish is a string even if it’s a join number.
   const eventSignalName = typeof(eventName) === 'number' ? eventName.toString() : eventName;

   myComponentElement.addEventListener('click', (ev) => {
       // when clicked send a join
       CrComLib.publishEvent('b', eventSignalName, true);
       CrComLib.publishEvent('b', eventSignalName, false);
   });

}
```

## Deploy the Custom Component

Once you have completed the prior procedures, including adding custom JavaScript and CSS, your custom component can be deployed within your Crestron Template project.

1. From a page in the Crestron Template Project, add a new block element in the HTML file that has an id or query selector that will identify the component.

Copy

```
<div id=”mycomponent-17”></div>
```

5. In the .js file for the same page component, call the custom component function defined in the procedures above in the onInit() function.

Copy

```
myComponentModule(“mycomponent-17”, “my label”, 17, 17);
```

9. Reload the project. When that page is loaded, the onInit() function will be called, which subsequently will call the function to create your custom component.