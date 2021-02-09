import pyttsx3

def Talk(speech):
    engine = pyttsx3.init()
    voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty('voice',voice)
    engine.setProperty('rate', 800)
    engine.say(speech)
    engine.runAndWait()

while True:
    Talk("it")