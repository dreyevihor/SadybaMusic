import qrcode
from PIL import Image, ImageDraw, ImageFont
import os, json, random, shutil
from cryptography.fernet import Fernet
import weasyprint

from SadibaMusic import settings

key = b'RLQHMwbjOj4ztWwPTkDTqBd3YYtF-g7S4W8bX4OItS8='
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(b"A really secret message. Not for prying eyes.")
plain_text = cipher_suite.decrypt(cipher_text)


def add_some_text(templ, obj_props, obj_value):
	font = ImageFont.truetype('/home/ihor/Documents/sadyba-music/SadibaMusic/Tickets/Times_New_Roman_Normal.ttf', 20)
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
	qr_code = qrcode.make(qr_value)
	width, height = templ.size
	qr_width = qr_props['width']*width
	qr_height = qr_props['height']*height
	size = min(qr_width, qr_height)
	if qr_props['isRotated']:
		qr_code = qr_code.rotate(90, expand=1)
	qr_code = qr_code.resize((int(size), int(size)))
	templ.paste(qr_code, (int(qr_props['left']*width), int(qr_props['top']*height)))
	return templ
	

def make_ticket(price_val, row_val, place_val, **kwargs):
	qr_props = kwargs.get('barcode_props')
	price_props = kwargs.get('price_props')
	place_props = kwargs.get('place_props')
	row_props = kwargs.get('row_props')
	ticket_template = kwargs.get('ticket_template')
	event_id = kwargs.get('event_id')

		
	ticket_template = add_some_text(ticket_template, price_props, price_val)
	ticket_template = add_some_text(ticket_template, place_props, row_val)
	ticket_template = add_some_text(ticket_template, row_props, place_val)
	qr_val = {'event': event_id, 'row': row_val, 'place': place_val}
	qr_val = json.dumps(qr_val)
	print(qr_val)
	ticket_template = add_qr(ticket_template, qr_props, qr_val)
	return ticket_template


def create_folder(event_id):
	while True:
		folder_name = 'temporary_' + str(event_id) +'_'+ str(random.randint(1, 10000))
		folder = os.path.join(settings.MEDIA_ROOT, folder_name)
		if not os.path.exists(folder):
			os.makedirs(folder)
			return folder

def folder_to_html_file(path):
	html = '''
		<html>
    <head>        
    </head>
    <body style="margin: 0; padding: 0;">
	'''

	for img in os.listdir(path):
		if img.endswith('.jpg') or img.endswith('.png'):
			html_img = '<img src="{0}" alt="" style="width: 124%; height: auto; margin-bottom: 20px; margin-left: -12%;">\n'.format(os.path.join(path, img))
			html+=html_img

	html += '''
				</body>
			</html>	
			'''
	with open(os.path.join(path, 'pdf.html'), 'w') as file:
		file.write(html)
		file.close()
	return os.path.join(path, 'pdf.html')

def html_to_pdf(html_file, event_id):
	path = os.path.join(settings.MEDIA_ROOT, 'tickets/')
	pdf_name = path + 'tickets_' + str(event_id)+ '_' +str(random.randint(1, 10000)) +'.pdf'
	weasyprint.HTML(html_file).write_pdf(str(pdf_name))
	return(pdf_name)


def clear_folder(path):
	shutil.rmtree(path, ignore_errors=True)


def generate_tickets(rows, **kwargs):
	qr_props = kwargs.get('barcode_props')
	price_props = kwargs.get('price_props')
	place_props = kwargs.get('place_props')
	row_props = kwargs.get('row_props')
	ticket_template = kwargs.get('ticket_template')
	event_id = kwargs.get('event_id')
	tmp_dir = create_folder(event_id)
	for row in rows:
		for place in range(int(row['place_from']), int(row['place_to'])):
			img = make_ticket(
				price_val = row['price'],
				row_val = row['row'],
				place_val = 20,
				event_id = event_id,
				barcode_props = qr_props,
				place_props = place_props,
				price_props = price_props,
				row_props = row_props,
				ticket_template = ticket_template
			)
