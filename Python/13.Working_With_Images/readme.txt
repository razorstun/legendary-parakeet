Working with Images

- pip install pillow - module to work with Images
- pillow is a fork from PIL library so you actuallu import it from PIL
-   from PIL import Image
    mac = Images.open('imagename.jpg')
    mac.size
    mac.filename
    mac.format_description
- Crop the image - computer = mac.crop((x,y,w,h))
- mac.paste(im=computer,box=(x,y))
- mac.resize((w,h))
- mac.rotate(90)
- color tranparency - mac.putalpha(0) will gives white - mac.putalpha(255) wil give completely opeaque
- to mix two color
    -first add tranparency to image - then add the other image to it - blue.paste(im=red,box(x,y),mask=red)
- blue.save("full file path")