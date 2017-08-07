from PIL import Image, ImageDraw, ImageFont

def add_num(img):
	im = ImageDraw.Draw(img)
	myfont = ImageFont.truetype(r'C:/windows/fonts/Arial.ttf',size=40)
	wid,hei = img.size
	im.text((wid-80,0),'899',font=myfont,fill='red')
	
def size_change(img):
	image = img.resize((192*4,108*4))
	return image

if __name__=='__main__':
	image = Image.open(r'C:\Users\Administrator\3c731efa828ba61ec124710a4234970a314e5997.jpg')
	image = size_change(image)
	add_num(image)
	image.save('result.jpg')