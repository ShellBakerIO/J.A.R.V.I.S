import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
from googletrans import Translator


recognizer = sr.Recognizer()
engine = pyttsx3.init()
yt_url = 'https://www.youtube.com/'
minecraft_path = r"C:\Users\HONOR\AppData\Roaming\.minecraft\TLauncher.exe"
translator_mode = False
translator = Translator()


def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Ошибка синтеза речи: {e}")


while True:
    with sr.Microphone() as source:
        print("Слушаю...")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio, language='ru-RU')
            print("Вы сказали: " + text)

            if not translator_mode:
                if text == "Джарвис":
                    speak("Да, сэр")
                elif text == "Открой YouTube":
                    webbrowser.open(yt_url, new=0, autoraise=True)
                    speak("Запускаю Ютуб, сэр!")
                elif text == "Запусти Minecraft":
                    subprocess.Popen(minecraft_path, shell=True)
                    speak("Запускаю Майнкрафт, сэр!")
                elif text == "Активируй переводчик":
                    translator_mode = True
                    speak("Переводчик активирован. Говорите, что нужно перевести.")
            else:
                if text == "Деактивируй переводчик":
                    translator_mode = False
                    speak("Переводчик деактивирован. Жду новых команд.")
                else:
                    try:
                        translation = translator.translate(text, src='ru', dest='en')
                        print(f"Перевод: {translation.text}")
                        speak(f"Перевод: {translation.text}")
                    except Exception as e:
                        print(f"Ошибка перевода: {e}")
                        speak("Повторите, пожалуйста.")
        except sr.UnknownValueError:
            speak("Сэр, я не расслышал вас.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            speak("Произошла ошибка, попробуйте снова.")
