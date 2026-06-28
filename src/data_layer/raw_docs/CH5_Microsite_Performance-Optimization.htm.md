

# Crestron Template Project Performance Optimization

The applications created using Crestron CH5 libraries can be run on various touch and mobile devices that have limited hardware capabilities. As a best practice, the project should be optimized to improve the application loading time and for smoother performance.

For example, the <ch5-triggerview> component loads all the triggerview child components up front, which helps to navigate faster between the pages. Additionally, certain components such as <ch5-dpad> and <ch5-keypad> require more project resources than components such as <ch5-button>, so designers must take the complexity of each component into consideration.

The following sections describe performance considerations that designers should take into account when using the Crestron Template Project. Factors for improving the performance of a project are also described.

## Weighted Coefficients for Components

Crestron has tested and developed a weighted coefficient value for each CH5 component.

The following table lists the weighted coefficient value for each CH5 component. These values can be used a guideline when using the Crestron Template Project to help ensure CH5 projects perform optimally.

NOTE: Custom attributes such as widgets and containers are not weighted, as their content and weight on the project will vary. Projects with custom attributes should be tested thoroughly to ensure proper performance.

| Component Name | Weighted Coefficient |
| --- | --- |
| Advanced Button (25 modes) | 5 |
| Animation Object | 1 |
| Background (640x320) | 22 |
| Background (1920x1200) | 25 |
| Button | 1 |
| CH5 Jointotext Boolean | 0.5 |
| CH5 Jointotext Numeric | 0.5 |
| Color Chip | 1 |
| Color Picker | 2 |
| D-Pad | 8 |
| Data CH5 Show | 1 |
| Date and Time | 1 |
| Empty Page | 8 |
| Formatted Text | 1 |
| Form | N/A |
| Image (800x800) | 1 |
| Import HTML Snippet | 1 |
| Keypad | 37 |
| List | 15 |
| Modal Dialog | 6.5 |
| Overlay Panel | 2 |
| QR Code | 1 |
| Segmented Gauge | 1.5 |
| Select | 12 |
| Signal Level Gauge | 1 |
| Slider | 1.5 |
| Spinner | 6 |
| Tab Button | 1 |
| Template | 1 |
| Text Input | 1 |
| Toggle | 1 |
| Triggerview | 1 |
| Video Switcher | 55 |
| Wi-Fi® Signal Level Gauge | 1 |

NOTE: When using CH5 button lists and subpage reference lists, coefficients are not provided because of the complexity of these controls. Avoid using more than two of these components when possible on the same page and test for performance.

## Limit Components

