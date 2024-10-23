import qrcode

data = input('Enter the text or URL: ').strip()
filename = input('Enter the filename by which name you want to save your QR code: ').strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)
print(f'QR code saved as {filename}')



# ANOTHER METHOD
import qrcode
from PIL import Image

data = input('Enter the text or URL: ').strip()
filename = input('Enter the filename (including extension, e.g., qr.png): ').strip()

# Create the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Customize the QR code
image = qr.make_image(fill_color='blue', back_color='white')

# Add a logo
logo = Image.open('v.png')  # Make sure logo.png is in the same directory
basewidth = 60  # Adjust to fit your QR code size
wpercent = (basewidth / float(logo.size[0]))
hsize = int((float(logo.size[1]) * float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.LANCZOS)

pos = (
    (image.size[0] - logo.size[0]) // 2,
    (image.size[1] - logo.size[1]) // 2,
)
image.paste(logo, pos)

# Save the final QR code
image.save(filename)
print(f'QR code saved as {filename}')
