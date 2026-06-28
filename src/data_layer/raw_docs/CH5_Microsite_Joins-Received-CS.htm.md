

# Receive Control System State and Joins

The following sections describe how to subscribe to control system state and to take actions on joins received from the control system.

## Subscribe to Control System State

CH5 components should reflect the state or values of the control system program. As the state or values from in the control system program are updated, they are sent to the touch screen as joins. CH5 components listen to those join changes and then update HTML elements to reflect the received values.

To allow advanced CH5 developers to create custom components that take action on joins received from the control system, the CH5 component library exposes a JavaScript function. This function is named CrComLib.subscribeEvent because it listens to state changes from the control system.

The CrComLib.subscribeState(type, signalName, callbackFunction ) function requires three parameters

- typeis a string parameter that is expected to be one of the following values:
  - 'b' or 'boolean': Indicates the value will be either true of false (like a Digital Join)
  - 'n', 'numeric', or 'number': Indicates the value will be a 16-bit integer number between the values of 0 to 65,535 or -32,768 to 32,767 (like an Analog Join)
  - 's' or 'string': Indicates the value will be a string (like a Serial Join)
  - 'o' or 'object' – indicates the value will be an object. Reserved for future use.
- signalName is a string parameter that is either a string representation of a join number or Contract Editor signal name. For more information on signal names, refer to [Contract Editor](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/CE-Overview.htm).
- callbackFunction is a function that will be called with the join value as received from the control system

## Receive a Digital Value from the Control System

Digital values can be received from the control system as the result of events occurring within HTML elements.

For example, consider an HTML <div> element that should be change its appearance based upon the Boolean value of digital join 33 received from the control system. The appearance is changed by appending a “--selected" class to the class list when join is true and removing “--selected" class when the join is false.

Copy

```
<div id="my-toggle" class="toggle"></div>

.toggle {
    width: 75px;
    height: 50px;
    border: 2px solid black;
    background-color: white;
}

.toggle--selected {
    background-color: rgba(0,0,255, .75); \
}
```

Using the CrComlib.subscribestate would have the following elements:

Copy

```
    const stateSignalName = '33';
    // NOTE: second parameter to CrComLib.subscribeState() is always a string
    const id = "my-toggle";
    const toggleElement = document.getElementById(id);
    CrComLib.subscribeState('b', stateSignalName, (value) => {
        console.log(`toggle(${id}) selected(${value})`);
        if (value) {
            toggleElement.classList.add(SELECTED_STATE_CLASSNAME);
        }
        else {
            toggleElement.classList.remove(SELECTED_STATE_CLASSNAME);
        }
    });
    toggleElement.addEventListener('click', onClick);
```

## Receive a Ramp Control Block from the Control System

A Ramp Control Block (RCB) is a method to communicate an Analog (or Numeric value) join from the control system. Similar to an Analog join, an RCB can provide a numeric value for a light, shade, or amplifier level. However, it also includes a time element to control how long it should take to reach that level.

A RCB can be generated in a SMIPL program with an Analog Preset or a Analog Ramp symbol. Refer to the following image.

![](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Resources/Images/RCB-1.png)

In SIMPL# Pro, the UShortInputSig.CreateRamp(ushort finalRampValue, uint timeToRamp) and UShortInputSig.StopRamp() functions can generate and stop an RCB.

An Analog Join can be subscribed to with the time duration as a special object. The state signal name for this subscription is the same as an Analog Join subscription, but the type is ‘o’ or ‘object,’ and the value received is in the following format:

Copy

```
{
   "rcb": {
      "time": ,
      "value": ,
      "startt": ,
      "startv":
   }
}
```

Each parameter has the following function and values:

- **time**: Numeric, the duration of the RCB (in milliseconds).
- **value**: Numeric, a number between 0 and 65,535 or -32,768 and 32,767.
- **statt**: (Optional) Numeric, The time difference between epoch and when the RCB started. Can be compared to Date.now().
- **startv**: (Optional) Numeric, The starting value of when the ramp began.

As an example, a user initiates a down RCB at 2022-05-07 14:34:46 UTC (1,652,798,086,106 milliseconds since Jan 1, 1970). The prior value was 49,152 (75%). The ramp time was set at 2 seconds, so the control system will request to go from 0 (0%) to 1500 ms (75% of 2 seconds).

The subscription callback for this scenario would be as follows:

Copy

```
{
   "rcb": {
      "time": 1500,
      "value": 0,
      "startt": 1652798086106,
      "startv": 49152
   }
}
```

After a quarter second, the user stops the down ramp. The control system indicates the new value is 32,768 (50%).

Copy

```
{
   "rcb": {
      "time": 0,
      "value": 32768,
   }
}
```

The following sample code is provided for programming Ramp Control Blocks.

Copy

```
const myFabricElement = document.querySelector(`#${id} .shade__fabric`);
const stateSignalName = typeof(stateName) === 'number' ? stateName.toString() : stateName;

const subscriptionId = CrComLib.subscribeState('o', stateSignalName, (value) => {
    console.log(`shade(${id}) subscription(${JSON.stringify(value)})`);
    if (value.hasOwnProperty('rcb')) {
        myFabricElement.style.transitionDuration = `${value['rcb']['time']}ms`;
        myFabricElement.style.transform = `scaleY(${value['rcb']['value']/65535})`;
     }
});
```