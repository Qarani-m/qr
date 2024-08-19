import qrcode

# URL to encode in the QR code
url = "https://qarani-m.github.io/qr/"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
    box_size=10,  # size of each box in the QR code grid
    border=4,  # thickness of the border (number of boxes)
)

# Add the URL to the QR code
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image to a file
img.save("website_qrcode.png")

print("QR code generated and saved as website_qrcode.png")
