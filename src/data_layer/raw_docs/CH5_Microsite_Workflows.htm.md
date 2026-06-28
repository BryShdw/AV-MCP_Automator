

# Workflows

This topic describes the various workflows that are supported by the AVF-CH5 contract.

Note the following points about the .AV Framework rooms when using the AVF‑CH5 contract:

- The data structure of the base AVF processor program was designed to run multiple rooms from a single instance of the programming. A Room\[x\] field has been added to the AVF-CH5 contract to support this design.
- At present, only one room per program is configured internally.
- All AVF-CH5 contract APIs start with Room\[0\]. Refer to [Contract Structure](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/AV-Framework/API-Reference/Contract-Structure.htm) for more information.

## Media Presentation Workflow

The AVF-CH5 contract allows for organization of the **Media** components associated per room. Each **Room** component contains an array of **Display** components that have been configured using web configuration. Each display can select from a list of configured input sources. These sources are available for selection from a list associated with each display.

Since each display has a different set of sources available for routing, each it also has its own list of sources. Each display can present a single input source at a time. This is modeled as **PresentingSource** object. When a source begins presentation on a display, the associated **PresentingSource** component updates to reflect the state of presentation and to provide access to media control commands.

The workflow for presenting a source from a touch screen is as follows:

1. When the touch screen first loads, a join will be received on the room called **DisplayCount**. This join tells the touch screen which displays are valid from the list associated with the room.
2. For each display, details for each **Source** component in the source list are received, as well as a **SourceCount** value on the display.
3. The user can now view the sources that are available for each display and details for each source, such as the following:

   - **HasSync**: Indicates if video sync is detected for the input source.
   - **AudioFollow**: Indicates that the source audio is being presented through the speakers for this source.
   - **Default**: Indicates the source will be regarded as the default source.
   - **Presenting**: Indicates that the source is currently presenting on the associated display.

5. Detailed information about the source device is available from the source list for each **Source** component. Each device will have a **Type** and **Model**, which can be used by the touch screen for determining how to render the page.
6. The user can present the source from the list by executing the **Present** command. At this point, the touch screen may switch views to control the media that has begun presentation. For example, the selected media source is Blu-ray Disc™ Player device. The touch screen may display a media control page appropriate for a Blu-ray Disc Player device. Refer to [Source Types](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/AV-Framework/API-Reference/Workflows.htm#Source) for more information.
7. If the display device has a warmup period, the **WarmingUp** flag for the display will change to **true**.
8. Once the source begins presenting, the **PresentingSource** associated with the display updates to show detailed media information. At this point, the **Presenting** flag for the **Source** component in the display list and the **PresentingSource** component will both change to **true**.

### Source Types

The following source types can be associated with a source:

- **AirMedia**: The **AirMedia** type is for connected AirMedia® presentation devices. When presenting an AirMedia device, the associated **AirMediaDetail** component is updated with details for AirMedia.
- **Blurray**: The **Bluray** type supports many models of Blu-ray Disc Player devices.
- **CableTv**: The **CableTv** type includes devices such as Tivo® and DirecTV® video cable box devices.
- **VideoServer**: The **VideoServer** type is for AppleTV® and Roku® video server devices
- **Uncontrolled**: This is the default for when the **Type** field is blank.

### Media Source Commands

When a Ddsplay has begun presenting and the associated **PresentingSource** component updates the **Presenting** flag to true, the commands associated with the **PresentingSource** will update based on whether they are supported or not. Each command’s **Supports** flag will reflect which associated commands are available based on the device that is configured. If the device had not been configured, none of the media commands will have this flag set true.

For Blu-ray Disc Player devices ( **Device.Type** is **bluray**) the commands associated with the Blu-ray Disc Player driver that is loaded will update based on how they are supported by that driver. For example, if the menu button is supported, this will be reported by the Blu-ray Disc Player driver, and subsequently be reported on the **Supports** field of the media command.

There are two commands for stopping the presentation on the display:

- **Blank**: If the display supports blanking, the panel will show a blanked screen (the display will be black with no video output). This will not stop the route on the display, but only will blank the output. This command is used mainly for devices that have long warmup or cooldown times. If the **Blank** command is executed and the display does not support blanking, a **Stop** command is executed instead.
- **Stop**: When the **Stop** command is executed, the control processor begins stopping the route. If the display has a cooldown period, the **CoolingDown** flag for the display will change to **true**.

## Room Scheduling Workflow

When .AV Framework is configured for use with a calendaring backend, such as Crestron Fusion® software, the touch screen provides the capability to view and create events within the calendar to book the room. For visualization, the touch screen can indicate if the room is available all day, currently in a meeting, or when the next reservation starts. The touch screen can also display the current meeting information and next scheduled meeting information.

Each room has a **RoomScheduler** component that is used as the entry point for this workflow. The room scheduler provides flags for the above described conditions:

- **AvailableAllDay**: Indicates that there are no meetings running and no meetings later today.
- **MeetingInProgress**: Indicates that a meeting is currently running.
- **HasNextMeeting**: Indicates that the room has a meeting later today.

There are two referenced components for **MeetingDetail** associated with the **RoomScheduler** that provide detailed meeting information:

- **CurrentMeeting**: Details for the meeting that is currently in progress.
- **NextMeeting**: Details for the next scheduled meeting that is not currently in progress.

The **RoomScheduler** provides room reservation capabilities via the **ReserveNow** component. This component provides scheduling options to the touch screen for creating a new reservation slot for the room. Using this component, the user can request updated meeting time slots, and then choose which one to use to book the room for an immediate meeting booking.

The workflow is as follows:

1. The touch screen invokes the **RecalculatedOptions** command to request updated time slots from the control processor.
2. The .AV Framework controller processes the request by synchronizing with the connected calendaring service and calculating new reservation options.
3. Reservation options are transmitted to the panel as **ReserveNowOption** components, and the **OptionsCount** attribute of **ReserveNow** component is updated.
4. The touch screen renders the reservation options to the user.
5. The user selects the desired reservation option, and invokes the **ReserveNowOption** command associated with the option in the list to initiate the reservation.
6. The controller requests the new time slot from the remote calendaring service. At this time, the **RoomScheduler** will change the **IsBusy** flag to true.
7. When the controller has completed the request, joins indicating the updated flags and schedule are reflected in the **RoomScheduler**, and the **IsBusy** flag value reverts to false.