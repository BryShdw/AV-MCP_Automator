

# TriggerView

The <ch5-triggerview> component is a container component used to group content. Each content item will be wrapped inside of a <ch5-triggerview-child> component. Only one ChildView will be visible at any give time.

For interactive examples using the <ch5-triggerview> component and CSS classes, refer to the [Showcase Application](https://sdkcon78221.crestron.com/downloads/ShowcaseApp/ch5-triggerview/endless.html).

## Features

The <ch5-modal-dialog> attributes provide the following features:

- Determines whether the first ChildView will be shown after the last ChildView to create an endless sequence.
- Determines whether gesturing will be supported, which changes the behavior inside the component.
- Determines the active view using a 0-based index.
- Selects a ChildView based on received control system state.
- Sends the index of the currently-visible item to the control system.

## Design Considerations

When using multiple <ch5-triggerview-child> subcomponents within a <ch5-modal-dialog> component, all TriggerView children will be displayed (instead of one at a time) if not all application resources have been downloaded first.

To prevent this, use the load event from the window as shown in the following example code:

Copy

```
const overlay = document.createElement('div');
overlay.className = 'overlay';

document.body.appendChild(overlay);

window.addEventListener('load', () => {
    overlay.remove();>
})
```

* * *

The <ch5-modal-dialog> component can be used outside of the <ch5-triggerview> component by placing it at the bottom of the app.component.html file. The dialog can then be triggered from any location in the project.

Refer to the following sample code:

Copy

```
<section class="main-selection">
    <app-header (valueChange)="getHeaderEvent($event)"></app-header>
    <ch5-triggerview class="main-swiper" [attr.activeView]="activeIndex" gesturable="true" endless = "false">
        ....
    </ch5-triggerview>
    ...
</section>

<!-- All CH5 modal dialogs -->
<ch5-modal-dialog receiveStateShowPulse="trigger_1"><p>Sample text</p></ch5-modal-dialog>
<ch5-modal-dialog receiveStateShowPulse="trigger_2"><p>Sample text</p></ch5-modal-dialog>
<ch5-modal-dialog receiveStateShowPulse="trigger_3"><p>Sample text</p></ch5-modal-dialog>
```

* * *

Standard-issue Angular uses {{ variable }} in HTML markup to allow the markup to display a value of the variable in the typescript/JavaScript. HTML5 UI also uses the double mustache {{ index }} as a counter in lists. However, Angular can be directed not to interpret the {{ }} and to leave them for interpretation by HTML UI via the [ngNonBindable directive](https://ngrefs.com/latest/templates/ngnonbindable "https://ngrefs.com/latest/templates/ngnonbindable").

Refer to the sample code below from the Showcase Application as an example:

Copy

```
<!--When using a computed property <b>{{ idx }}</b>, Angular tries to process it as an embedded expression, adding ngNonBindable to the template will force Angular to ignore it.-->

<ch5-list id="demo-list-1" size="500" maxHeight="400px" indexId="idx">
    <template ngNonBindable>
        <div class="horizontal-list-item">
            <span>item_{{idx}}</span>
        </div>
    </template>
</ch5-list>
```