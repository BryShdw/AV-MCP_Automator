

# Utility Functions

With Smart Graphics projects, analog and digital joins can be converted to strings to be added to text controls. CH5 provides equivalent functionality, but it requires working with JavaScript using the CrComLib.subscribeStateScript() and TextFormat() functions.

- The CrComLib.subscribeStateScript() function builds on the general CrComLib.subscribeState() function, but allows multiple subscriptions to managed simultaneously. Whenever any of the underlying state signals have updated values, the script provided to the function will be called. The result of the script will be the parameter of a provided callback function.
- The CrComLib.TextFormat() function is a helper function to provide a text string based upon the value of state signals.

For an illustration of these functions, refer to the following JavaScript code:

Copy

```
const el =document.querySelector('#updated-element');
const signalScript="CrComLib.textformat(\"WifiStrength: {1}\",{{n.Wifistrength}})";
const callback = function(result){
    el.textContent = result;
};

const subscription = CrComLib.subscribeStateScript(signalScript, callback, 'defaultValue');
// save the subscription to call the CrComLib.unsubscribeStateScript(subscription)
// function if and when no longer required
```

The following example shows the code above combined with HTML:

Copy

```
<ch5-slider sendEventOnChange="ChangeWifistrength" receiveStateValue="Wifistrength"></ch5-slider>

<div id="updated-element"></div>
```

The following example shows the code above combined with control system emulation:

Copy

```
{
    "cues": [\
        {\
            "type" : "n",\
            "event": "ChangeWifistrength",\
            "trigger": "&change",\
            "actions": [\
                {\
                    "type": "n",\
                    "logic": "link",\
                    "state": "Wifistrength" }\
            ]\
        }\
    ],
    "onStart": [\
        {\
            "type": "n",\
            "state": "Wifistrength",\
            "value": 0\
        }\
    ]
}
```

The result may look as follows in the GUI:

![](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Resources/Images/Function.gif)