

# Contract Structure

The AVF-CH5 contract is organized within a tree structure. The primary component nodes at the root are **Room** and **TimeDate**.

NOTE: Currently, .AV Framework only supports the first **Room** component in the list per control processor.

## Overview

The contract is organized as follows:

- The root of the contract contains an array of two **Room** components and a **TimeDate** component called **SystemTime**.
- The root **TimeDate** component has the current time and date from the control system.

## Room Components

The parent and child components of the contract related to the room are described in the sections that follow.

### Room

The **Room** component contains all other configurable components for the room. It is also the root for most joins that are used to communicate with the control system.

The **Room** component contains the following attributes.

| Attribute | Type | Description |
| --- | --- | --- |
| Locale | String | Indicates the locale of the system that is configured through the controller. This setting can be changed on the **System Settings** screen in the web configuration UI. |
| IsBusy | Boolean | Set when the .AV Framework system is busy. This flag is not currently used. |
| RoomName | String | The room name. |
| DisplayCount | Numeric | The number of displays configured for the room. |
| StartButtonEnabled | Boolean | Indicates that the **START** button option in the configuration settings is set to true. |
| StartButtonText | String | Custom text that can be displayed on the **START** button. |
| Tick | String | When the **EnableTick** command is executing, this value will update once per second with the tick value of the processor. **Tick** can be used to synchronize the animation time-step between running touch screens. |
| EnableTick | Command | When enabled, the controller will send updates to the **Tick** property. When disabled, control processor will stop sending updates to the **Tick** property. |
| Audio | Component | A child attribute containing the microphone and speaker audio state and control. |
| TouchScreenSettings | Component | A child attribute containing the configured touch screen settings. |
| LockTouchPanel | Component | A child attribute used to indicate the locked touch screen message. |
| Broadcast | Component | A child attribute used to indicate broadcast messages. |
| Power | Component | A child attribute containing power settings and power down behavior. |
| RoomScheduler | Component | A child attribute used for calendaring integration to reserve the room. |
| Display | Component | A child attribute containing displays that can be used for presentation. |
| SystemInfo | Component | A child attribute containing detailed controller information. |

### Audio

The **Audio** component provides control and state information for the audio subsystem of the control processor. The **Audio** component reports information for its parent **Room** component.

The **Audio** component contains the following attributes.

| Attribute | Type | Description |
| --- | --- | --- |
| IsMicMuted | Boolean | When enabled, all microphones in the room will be muted. |
| IsSpeakerMuted | Boolean | When enabled, all speakers in the room will be muted. |
| Volume | Numeric | The room volume percentage. |
| RaiseVolume | Command | When executing, volume will ramp up. When not executing, volume ramp will stop. |
| LowerVolume | Command | When executing, volume will ramp down. When not executing, volume ramp will stop. |
| MuteMic | Command | When executed, the mute state of the microphone is toggled on or off. |
| MuteSpeaker | Command | When executed, the mute state of the speakers is toggled on or off. |

The following diagram shows the relationship between the **Room** parent component and **Audio** child component.

![](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Resources/Images/Diagram2.png)

### TouchScreenSettings

The **TouchScreenSettings** component provides the touch screen with settings as configuring using the **Touch Screen Settings** screen in the .AV Framework web configuration UI.

The **TouchScreenSettings** component contains the following attributes.

| Attribute | Type | Description |
| --- | --- | --- |
| ScreenSaverEnabled | Boolean | When enabled, the touch screen will use the **ScreenSaver** settings to show/hide the screen saver. An example for consuming these settings is provided in the .AV Framework UI. |
| EnableCustomSSBackground | Boolean | When enabled, the UI will use the custom backgrounds provided by **CustomSSBackgroundUrls** for the screen saver. |
| CustomSSBackgroundUrls | String | A comma-delimited list of image files to use as the touch screen background. |
| EnableCustomHelpPage | Boolean | When enabled, the **Info** button loads a help file image provided by **CustomHelpPageUrl**. |
| CustomHelpPageUrl | String | A URL to a custom help page image file to replace the info screen image. |
| BackgroundsInterval | Numeric | The duration that must elapse before the next custom background image file is loaded. |
| ScreenSaverSleepTime | Numeric | The duration that the touch screen must be idle (in minutes) before the screen saver becomes active. |
| ScreenSaverStartTime | Numeric | The hour of day when the screen saver should become active. 0 = 12:00AM. |
| ScreenSaverEndTime | Numeric | The hour of day when the screen saver should become inactive. 0 = 12:00AM. |
| AVFUiTheme | String | The configured .AV Framework theme. This value must be "UI2\_CH5" for CH5-based UIs. |
| EnableCustomLogo | Boolean | When enabled, a custom logo image file is displayed. |
| CustomLogoUrl | String | A URL to a custom logo image file. |

