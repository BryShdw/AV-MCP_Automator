

# ADA (American Disabilities Act) Compliance

ADA compliance refers to the Americans with Disabilities Act Standards for Accessible Design, which states that all electronic and information technology (such as websites) must be accessible to people with disabilities.

The Americans with Disabilities Act (ADA) was enacted to protect the rights of individuals with disabilities, specifically prohibiting discrimination in employment, public services, public accommodations, and telecommunications.

Beginning January 2018, new ADA regulations for web accessibility went into effect. While organizations cannot be 100% compliant, there are steps that they can take to ensure their sites are accessible to those with disabilities.

## Examples of ADA Compliance

**Review the Website Content Accessibility Guidelines (WCAG 2.0).** These guidelines offer recommendations on how to make your website accessible.

**Conduct an audit of your site using a WAVE Web Accessibility Tool.** The Google Chrome® WAVE Tool is a great tool to look for accessible issues, including missing alt tags, styles, and so forth.

**Make sure your images have descriptive alt tags.** Alt tags are used by screen readers, players, and voiceovers to describe elements on a website to users.

**Review your website’s styles and elements, such as headings, buttons and links.** Keep in mind all types of users who access your website, including those who experience disabilities. For example, if your site’s navigation incorporates lighter, smaller fonts on light backgrounds, this may be illegible for some users.

**Utilize web writing best practices when developing content.** Keeping your website content simple and conversational can help users scan content easier. Using headlines and subheadlines can also help break out content into smaller bites or sections. For abbreviations and acronyms like FBI, include periods between the letters, to help screen readers pronounce them properly.

**Audit your website’s code.** Have a developer review the code and CSS to ensure best practices are being utilized and clean up outdated code.

## Implementation of ARIA in CH5 Application

Every component HTML file starts with the <section>. This <section> tag will have ARIA in it.

Copy

```
<section id="page1-page" class="details-container" aria-labelledby="Page 1">
....
</section>
```

ARIA can be implemented in the CH5 components also. The following sample uses the <ch5-button> component as an example.

For <ch5-button>, ARIA and role can be applied in the following way:

Copy

```
<ch5-button customClass="thumb-btn-{{idx}}" type="text" shape="rectangle"receiveStateSelected="active_state_class_{{idx}}" receiveStateLabel="nav_label_{{idx}}"iconurl="./assets/img/navigation/nav_icon_{{idx}}.svg" iconPosition="bottom"onclick="appModule.navMenu({{idx}})" role="button" aria-label="Open Navigation Menu"aria-pressed="false">
</ch5-button>
```

A user can implement the role attribute for the <nav> HTML tag.

Copy

```
<nav role="navigation" class="navbar navbar-dark navbar-default fixed-top">
....
</nav>
```

The attribute can be implemented in the .scss file.

Copy

```
[role="button"] {
    cursor: pointer;
}
```

## Reference Links

For the more detailed information, refer to the following links:

- [https://webaim.org/techniques/aria/#keyboard](https://webaim.org/techniques/aria/#keyboard)
- [https://www.w3.org/TR/wai-aria-practices-1.1/](https://www.w3.org/TR/wai-aria-practices-1.1/)
- [https://www.csun.edu/universal-design-center/aria-best-practices](https://www.csun.edu/universal-design-center/aria-best-practices)
- [https://www.w3.org/TR/2009/WD-wai-aria-practices-20090224/](https://www.w3.org/TR/2009/WD-wai-aria-practices-20090224/)