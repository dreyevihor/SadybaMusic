import qrcode
from PIL import Image, ImageDraw, ImageFont
import json
from cryptography.fernet import Fernet

key = b'RLQHMwbjOj4ztWwPTkDTqBd3YYtF-g7S4W8bX4OItS8='
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(b"A really secret message. Not for prying eyes.")
plain_text = cipher_suite.decrypt(cipher_text)


def add_some_text(templ, obj_props, obj_value):
	font = ImageFont.truetype('../static/fonts/Times_New_Roman_Normal.ttf', 20)
	width, height = templ.size
	obj = Image.new('RGBA', (40, 18), (255,255,255,255))
	obj_dr = ImageDraw.Draw(obj)
	obj_dr.text((0, 0), str(obj_value), font=font, fill=(0, 0, 0, 255))
	if obj_props['isRotated']:
		templ.paste(obj.rotate(90, expand=1), (int(obj_props['left']*width), int(obj_props['top']*height)))
	else:
		templ.paste(obj, (int(obj_props['left']*width), int(obj_props['top']*height)))
	return templ

def add_qr(templ, qr_props, qr_value):
	qr_code = qrcode.make('test')
	width, height = templ.size
	qr_width = qr_props['width']*width
	qr_height = qr_props['height']*height
	size = min(qr_width, qr_height)
	if qr_props['isRotated']:
		qr_code = qr_code.rotate(90, expand=1)
	qr_code = qr_code.resize((int(size), int(size)))
	templ.paste(qr_code, (int(qr_props['left']*width), int(qr_props['top']*height)))
	return templ
	

def make_ticket(price_val, row_val, place_val **kwargs):
	qr_props = kwargs.get('barcode_props')
	price_props = kwargs.get('price_props')
	place_props = kwargs.get('place_props')
	row_props = kwargs.get('row_props')
	ticket_template = kwargs.get('ticket_template')
	event_id = kwargs.get('event_id')
	width, height = ticket_template.size

		
	ticket_template = add_some_text(ticket_template, price_props, price_val)
	ticket_template = add_some_text(ticket_template, place_props, row_val)
	ticket_template = add_some_text(ticket_template, row_props, place_val)
	qr_val = {'event': event_id, 'row': row_val, 'place': place_val}
	qr_val = json.dumps(qr_val)
	print(qr_val)
	ticket_template = add_qr(ticket_template, qr_props, qr_val)
	ticket_template.show()
"""
	price = Image.new('RGBA', (40, 18), (255,255,255,255))
	price_dr = ImageDraw.Draw(price)
	price_dr.text((0, 0), str(price_val), font=font, fill=(0, 0, 0, 255))
	if price_props['isRotated']:
		ticket_template.paste(price.rotate(90, expand=1), (int(price_props['left']*width), int(price_props['top']*height)))
	else:
		ticket_template.paste(price, (int(price_props['left']*width), int(price_props['top']*height)))
	


	place = Image.new('RGBA', (40, 18), (255,255,255,255))
	place_dr = ImageDraw.Draw(place)
	place_dr.text((0, 0), str(place_val), font=font, fill=(0, 0, 0, 255))
	if place_props['isRotated']:
		ticket_template.paste(place.rotate(90, expand=1), (int(place_props['left']*width), int(place_props['top']*height)))
	else:
		ticket_template.paste(place, (int(place_props['left']*width), int(place_props['top']*height)))
	


	row = Image.new('RGBA', (40, 18), (255,255,255,255))
	row_dr = ImageDraw.Draw(row)
	row_dr.text((0, 0), str(row_val), font=font, fill=(0, 0, 0, 255))
	if row_props['isRotated']:
		ticket_template.paste(row.rotate(90, expand=1), (int(row_props['left']*width), int(row_props['top']*height)))
	else:
		ticket_template.paste(row, (int(row_props['left']*width), int(row_props['top']*height)))
	


	barcode = code128.image('test')
	barcode_width = barcode_props['width']*width
	barcode_height = barcode_props['height']*height
	if barcode_props['isRotated']:
		barcode = barcode.rotate(90, expand=1)
	barcode = barcode.resize((int(barcode_width), int(barcode_height)))
	ticket_template.paste(barcode, (int(barcode_props['left']*width), int(barcode_props['top']*height)))
	

	ticket_template.show()









"""


import binascii
from Crypto.Cipher import AES
from Crypto import Random

def encrypt(passwrd, message):
    msglist = []
    key = bytes(passwrd, "utf-8")
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    msg = iv + cipher.encrypt(bytes(message, "utf-8"))
    msg = binascii.hexlify(msg)
    for letter in str(msg):
        msglist.append(letter)
    msglist.remove("b")
    msglist.remove("'")
    msglist.remove("'")
    for letter in msglist:
        print(letter, end="")
    print("")

def decrypt(passwrd, message):
    msglist = []
    key = bytes(passwrd, "utf-8")
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    msg = cipher.decrypt(binascii.unhexlify(bytes(message, "utf-8")))[len(iv):]
    for letter in str(msg):
        msglist.append(letter)
    msglist.remove("b")
    msglist.remove("'")
    msglist.remove("'")
    for letter in msglist:
        print(letter, end="")
    print("")

