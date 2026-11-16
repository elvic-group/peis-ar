"""Usage: python make_qr.py https://din-adresse/  -> writes qr_peis.png (print-ready, 1200 px)."""
import sys, qrcode
url = sys.argv[1]
img = qrcode.make(url, box_size=30, border=3, error_correction=qrcode.constants.ERROR_CORRECT_M)
img.save("qr_peis.png"); print("wrote qr_peis.png for", url)
