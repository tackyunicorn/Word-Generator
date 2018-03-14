import urllib3
from bs4 import BeautifulSoup
from PIL import Image , ImageDraw , ImageFont
import random

# Specify size of dataset here
size = 10

# Get dictionary words from the url and parse it into a list WORDS
url = 'https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain'
http = urllib3.PoolManager()
response = http.request('GET' , url)
content = BeautifulSoup(response.data.decode('utf-8') , "html5lib")
# Extract plain text from soup, lowercase the string, splitlines to convert to list
WORDS = content.get_text().lower().splitlines()

#----------PIL PARAMETERS----------
# RGB mode (use RGBA w/o bgcolor for transparency)
mode = 'RGB'
# Size of each image in dataset
(W , H) = (300 , 100)
# White background color
bgcolor = (255 , 255 , 255)
# Black text color
txtcolor = (0 , 0 , 0)
# Create font object (optional)
font = ImageFont.truetype('./fonts/Roboto-Bold.ttf' , size=35)

for i in range(size):
    word = random.choice(WORDS)
    img = Image.new(mode , (W , H) , bgcolor)
    draw = ImageDraw.Draw(img)
    # Get the textsize
    (w , h) = draw.textsize(word , font)
    # Text is centralized using the first parameter passed
    draw.text(((W-w)/2 , (H-h)/2) , word , fill=txtcolor , font=font)
    img.save('./dataset/'+word+'.png' , optimize=True , quality=10)

print ('Dataset of ',size,' words generated succesfully!')
