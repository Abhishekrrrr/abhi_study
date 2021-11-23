from gtts import gTTS
import os
text=open('dem.txt','r').read()
language='en'
output=gTTS(text=text,lang='en',slow=False)
output.save('out.mp3')
os.system('start out.mp3')

