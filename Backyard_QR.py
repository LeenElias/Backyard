import qrcode
data="http://backyard.menus.run/"
img=qrcode.make(data)
img.save("BackyardQR.png")