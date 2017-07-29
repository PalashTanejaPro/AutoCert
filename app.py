from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from flask import redirect,Flask, request

img = Image.open("certitemplate.jpg")
draw = ImageDraw.Draw(img)
app = Flask(__name__)
Name = ""
School = ""
event=""

@app.route('/data')
def data():
	Name = request.args.get('name')
	School = request.args.get('school')
	event = request.args.get('event')
	print Name
	print School
	print event
	selectFont = ImageFont.truetype("Font.ttf", size = 70)
	draw.text( (1050,1500), Name, (0,0,0), font=selectFont )
	draw.text( (1050,1830), School, (0,0,0), font=selectFont )
	draw.text( (1050,2170), event, (0,0,0), font=selectFont )
	img.save( 'static/certi.pdf', "PDF", resolution=100.0)
	return redirect('/static/certi.pdf') 
#Name="Palash Taneja"
#School = "DPS Rohini"
#event = "Programming"

app.run()

