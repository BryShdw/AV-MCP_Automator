

# BEM (Block, Element, Modifier)

The BEM (Block, Element, Modifier) methodology is a popular naming convention for classes in HTML and CSS that is recommended for use in the Crestron Template Project.

CSS can be written in the BEM style as shown below:

Copy

```
/* Block component */
.ch5 - custom - select {} /* Element that depends upon the block */ .ch5 - custom - select {
  .ch5 - select__main {
    padding: 0.5 rem 1 rem;color: inherit;
  }
} /* Modifier that changes the style of the block */ .ch5 - button--icon {
  font - size: 1.5 rem;
}
```

In the above example, .ch5-custom-select { } is the block (the top-level abstraction). Elements can be placed inside, and these are denoted by two underscores, such as with .ch5-select\_\_main { }. Modifiers can manipulate the block so that one can theme or style that particular component without inflicting changes on a completely unrelated module. This can be written as .ch5-button--icon { }.

HTML can be written using BEM as follows:

Copy

```
<ch5-select class="ch5-custom-select">
    <template>
        <ch5-select-option class="ch5-button--icon">
        </ch5-select-option>
    </template>
</ch5-select>
```

## Importance of BEM

- BEM provides a modular structure to your CSS project.
- BEM also provides a relationship between CSS and HTML.
- BEM allows you to modify the behavior of the block and its representation in HTML in the same declarative way like in CSS.

## Why Should I Use BEM?

BEM fixes the two biggest problems with regular CSS:

- **Inheritance**: BEM avoids CSS inheritance and provides some sort of scope by using unique CSS classes per element.
- **Specificity**: BEM reduces style conflicts by keeping CSS specificity to a minimum.

## Benefits of BEM

- By avoiding use of HTML element names in CSS selectors, BEM makes CSS code readily portable to a different HTML structure.
- BEM encourages front end developers to create a flat CSS structure with no nested selectors. So the less browsers have to evaluate, the faster they can render.
- BEM avoids CSS conflicts by using unique contextual class names for every block, element, and modifier combination.
- BEM's modular approach encourages developing independent modules of code and hence easier to maintain & update without affecting other modules in the project.