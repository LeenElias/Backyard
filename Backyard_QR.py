import qrcode
from PIL import Image

# Generate QR code
qr = qrcode.QRCode(
    version=2,  # Adjust based on size needed
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
    box_size=10,
    border=4,
)
qr.add_data("https://backyard.menus.run/")
qr.make(fit=True)

# Create the QR code image
qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Load the logo image
logo = Image.open("backyardlogo.jpg")

# Resize logo
qr_width, qr_height = qr_img.size
logo_size = int(qr_width * 0.15)  # logo will be 25% the width of the QR
logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

# Calculate position and paste logo
pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
qr_img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)

# Save the final image
qr_img.save("backyard_QR.png")
