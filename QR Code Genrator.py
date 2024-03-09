import qrcode

qr_code_genrate = input('Enter a Text > ')
img = qrcode.make(qr_code_genrate)
img.save(qr_code_genrate)
