

# Slow Mode (CH5 CLI Deploy)

Crestron provides the CH5 CLI utilities to allow Crestron HTML5 User Interface developers to distribute projects to touch screens and other devices without having to switch applications to Crestron Toolbox™ software. For more information on the CH5 CLI utilities, refer to [Build a Crestron Template Project](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Deploy-Project.htm).

Occasionally, CH5 CLI fails to upload and deploy a project to a touch screen because of an intermittent failure.

The failure will appear as follows when running the command:

Copy

```
C:\project-directory >ch5-cli deploy -H 1.1.1.1 -t touchscreen dist/prod/project_name.ch5z
Connected to device. Uploading archive file.
Trying to upload file to display/project_name.ch5z.
Closing sftp connection.
Error: Error on connection to 1.1.1.1:  put: Permission denied display/project_name.ch5z. No success executing command.
```

To work through this error, use the slow mode option, which uploads the file at a slower speed. Append --slow mode or -s to the ch5-cli deploy command to run slow mode while deploying a project.

The status will indicate that slow mode is being run as follows:

Copy

```
C:\project-directory >ch5-cli deploy -H 1.1.1.1 -t touchscreen dist/prod/project_name.ch5z --slow-mode
Connected via ssh to device
Device output:

Device output:

TSW-1070>
Connection closed.
Connection has ended. Success executing command.
Connected to device. Uploading archive file.
Trying to upload file to display/xpanel_test.ch5z.
Uploaded file.
Closing sftp connection.
Sending reload command to touchscreen device:projectload
Connected via ssh to device
Device output:

Device output: Installing User Project, Please wait...

Device output: Success. Restarting UI...

Device output:

Device output:
TSW-1070>
Connection closed.
Connection has ended. Success executing command.
```