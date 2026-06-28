

# Hard Buttons

CH5 supports performing actions that are triggered by hard button presses on touch screens. The five hard buttons generate a state signal of “Csig.Hard\_Button\_X.Press” where X is numbers ‘1’ to ‘5’.

The state Boolean signal value is true when the button receives a press motion and false when no press is present.

- Csig.Hard\_Button\_1.Press
- Csig.Hard\_Button\_2.Press
- Csig.Hard\_Button\_3.Press
- Csig.Hard\_Button\_4.Press
- Csig.Hard\_Button\_5.Press

**Example**

<ch5-modal-dialog receiveStateShowPulse="Csig.Hard\_Button\_1.Press" title="Shutdown System" prompt="Turn the system off?" closable mask>

</ch5-modal-dialog>

![TSW Hard Buttons](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Resources/Images/TSW-Hard-Buttons.png)