Avoid using too many components in a single page. You can load roughly 50 weighed components in a page and 600 weighted components in a project for smoother performance. For example, a project with 15 pages should have an average of up to 40 weighted components per page using these guidelines. Refer to [Weighted Coefficients for Components](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/Performance-Optimization.htm#Weighted_Coefficients_for_Components) for more information.

## Avoid Large DOM Size

Avoid creating a large DOM tree or nesting DOM nodes too deep, as this can cause runtime performance issues. Having an excessive DOM tree within a project affects the performance of HTML applications, as the browser must perform more complex operations to load the project pages. This can cause increased memory and CPU usage, slow page loading times, and suboptimal page rendering.

It is recommended that project pages should contain no more than 1500 DOM elements. Additionally, the DOM depth of a page should be less than 32 with no more than 60 child/parent elements.

## Application Initialization and Startup

The average time that it takes a base CH5 template project to initialize and start is 9 to 15 seconds after the CH5 application is started by the device firmware. There is no exact formula to determine the increase in startup time relative to the weighted coefficient total of project components. However, designers should expect that the startup and initialization time of a CH5 template project should not exceed 20 seconds as long as the weighted coefficient value of the project is 600 or less. Other factors, such as the DOM tree structure and complexity of CSS styles, also can affect the load and rendering times of a project.

## Unsubscribe Subscriptions

Subscribe to observers whenever required. You can unsubscribe observers that are used to fetch information only once. (For example: count, flags, and so forth).

**Example:**

Copy

```
// Subscribe to join

var selectedSubscription = CrComLib.subscribeState('n', JOIN_NAME, function () {

// Add your code

});

// Unsubscribe join

CrComLib.unsubscribeState('n', JOIN_NAME, selectedSubscription);
```

## Debug

Exceptions are one of the best ways to identify bugs and even performance problems in your code. Additionally, console logging should be filtered and turned off by default. It can be turned on during development.

As you continue to make changes to your application and roll out new features, its usage and performance will continue to change and needs to be monitored regularly.

The recommendations above are different from some of the other best practices in this section.

## Page Preload and Caching

As of the CH5 2.0 release, two new **preloadPage** and **cachePage** options are available within the **project-config.json file** at the template project page level. These options enhance the application behavior and performance.

- Caching is a feature supported by web browsers that allows content to be made immutable when a page is refreshed. This allows the browser to retain elements such as JavaScript, images, fonts, and stylesheets between page reloads. Designers should consider turning on caching for large pages that contain a component weighted coefficient value of 25 or more as described in [Weighted Coefficients for Components](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/Performance-Optimization.htm#Weighted_Coefficients_for_Components). Cache content is stored in memory, so memory availability should also be taken into consideration when caching since the desired result may not be possible if the project is too large. Refer to [Avoid Large DOM Size](https://sdkcon78221.crestron.com/sdk/Crestron_HTML5UI/Content/Topics/Best-Practices/Performance-Optimization.htm#Avoid_Large_DOM_Size) for more information.
- Page preload is a feature that tells the browser how content should be loaded when the page loads. This allows the browser to prioritize loading resources more accurately. Page preload can slow down the load time of a page, but it provides a better user experience. Preloading a page does not cache the page automatically, so it is recommended that pages should be both preloaded and cached for an optimal user experience.

Copy

```
"pages": [\
    {\
        "pageName": "page1",\
        "fullPath": "./app/project/components/pages/page1/",\
        "fileName": "page1.html",\
        "cachePage": false,\
        "preloadPage": false,\
        "standAloneView": false,\
        "navigation": {\
            "sequence": 1,\
            "label": "menu.page1",\
            "isI18nLabel": true,\
            "iconClass": "fas fa-file-alt",\
            "iconUrl": "",\
            "iconPosition": "bottom"\
        }\
    }\
]
```

These options are embedded to the project-config.json file (at the page level) when npm run generate:page is issued to create a page:

- **preloadPage**: A Boolean that determines the preloading behavior for the page. The default value is false.
  - If true, the specified page is preloaded when the project starts.
  - If false, the specified page is not preloaded and will only load when a user navigates to the page.

- **cachePage**: A Boolean that determines the caching behavior for the page. The default value is false.
  - If true, the specified page is cached after the page is loaded and will remain cached in the project.
  - If false, the specified page is removed from the cache whenever a user leaves the page. The page is reloaded whenever a user revisits it.

To optimize project performance, identify the pages that are most frequently utilized, that contain many components, or that must be immediately available at application start up. Then, apply the **preloadPage** and **cachePage** options to these pages as needed to decrease load time or to provide a responsive user experience.

NOTE: For optimal performance when using CH5 button lists and subpage reference lists, ensure **cachePage** is set to true.

## Image Considerations

The images used within a project can affect its overall performance. Image-related factors that affect performance include the image size, location (embedded in the project or external to it), and the external connection speed. Avoid using large images with resolutions higher than your deployment screen's resolution, and compress images when possible.

As an example, a 640 x 360 background image with a size of 53kb will load four times faster than a 2560 x 1440 background image with a size of 249kb from the same remote source.

## Reference Material

Refer to the following reference documents for more information on performance optimization.

- [web.dev/dom-size](https://web.dev/dom-size)
- [chrome.google.com/webstore/detail/dom-size-analyzer/mcneiimlodlbmohipgdbbglgbmaoojen](https://chrome.google.com/webstore/detail/dom-size-analyzer/mcneiimlodlbmohipgdbbglgbmaoojen)
- [web.dev/reduce-the-scope-and-complexity-of-style-calculations/](https://web.dev/reduce-the-scope-and-complexity-of-style-calculations/)