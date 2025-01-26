import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess

recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
yt_url = 'https://www.youtube.com/'
minecraft_path = r"C:\Users\HONOR\AppData\Roaming\.minecraft\TLauncher.exe"

while True:
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language='ru-RU')
            print("Вы сказали: " + text)
            if text == "Джарвис":
                engine.say("Да, сэр")
                engine.runAndWait()
            elif text == "Открой YouTube":
                webbrowser.open(yt_url, new=0, autoraise=True)
                engine.say("Запускаю Ютуб, сэр!")
                engine.runAndWait()
            elif text == "Запусти Minecraft":
                subprocess.Popen(minecraft_path, shell=True)
                engine.say("Запускаю Майнкрафт, сэр!")

        except sr.UnknownValueError:
            engine.say("Не удалось распознать речь")
            engine.runAndWait()
