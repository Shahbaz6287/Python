# 1st project as qrcode
import qrcode as qr
img = qr.make("https://accounts.pwskills.com/login?domain=pwskills.com&redirectUrl=%2F")
img.save("pw skills.png")


# 2nd project as Qrcode
# import qrcode


# qr=qrcode.QRCode(version=1,
#                 error_correction=qrcode.constants.ERROR_COTRRECT_H,
#                  box_size=10, border=4,)
# qr.add_data("https://www.wscubetech.com/")
# qr.make(fit=True)
# img=qr.make_image(fill_color="gray", back_color="green")
# img.save("wscube_web.png")