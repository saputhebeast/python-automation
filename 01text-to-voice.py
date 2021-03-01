#pip install gTTS
from gtts import gTTS
textToVoice = input("Enter the text: ")
voice = gTTS(text=textToVoice, lang='en', slow=False)
voice.save("voice.mp3")
