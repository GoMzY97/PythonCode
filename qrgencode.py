import qrcode
from PIL import Image

#data u want to encode in the qr code 
data ="https://x.com/clcoding"

#Genertae QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

#Create an image from the qr code
image = qr.make_image(fill="black", back_color="white")

#save the image 
image.save("qr_code.png")
Image.open("qr_code.png")

