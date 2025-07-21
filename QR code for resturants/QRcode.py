import qrcode


data = input("Provide the url")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)   
img = qr.make_image(fill_color="black", back_color="white")
img.save("MYQRcode.png")

print("QR code generated and saved as MYQRcode.png")
print("You can scan the QR code to retrieve the data.")