The following diagram shows the relationship between the **Room** parent component and **TouchScreenSettings** child component.

![](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Resources/Images/Diagram1.png)

### LockTouchPanel

The **LockTouchPanel** component indicates the touch screen should display a blocking message and block all other operations. This behavior is independent from the power-related states and messages and is used by the control system to block normal AV operations during an otherwise normal power state.

The **LockTouchPanel** component contains the following attributes.

| Attribute | Type | Description |
| --- | --- | --- |
| InProgress | Boolean | When enabled, indicates that the touch screen should be blocked from operation by showing the **Message** string. |
| Message | String | A message displayed on the screen when **InProgress** is true. |

The following diagram shows the relationship between the **Room** parent component and **LockTouchPanel** child component.

![](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Resources/Images/Diagram3.png)

### Broadcast

The **Broadcast** component provides information to the touch screen about in‑progress broadcast messages. If the broadcast message type is an emergency, the message should be shown on screen while **InProgress** is true, it but can be dismissed by acknowledging the message.

The **Broadcast** component contains the following attributes.

| Attribute | Type | Description |
| --- | --- | --- |
| InProgress | Boolean | Indicates that a broadcast message has been raised. |
| Message | String | A message to be displayed on screen when a broadcast message is raised. |
| IsEmergency | Boolean | Indicates that the broadcast message is an emergency and must be acknowledged before it will be dismissed. |
| Acknowledge | Command | Indicates to .AV Framework that the current broadcast message has been dismissed, resetting the **InProgress** flag. |

### Power

The **Power** component provides state and control for the power state of the .AV Framework system.

The **Power** component contains the following attributes.

| Attribute | Type | Description |
| --- | --- | --- |
| IsPowerOn | Boolean | When true, indicates that the .AV Framework system power state is on. |
| IsShuttingDown | Boolean | When true, indicates that the shutting down sequence is in progress. |
| ShuttingDownCount | Numeric | The current countdown value of the shutting down sequence. |
| CancelShutdown | Command | If the .AV Framework system is currently shutting down, executing this command will cause the system to immediately complete the shutdown sequence and remain on. |
| CompleteShutdown | Command | If the .AV Framework system is currently shutting down, executing this command will cause the system to immediately complete the shutdown sequence and power off. |
| PowerOn | Command | Powers the .AV Framework system on. This command is not used by the touch screen. |
| PowerOff | Command | Powers the .AV Framework system off. This command begins the shutting down sequence. |

### Display

The **Display** component provides an entry point for controlling an .AV Framework presentation.

The **Display** component contains the following attributes.

| Attribute | Type | Description |
| --- | --- | --- |
| SourceCount | Numeric | The number of sources in the source list available for routing. |
| WarmingUp | Boolean | When true, indicates that the display is in a warm up cycle. |
| CoolingDown | Boolean | When true, indicates that the display is in a cool down cycle. |
| VideoMuteMode | Numeric | The current mode associated with the blank video command.<br>0 = stop, 1 = Blank, 3 = Blanking |
| Device | Component | The **Device** component for the display. |
| StopRoute | Command | Execute to stop routing the display. |
| BlankRoute | Command | Execute to blank the source route for the display. |
| Source | List<Source> | A list of available sources for routing. |
| PresentingSource | Component | The **PresentingSource** component for the display. Valid when the **Presenting** flag is true. |

### PresentingSource

The **PresentingSource** component represents information for the source that is currently presenting within its parent **Display** component. The P **resentingSource** component is valid when its **Presenting** flag is true.

The **PresentingSource** component contains the following attributes.

