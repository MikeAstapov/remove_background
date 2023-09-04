from rembg import remove
from PIL import Image

input_path = 'P2YjZWzsyZA.jpg'
output_path = 'out23.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)