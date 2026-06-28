

# Debugging

Debugging the contract can be performed by using the console commands described in this section or by inspecting using the provided .AV Framework touch screen.

## AVF-CH5 Console Commands

The following console commands can be issued to the touch screen to test various behavior using Crestron Toolbox™ software. For more information, refer to the Crestron Toolbox help file.

- **CH5PrintStates**: All of the contract states can be seen by issuing this command, as well as some attributes that are not transmitted to the contract, such as **Device ID**.
- **CH5FakeSync**: Issuing this command simulates a sync status. This is useful for testing the change of sync state when the physical device is not present or sync cannot be changed because it is remote.
- **CH5PowerOffButton**: Issuing this command simulates the physical button press for power off. This is useful for testing the physical button power off button behavior when the touch screen is remote.
- **CH5PowerOnButton**: Issuing the command simulates the physical button press for power on. This is useful for testing physical button power on button behavior when the touch screen is remote.
- **CH5Present**: Issuing this command starts presenting on a connected display.
- **CH5StopRoute**: Issuing this command stops presenting on a connected display.