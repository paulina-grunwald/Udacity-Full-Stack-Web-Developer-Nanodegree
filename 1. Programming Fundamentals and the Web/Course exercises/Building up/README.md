# Key Learning Points Form Media Query

- Responsive website will adjust depending on the characteristics of device on which is viewed. Responsive website will apply different styles for different devices.
- Media Query will allow to selectively apply CSS design.
- style sheet: <link rel="stylesheet" href="styles.css">
- This media view query will apply only if the viewport is wider than 500px:
 ``<link rel="stylesheet" media="screen and (min-width:500px)" href="over500.css">
 ``
- Media query can be also emmbeded in @media tag e.g
  ```
  @media screen and (min-width:500px) {
    body { background-color: green; }
  }
  ```
- There are advantages and disadvantages of used linked CSS and @ media. Linked CSS will execute many small http requests but @media will execute few big http requests.

- Media query properties:
  - min-aspect-ratio/max-aspect-ratio
  - min-color/max-color
  - min-width/max-width
  - min-width/max-width
  - min-resolution/max-resolution

- __max-width__ rules are applied anytime when the value specified is less than viewport value.
- It's not recommended to use min-device-width/max-device-width.
- Breakpoints should be found in relation to content.


## References:
- https://css-tricks.com/css-media-queries/
