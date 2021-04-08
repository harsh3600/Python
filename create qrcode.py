import qrcode

qr = qrcode.QRCode(
	version = 1,
	box_size = 20,
	border = 10)

data = "https://github.com/harsh3600"
#In data you can add your data to be added in qrcode

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill="black",back_color="white")
img.save("QR.png")
