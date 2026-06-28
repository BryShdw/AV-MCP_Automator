

# Build a Crestron Template Project

The following topics describe how to build, deploy, and archive a Crestron Template Project to run in a web browser or on a touch screen.

## Build Commands

NPM scripts are used to build a project. The following scripts are provided in the Crestron Project Template (package.json) file.

NPM Scripts

![](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Resources/Images/CH5_Install_and_Sample_Project_Setup_4.jpg)

- clean: Removes the prior build output.
- start: Used to see continuous updates as the project is saved. Runs the project in a browser as a live server each time the file is saved.
- build:prod: Creates a performance-optimized output suitable for production deployment.
- build:archive: Creates a CH5 project archive (.ch5z) file using the ch5-cli archive command. Parameter changes and documentation for using the ch5-cli archive utility are located at [Create and Deploy CH5 Archives](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/UI-CH5-Archives.htm).
- build:deploy: Deploys the project archive to a touch screen or control system using the ch5-cli deploy command. Parameter changes and documentation for using the ch5-cli deploy utility are located at [Create and Deploy CH5 Archives](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/UI-CH5-Archives.htm).

  - At a minimum, the “-H hostname” parameter will need to be changed to actual hostname or IP address of your touch screen or control system.
  - Adding parameters to this command for passing credentials to access the Crestron device will be required in many cases.
  - To deploy to more than one device, duplicate the build:deploy description with an new name (such as build:deployweb) and modify as necessary.

- build:onestep: Executes build:prod, build:archive, and build:deploy sequentially for one step deployment.

## One-Step Deployment

Building, archiving, and deploying a CH5 project is a simple one-step process. The following script will chain the results of build:prod, build:archive, and build:deploy. A failure of any of these scripts will result in an error.

Copy

```
npm run build:onestep
```

## Production Build

Issue npm run build:prod to build the project in production mode. The build artifacts will be stored in the 'dist/' directory. The production build will minify the JavaScript and CSS files.

The production build runs in production mode on the devices. The production build runs uglify and builds your source files into one or multiple minified files. The source map files that maps the transformed source to the original source are not included.

## Deploy a Project

The deploy command builds the project that can then be deployed on a touch screen.

The host name or IP address of the touch screen must be added in package.json as shown in the example code below:

Copy

```
"build:deploy": "ch5-cli deploy -H <hostname> -t touchscreen dist/<ch5-sample-project>.ch5z"
```

The option -p must be included to prompt for a user name and password for devices where authorization is enabled.

Copy

```
"build:deploy": "ch5-cli deploy -H <hostname> -p -t touchscreen dist/<ch5-sample-project>.ch5z"
```

## Archive a Project

Issue npm run build:archive to archive a project.

The app can be distributed by archiving your application, which then can be readily deployed on supported touch screens and control systems (for the HTML5 Web XPanel functionality). The archive utility helps to compile, compress, and bundle the required files to run the application on the device. The build artifacts are stored in the **dist/** directory. The archive file is a zip file that has a ".ch5z" extension and consists of ".ch5" and a manifest JSON file. The generated archive file should not be renamed. However, the archive file can be renamed by modifying the default name "shell-template" as the -p parameter of the ch5-cli archive command.

## Run in Browser

Issue npm run start to compile and launch a webserver to host the project in the default desktop web browser.

The default hostname is "localhost" and the default port number is "3000". Any changes to source code will be "watched," and the project will be recompiled and the browser will update automatically. Chrome or Safari browsers are preferred.

NOTE: Changes to the project structure, including adding pages or widgets, and changes project configuration require a restart of this command to properly pick up the change.

## Export a Project

The user can export the project excluding the directories like node\_modules and dist, which are installed during project setup and build. This reduces the file size and makes it easy to share the project.

To export the project, go to the command prompt or terminal of the template project and execute npm run export:project.

By default, the zip file is created inside the project dist folder. This file has the naming convention of {fileName}.zip. The filename is picked from 'name' parameter in package.json file.