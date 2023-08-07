import time 
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller
import pyttsx3  
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 200
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recongnizing... ")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}") 

    except Exception as e:
        speak("say that again please...")
        return None
    return query


# try:  
#     speak("whom to you have to send meassage")
#     speak("what message you have to send")
#     message=takecommand().lower()
#     speak("time in hours")
#     time_hrs=takecommand()
#     speak("time in seconds")
#     time_min=takecommand()
#     # Sending message in WhatsApp in India, using Indian dial code (+91)  
#     pwk.sendwhatmsg("+91"+Contact_no, message, time_hrs, time_min)  
#     print("Message Sent!") # Prints success message in console  
# except Exception as e:  
#     print(f"Error in sending the message: {e}")


keyboard = Controller()
# Contact_no=takecommand().lower()


def send_whatsapp_message(msg: str):
    try:
        pywhatkit.sendwhatmsg_instantly(
            phone_no="<+919893544211>", 
            message=msg,
            tab_close=True
        )
        time.sleep(10)
        pyautogui.click()
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("Message sent!")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    send_whatsapp_message(msg="Test message from a Python script!")