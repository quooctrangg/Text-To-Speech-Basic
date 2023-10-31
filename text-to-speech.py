from gtts import gTTS
import playsound

def speak(text):
    tts = gTTS(text=text, lang='vi')
    fileName = 'voice.mp3'
    tts.save(fileName)
    playsound.playsound(fileName)

text = input('Nhập điều bạn muốn nói: ')
speak(text)