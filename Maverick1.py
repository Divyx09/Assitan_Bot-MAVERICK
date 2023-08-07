import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import requests
from requests import get 
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes 
import pyautogui
import keyboard
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
# from transformers import AutoModelForCausalLM, AutoTokenizer
import playsound
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import  Options


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

def wish():
    hour=int(datetime.datetime.now().hour)
    now = datetime.datetime.now()
    if hour>=0 and hour<=12:
        speak(f"Good morning . Its" + now.strftime(' %Y/%m/%d %I:%M %p'))

    elif hour>12 and hour<18:
        speak(f"Good afternoon. Its " + now.strftime(' %Y/%m/%d %I:%M %p'))
    else:
        speak(f"Good evening. Its" + now.strftime(' %Y/%m/%d %I:%M %p'))
    speak(" I am Maverick. How may i help you sir")

def news():
    main_url="http://newsapo.org/v2/top-headlines?sources=techcrunch&apikey=5523246cd08b4813b51547829f40d736"
    main_page= requests.get(main_url).json()
    artilcces=main_page["articles"]
    head=[]
    day=["first""second""third""fourth""fifth""sixth""seventh""eighth""ninth""tenth"]
    for ar in artilcces:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")



if __name__ == "__main__":
    wish()
    if 11:
        while True:
            query=takecommand().lower()

            if "open notepad" in query:
                speak("opening notepad")
                npath="C:\\Windows\\System32\\notepad.exe"
                os.startfile(npath)

            elif "current time" in query:
                now = datetime.datetime.now()
                speak("Current time is " + now.strftime('%I:%M %p'))
                
            elif " date " in query:
                now = datetime.datetime.now()
                speak("Current time is " + now.strftime('%Y:%m %d'))

            elif "day" in query:
                now=datetime.datetime.now()
                speak("today is " + now.strftime('%A') )

            elif "close notepad" in query:
                speak("ok sir, closing notepad")
                os.system("taskkill /IM notepad.exe /F")

            elif "open command prompt" in query:
                speak("opening command prompt")
                os.system("start cmd")

            elif "close command prompt" in query:
                speak("closing command prompt")
                os.system("taskkill /IM CMD.exe /F")
                
            elif "tell me a joke" in query:
                joke = pyjokes.get_joke()
                speak(joke)
                speak(joke)

            elif "shutdown the system" in query:
                speak("System going to shutdown")
                os.system('shutdown /s /t 0')

            elif"restart the system" in query:
                speak("System going to restart in 2 minutes")
                os.system("shutdown /r /t 0")
            
            elif("sleep the system") in query:
                speak("System going for sleep ")
                os.system("rundll32.ex porprof.dll,SetSuspendState 0,1,0")

            
            elif "open camera" in query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img =cap.read()
                    cv2.imshow('webcam', img)
                    k=cv2.waitKey(50)
                    if k==27:
                        break;
                    cap.release()
                    cv2.destroyAllWindows()

            elif "set alarm" in query:
                speak("sir at what you want to set alarm ")
                time=takecommand()
                while True:
                    Time_Ac=datetime.datetime.now()
                    now =Time_Ac.strftime("%H:%M:%S:")
                    if(now==time):
                        speak("Time to wake up sir")
                        playsound('.\Songs\Pyaar Hota Kayi Baar Hai_320(PagalWorld.com.se).mp3')
                    
                    elif now>time:
                        break;


            elif "play music" in query:
                music_dir=".\songs"
                songs = os.listdir(music_dir)
                # rd =random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir,songs[0]))
            
            elif "ip address" in query:
                ip = get('https://api.ipify.org').text
                speak(f"your ip addres is {ip}")

            elif "wikipedia" in query:
                speak("searching wikipedia... ")
                query=query.replace("wikipedia","")
                results =wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                speak(results)
                print(results)

            elif "switch the window" in query:
                keyboard.press("alt+tab")
                keyboard.release("alt+tab")

            elif "send message on whatsapp " in query:
                try:   
                    kit.sendwhatmsg("+918827409899", "Hi, how are you?", 20, 34)  
                    print("Message Sent!") 
                except Exception as e:  
                    print(f"Error in sending the message: {e}")
            
            # elif "tell me news" in query:
            #     speak("todays news are as follows")
            #     news()

            elif " send email to" in query:
                query=takecommand().lower()
                if "send a file " in query:
                    email = 'attardedivy94@gmail.com'
                    password = '4235deep'
                    send_to_email = 'divyaattarde94@gmail.com'
                    speak("okay sir,what is the subject for this email")
                    query=takecommand().lower()
                    subject = query
                    speak("and sir' what is the message for this email")
                    query2 = takecommand().lower()
                    message =query2
                    speak("sir please enter the correct path of the file into the shell")
                    file_location =input("please enter the path here")

                    speak("please enter the path here")

                    msg = MIMEMultipart()
                    msg['from']=email
                    msg['to']=send_to_email
                    msg['Subject']= subject

                    msg.attach(MIMEText(message,'plain'))

                    filename=os.path.basename(file_location)
                    attachement=open(file_location,'rb')
                    part=MIMEBase('application','octect-stream')
                    part.set_payload(attachement.read())
                    encoders.encode_base64(part)
                    part.add_header('content-Disposition',"attachement; filename %s" % filename)

                    msg.attah(part)

                    server=smtplib.SMTP('smtp.gmail.com',587)
                    server.starttls()
                    server.login(email,password)
                    text=msg.as_string()
                    server.sendmail(email,send_to_email,text)
                    server.quit()
                    speak(f"email has been sent to {send_to_email}")
                else:
                    email = 'attardedivy94@gmail.com'
                    password = '4235deep'
                    send_to_email = 'divyaattarde94@gmail.com' 
                    message = query

                    server=smtplib.SMTP('smtp.gmail.com',587)
                    server.starttls()
                    server.login(email,password)
                    text=msg.as_string()
                    server.sendmail(email,send_to_email,text)
                    server.quit()
                    speak(f"email has been sent to {send_to_email}")


                

            elif "open youtube" in query:
                webbrowser.open("https://www.youtube.com/")
            elif "open amazon" in query:
                webbrowser.open("https://www.amazon.in")
            elif "open hotstar" in query:
                webbrowser.open("https://www.hotstar.com/in")
            elif "open amazon prime" in query:
                webbrowser.open("https://www.primevideo.com")
            elif "open get hub" in query:
                webbrowser.open("https://github.com")
            elif "open google drive" in query:
                webbrowser.open("https://drive.google.com")
            elif "open Facebook" in query:
                webbrowser.open("https://www.facebook.com")
            elif "open instagram" in query:
                webbrowser.open("https://instagram.com")
            elif "open google" in query:
                speak("Sir, what should i search on google")
                cm = takecommand().lower()
                webbrowser.open(f"|{cm}")

            elif "on youtube" in query:
                speak('playing...')
                query = query.replace("on youtube","")
                kit.playonyt(query)

            elif "email to " in query:
                speak("what should i say")
                query=takecommand().lower()
            
            elif "no thanks" in query:
                speak("Thanx for using me sir. Bye , Have a nice day ahead")
                exit()

            elif "stop" in query:
                speak("I am available for you anytime. Bye , Have a nice day ahead")
                exit()
            
            speak("sir, do you have any other work")

            
            