import qrcode
import image
qr = qrcode.QRCode(
    version=15,  
    box_size=10, 
    border=5,
)
data = "https://www.youtube.com/watch?v=onHPipeASdk&list=PLpp8-k7G_6Y3Wj1suZQ-9lATFzFuGw93x&index=1"

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("sample.png")

print("QR Code generated and saved as 'qr_code.png'")
