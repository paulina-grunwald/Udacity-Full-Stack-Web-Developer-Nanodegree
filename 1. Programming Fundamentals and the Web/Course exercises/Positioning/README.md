# Key Learning Points Form Positioning

- The default position in CSS is __static__ (also called normal flow). The relative, absolute and fixed flows are variations of the normal flow.
- Block elements are laid out vertically. Their left outer edges will line up with their parent’s left outer edges. Even though these blocks do not take up the full width of the page, they still stack.
- Inline elements are laid out horizontally inside their parents. The left edge of an element’s line box will touch the right edge of the preceding element’s line box.
- __display: inline-block__ elements can be sized like block elements but are laid out like inline elements.
-  whitespace, the newline and the tab, between the .child elements is turned into an __anonymous box__. Anonymous boxes arise in situations where there is a mix of block and inline elements inside a container. In the example.
-  __Relative flow__ is a variant of normal flow but it allows to shift the position of the element after they have been laid out in the normal flow. That means we can define relative position of element in the normal flow by specfying top, bottom, left and right distance from the end of the container.
