# Key Learning Points Form Media Query

- __Responsive website__ will adjust depending on the characteristics of device on which is viewed. Responsive website will apply different styles for different devices.
- __Media Query__ will allow to selectively apply CSS design.
- __Style sheet__: <link rel="stylesheet" href="styles.css">
- This media view query will apply only if the viewport is wider than 500px:
 ```CSS
 <link rel="stylesheet" media="screen and (min-width:500px)"
 href="over500.css">
 ```
- Media query can be also emmbeded in @media tag e.g
  ```CSS
  @media screen and (min-width:500px) {
    body { background-color: green; }
  }
  ```
- There are advantages and disadvantages of used linked CSS and @ media. Linked CSS will execute many small http requests but @media will execute few big http requests.

- __Media query properties__:
  - min-aspect-ratio/max-aspect-ratio
  - min-color/max-color
  - min-width/max-width
  - min-width/max-width
  - min-resolution/max-resolution

- __Max-width__ rules are applied anytime when the value specified is less than viewport value.
- It's not recommended to use min-device-width/max-device-width.
- __Breakpoints__ should be found in relation to content.
- __Grid fluid system__ -
- __Flexbox__ -
- __display: flex;__
- __flex-wrap: wrap;__ (elements will wrap to the next line)



## References:
- https://css-tricks.com/css-media-queries/
- https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Basic_Concepts_of_Grid_Layout