| Attribute | Type | Description |
| --- | --- | --- |
| Presenting | Boolean | When true, indicates that the parent **Display** component is presenting and that this component is valid. |
| AudioFollow | Boolean | When true, indicates that the source's audio is being presented on one or more display devices. |
| HasSync | Boolean | When true, the input device is sending and the AV switcher is receiving sync signal. |
| ChannelType | String | Describes the channel that this source is presenting from.<br>Examples: HDMI® channel, DM® channel, VGA |
| Device | Component | The **Device** component for the source. |
| AirMediaDetail | Component | When this source’s **Device.Type** is **AirMedia**, the **AirMediaDetail** component will be valid. |
| Backspace | Command | A command for the backspace media function. |
| Key0 | Command | A command for the key 0 media function. |
| Key1 | Command | A command for the key 1 media function. |
| Key2 | Command | A command for the key 2 media function. |
| Key3 | Command | A command for the key 3 media function. |
| Key4 | Command | A command for the key 4 media function. |
| Key5 | Command | A command for the key 5 media function. |
| Key6 | Command | A command for the key 6 media function. |
| Key7 | Command | A command for the key 7 media function. |
| Key8 | Command | A command for the key 8 media function. |
| Key9 | Command | A command for the key 9 media function. |
| Pound | Command | A command for the pound media function. |
| Asterisk | Command | A command for the asterisk media function. |
| Period | Command | A command for the period media function. |
| Dash | Command | A command for the dash media function. |
| ForwardScan | Command | A command for the forward scan media function. |
| ReverseScan | Command | A command for the reverse scan media function. |
| Play | Command | A command for the play media function. |
| Pause | Command | A command for the pause media function. |
| Stop | Command | A command for the stop media function. |
| ForwardSkip | Command | A command for the forward skip media function. |
| ReverseSkip | Command | A command for the reverse skip media function. |
| Repeat | Command | A command for the repeat media function. |
| Return | Command | A command for the return media function. |
| Back | Command | A command for the back media function. |
| UpArrow | Command | A command for the up arrow media function. |
| Down Arrow | Command | A command for the down arrow media function. |
| Left Arrow | Command | A command for the left arrow media function. |
| Right Arrow | Command | A command for the right arrow media function. |
| Select | Command | A command for the select media function. |
| Enter | Command | A command for the enter media function. |
| Clear | Command | A command for the clear media function. |
| Home | Command | A command for the home media function. |
| Menu | Command | A command for the menu media function. |
| Red | Command | A command for the red media function. |
| Green | Command | A command for the green media function. |
| Blue | Command | A command for the blue media function. |
| Yellow | Command | A command for the yellow media function. |
| PopUpMenu | Command | A command for the pop-up menu media function. |
| TopMenu | Command | A command for the top menu media function. |
| Options | Command | A command for the options media function. |
| Eject | Command | A command for the eject media function. |
| Exit | Command | A command for the exit media function. |
| ThumbsUp | Command | A command for the thumbs up media function. |
| ThumbsDown | Command | A command for the thumbs down media function. |
| Replay | Command | A command for the replay media function. |
| Favorite | Command | A command for the favorite media function. |
| Dvr | Command | A command for the DVR media function. |
| Live | Command | A command for the live media function. |
| Record | Command | A command for the record media function. |
| OnDemand | Command | A command for the on demand media function. |
| ChannelUp | Command | A command for the channel up media function. |
| ChannelDown | Command | A command for the channel down media function. |
| PlayPause | Command | A command for the play/pause media function. |
| Info | Command | A command for the info media function. |
| Guide | Command | A command for the guide media function. |
| Last | Command | A command for the last media function. |

### AirMediaDetail

The **AirMediaDetial** component provides information received by the control processor from the associated and configured AirMedia® device. These details are valid for the **PresentingSource** display when the **Device.Type** is **AirMedia**.

The **AirMediaDetail** component contains the following attributes.

| Attribute | Type | Description |
| --- | --- | --- |
| Users | Numeric | The number of connected AirMedia users. |
| HasPin | Boolean | When true, indicates that a PIN is required to connect to AirMedia from the guest client. |
| Address | String | The web address used by the guest client to connect to AirMedia. |
| Pin | String | The PIN code used by the guest client to connect to AirMedia. |

### SystemInfo

The **SystemInfo** component provides details for how system state information is organized and provided to the touch screen. The type of information is visualized on the help pages of the .AV Framework touch screen.

The **SystemInfo** component contains the following attributes.

| Attribute | Type | Description |
| --- | --- | --- |
| HostName | String | The .AV Framework controller host name, |
| FusionServerStatus | String | The Crestron Fusion connection status. |
| FusionRoomName | String | The room name in Crestron Fusion. |
| MACAddress | String | The .AV Framework controller MAC address. |
| VersionNumber | String | The .AV Framework version number. |
| SystemType | String | The type of .AV Framework controller (e.g., MPC3‑101). |
| Ready | Boolean | Indicates the controller has finished booting. When this value is false, the touch screen displays an Initializing screen which blocks touch screen operation. |
| SystemState | String | The configuration state of the system. When this value is **Configuring**, .AV Framework may not be sending current state information to the touch screen and may not process Command execution. The touch screen uses this state to display a Configuring screen which blocks touch screen operation.<br>.AV Framework may report additional configuration states as follows:<br>**UnConfigured**: This is the default state of the system before the .AV Framework configuration is loaded. When the system is in this state, it is not online.<br>**Configuring**: When a changed .AV Framework configuration has been saved, the .AV Framework system goes offline. This state indicates that the configuration has not yet been applied in the configuration UI.<br>**Configured**: When configured, the .AV Framework system is active and online.<br>**UnKnown**: Indicates that the system is not reporting a state, possibly caused by an error. |

