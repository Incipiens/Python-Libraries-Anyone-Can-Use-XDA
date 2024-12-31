from PIL import Image, ImageDraw, ImageFont

image = Image.new('RGB', (400, 200), color='blue')
draw = ImageDraw.Draw(image)
draw.text((100, 80), "Hello, World!", fill="white")
image.save('hello_image.png')