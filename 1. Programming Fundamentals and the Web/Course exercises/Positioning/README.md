# Key Learning Points Form Positioning

- The default position in CSS is __static__ (also called normal flow). The relative, absolute and fixed flows are variations of the normal flow.
- __< div>s (block elements)__ stack vertically while the __< span>s (inline elements)__ stack horizontally.
- __Block elements__ are laid out vertically. Their left outer edges will line up with their parent’s left outer edges. These blocks do not take up the full width of the page but they still stack.
- __Inline elements__ are laid out horizontally inside their parents. The left edge of an element’s line box will touch the right edge of the preceding element’s line box.
- __display: inline-block__ elements can be sized like block elements but are laid out like inline elements. It behaves as an inline element with the sizing behaviours of the block element.

  ```
  .example {
  display: inline-block;
  }
  ```
- The relative positioning of block and inline elements is not actually determined by the element __display__ property but by the formatting context which is influenced by the siblings of the element.
-  Whitespace, the newline and the tab, between the .child elements is turned into an __anonymous box__. Anonymous boxes arise in situations where there is a mix of block and inline elements inside a container. __Anonymous box__ generation is used to deal with cases where a parent element contains a mixture of inline-level and block-level child elements (in which case "anonymous block boxes" are generated) and with cases where the markup contains inline-level elements mixed with surrounding text (in which case "anonymous inline boxes" are generated), such as an em or i tag inside a paragraph of text.


- CSS defines three positioning schemes, which are:
  - __normal flow__, which consists of three formatting contexts: the block, inline and relative formatting contexts
  - __floats__, which interact with normal flow in their own way and form the basis of most modern CSS grid frameworks
  - __absolute positioning__, which deals with absolute and fixed elements relative to the normal flow.

-  __Relative flow__ is a variant of normal flow but it allows to shift the position of the element after they have been laid out in the normal flow. That means we can define relative position of element in the normal flow by specifying top, bottom, left and right distance from the end of the container.

  ```
  .relative {
    position: relative;
    top: 10px;
    left: 10px;
  }
  ```

- shift can move blocks by specified px distance.
  ```
  .shift {
    /*position: relative;*/
      top: 10px;
      left: 10px;
  }
      ```

- __nth-child(n) selector__ matches every element that is the nth child, regardless of type, of its parent. e.g

  ```
  p:nth-child(odd) {
      background: red;
    }

    p:nth-child(even) {
      background: blue;
    }
    ```



### References:
- Udacity Full Stack Developer Nanodegree: Postining course
-http://book.mixu.net/css/1-positioning.html#anonymous-box-generation
- https://www.w3.org/TR/CSS2/visuren.html#anonymous-block-level
