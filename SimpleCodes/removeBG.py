from rembg import remove
from PIL import Image

input_path = 'dog.jpg'
output_path = 'dog.png'
inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
