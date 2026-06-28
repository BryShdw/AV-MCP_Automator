

# Animation Considerations

Crestron HTML5 runs on certain low-powered embedded devices. Therefore, a CH5 project on these devices will not match the performance of the project on a developer workstation. Developers need to review all animations intended for deployment on an actual device to ensure optimal performance.

JavaScript is an interpreted language with an interpreter in the web browser that parses every line of code at runtime. As a result, JavaScript is slower than native languages. Crestron touch screens also do not have a dedicated GPU (Graphics Processing Unit), so the hardware does not provide the same acceleration required for smooth animations that is possible on a workstation. Therefore, when writing JavaScript for CH5, it is recommended not to create any animations that involve modifying the elements in JavaScript, including the requestAnimationFrame() function.

Using CSS is preferred because it uses native code when using the CPU, and many of the operations will be instead processed by the GPU, which is the ideal processor for graphical elements.

The “transform” CSS style property will best utilize the GPU. This CSS style will create smoother animations than using left/top/bottom/right properties.

- The transform style property has a value of a function that changes the element.
- The transform methods appropriate for most touch screen projects are “2D” transform methods as shown in the table below.

| Function | Description |
| --- | --- |
| matrix(n,n,n,n,n,n) | Defines a 2D transformation using a matrix of six values |
| translate(x,y) | Defines a 2D translation moving the element along the X- and the Y-axis |
| translateX(n) | Defines a 2D translation moving the element along the X-axis |
| translateY(n) | Defines a 2D translation moving the element along the Y-axis |
| scale(x,y) | Defines a 2D scale transformation by changing the element's width and height |
| scaleX(n) | Defines a 2D scale transformation by changing the element's width |
| scaleY(n) | Defines a 2D scale transformation by changing the element's height |
| rotate(angle) | Defines a 2D rotation where the angle is specified in the parameter |
| skew(x‑angle,y‑angle) | Defines a 2D skew transformation along the X- and the Y-axis |
| skewX(angle) | Defines a 2D skew transformation along the X-axis |
| skewY(angle) | Defines a 2D skew transformation along the Y-axis |

## Examples

The following example shows how a slide-out menu can be created using animation best practices.

First, create the menu as shown in sample code below.

Copy

```
 <div class="menu">
    <div id="app-menu" class="app-menu-transform">
         <!—menu content here -->
     </div>
</div>
```

Copy

```
.menu {
    position: fixed;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    pointer-events: none;
    z-index: 150;
}
```

The menu position has the following properties:

- With position:fixed, it is not relative to other elements
- With z-index:150, it is above other elements
- With left:0, top:0, width: 100%, and height: 100%, it overlays its parent container

Next, trigger the animation based on a click event.

Copy

```
var myMenu = document.querySelector(".menu");
function toggleClassMenu() {
    myMenu.classList.add("menu--animatable");
    if(!myMenu.classList.contains("menu--visible")) {
        myMenu.classList.add("menu--visible");
    } else {
        myMenu.classList.remove('menu--visible');
    }
}

myMenu.addEventListener("click", toggleClassMenu, false);
```

The click event triggers the toggleClassMenu() function, which adds a class called “menu--animatable" and toggles the “menu--visible" class to the parent menu element.

Next, define the classes as follows:

Copy

```
/**
  <element class="app-menu-transform">
*/
.app-menu-transform {
    transform: translateX(-103%);
}
/**
    <element class="menu--visible">
…
          <element class="app-menu-transform">

*/
.menu--visible .app-menu-transform {
    transform: none;
}

/**
<element class="menu--animatable">
…
     <element class="app-menu-transform">
*/

.menu--animatable .app-menu-transform {
    transition: all 1000ms linear;
}

/**
<element class="menu--visible menu--animatable">
…
     <element class="app-menu-transform">
*/
.menu--visible.menu--animatable  .app-menu-transform {
    transition: all 1500ms linear;
}
```

The transform: property has a value of function “translateX()”, which glides the element along the X, horizontal axis.

When the ‘menu--visible' class is not in the class list of the menu element, the transform is set to make the element glide off the page to the left (such as translateX(-103%)). When ‘menu--visible' is set in the classlist for the menu, transform: property is set to none, effectively directing the translateX() to be removed.

In all cases, when the menu element has the ‘menu--animatable' class applied, a transition: style is applied to the app-menu element. The time duration is changed based upon the menu opening onto the visible view or closing out off the visible view. The ‘transition’ property directs the updated transform property to be applied over a duration of time, 1000 or 1500ms, and by what timing (aka easing) function.

Lastly, our animation was triggered by adding class ‘menu--animatable' to the menu element. To trigger the animation again, we need to remove the class.

This is accomplished with the JavaScript code shown below to remove the class on the “transitionend” event triggered when the transition completes.

Copy

```
function OnTransitionEnd() {
    myMenu.classList.remove("menu--animatable");
}

myMenu.addEventListener("transitionend", OnTransitionEnd, false);
```

## Resources

The following additional resources are recommended for working with CSS animations:

- [www.w3schools.com/css/css3\_2dtransforms.asp](https://www.w3schools.com/css/css3_2dtransforms.asp) \- For 2D transformation properties
- [https://easings.net/](https://easings.net/) \- For timing functions
- [https://developer.mozilla.org/en-US/docs/Web/CSS/animation-timing-function](https://developer.mozilla.org/en-US/docs/Web/CSS/animation-timing-function) \- For timing functions
- [https://www.w3schools.com/cssref/css3\_pr\_animation-timing-function.asp](http://www.w3schools.com/cssref/css3_pr_animation-timing-function.asp) \- For timing functions
- [https://medium.com/outsystems-experts/how-to-achieve-60-fps-animations-with-css3-db7b98610108](https://medium.com/outsystems-experts/how-to-achieve-60-fps-animations-with-css3-db7b98610108) \- General resource for CSS animations