## Scheduling Components

The parent and child components of the contract related to scheduling are described in the sections that follow.

### RoomScheduler

The **RoomScheduler** component is a child component of a **Room** that encapsulates the scheduling capabilities for the room. The state information that is provided by the **RoomScheduler** component indicates to the current schedule state to the touch screen.

The **RoomScheduler** component contains the following attributes.

| Attribute | Type | Description |
| --- | --- | --- |
| IsCalendaringConnected | Boolean | When calendaring is connected, this is true. If false, check that your calendaring has been configured correctly in the .AV Framework configuration web UI pages. |
| IsBusy | Boolean | Set when the scheduling calendar is busy. The .AV Framework controller handles the last scheduling request. At this time, the touch screen should indicate that the system is busy and is not ready to take additional requests to schedule meetings. |
| AvailableAllDay | Boolean | Set when there is no next meeting. This flag will indicate whether the **NextMeeting** component has valid information. If this flag is false, the **NextMeeting** information is not valid. |
| MeetingInProgress | Boolean | Set when the current meeting is in progress. This flag will indicate whether the **CurrentMeeting** component has valid information. If this flag is false, the **CurrentMeeting** information is not valid. |
| HasNextMeeting | Boolean | Set if there is a valid upcoming meeting in **NextMeeting**. If this flag is true, the **NextMeeting** information describes the upcoming event. |

The following components are referenced by the **RoomScheduler** component.

| Attribute | Type | Description |
| --- | --- | --- |
| CurrentMeeting | Component (MeetingDetail) | The current meeting that is in progress. If the **MeetingInProgress** flag is false, this information is not valid. |
| NextMeeting | Component (MeetingDetail) | Set when the scheduling calendar is busy. The .AV Framework controller handles the last scheduling request. At this time, the touch screen should indicate that the system is busy and is not ready to take additional requests to schedule meetings. |

### MeetingDetail

The **MeetingDetail** component describes the scheduled meeting as a calendar event.

The **MeetingDetail** component contains the following attributes.

| Attribute | Type | Description |
| --- | --- | --- |
| Organizer | String | The meeting organizer. Can be left blank if privacy is enabled. |
| Subject | String | The meeting subject. Can be left blank is privacy is enabled. |
| IsPrivate | Boolean | When true, privacy is enabled. If this flag is true, one or both of the fields are marked as private and are blanked before being sent. |

### ReserveNow

The **ReserveNow** component encapsulates the meeting reservation workflow provided by the .AV Framework controller. This workflow creates a new calendar event associated with a meeting.

The **ReserveNow** component contains the following attributes.

| Attribute | Type | Description |
| --- | --- | --- |
| StartTime | Component (TimeDate) | Indicates the time at which a new reservation will start. This is the start time of the calendar event created by the **ReserveNow** workflow. |
| ReserveNowOption | List<ReserveNowOption> | A list of times that can be reserved from the touch screen. |
| RecalculatedOptions | Command | This command is used to update the **StartTime** and **ReserveNowOption** list. |
| OptionsCount | Numeric | The number of options that are valid in the **ReserveNowOption** list. |

The **ReserveNow** component has the following workflow:

- The user executes the **RecalculatedOptions** command to refresh the **ReserveNowOption** list.
- After the **ReserveNowOption** is updated, the user is presented with these updated options.
- The user can then select which option to reserve from the list and completes the reservation by executing the **ReserveNowOption** command.

![](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Resources/Images/Diagram4.png)

### ReserveNowOption

The **ReserveNowOption** component combines a **TimeDate** component with a **Command** component. This provides a visual representation of which time slot is available for reservation using the **ReserveNow** component.

The **ReserveNowOption** component contains the following attributes.

| Attribute | Type | Description |
| --- | --- | --- |
| EndTimeDate | Component (TimeDate) | Indicates the end time for the new reservation option. |
| Command | Component | The command component of the **ReserveNowOption** component. |