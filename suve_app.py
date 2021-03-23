import requests
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import pyautogui as pg
import webbrowser
import pyjokes
import tensorflow.keras
import numpy as np
import os
import sys
import wikipedia as wk
import operator
from tkinter import *
from tkinter import *
from PIL import ImageTk, Image
import os
import wolframalpha


client = wolframalpha.Client('6Q623Y-K4JK8VJXPJ')

root = Tk()
root.title("Project SUVE")
root.iconbitmap('logo.ico')

def speak(text):
    tts = gTTS(text=text, lang="hi")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove("voice.mp3")


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
            print(f"User said: {query}\n")  #User query will be printed.

        except Exception as e:
            print("Exception: ")
        return query

def genius(query):
    res=client.query(query)
    out = next(res.results).text
    return out

def classify(text):
    key = "3ca94b20-4a7c-11eb-ba32-f110fea3a9a95f52747b-b53c-4f21-ae1b-8a49d6abe049"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        print("No response from ML")


print(" ")
print("--------------------")
print("Project SUVE")
print("--------------------")
print("Assistant name: Tara")
print('---------------------')
print(" ")

def tara():
    speak("Greetings user, I am tara, you very own voice assistant, what can I do for you?")

    while True:
        text = listen()
        text = classify(text)
        try:
            cf = text["confidence"]
            text = text["class_name"]
            label = text
        except:
            print("No classification found")
            continue
        print("Recongized Label Function: "+label)
        print("Confidence: "+str(cf))

        if label=="calc" and cf>65:
            speak("Please speak your expression to be calculated")
            exp = listen()
            speak(genius(exp))

        elif "you" in text and ("leave" in text or "exit" in text):
            speak("Thank you for using this service")
            break

        elif label=="greeting" and cf>65:
                speak("Greetings user, I am tara, you very own voice assistant, what can I do for you")

        elif label=="cursor_right" and cf>65:
            xyzab = pg.position()
            listtss= list(xyzab)
            xc = listtss[0]
            yc = listtss[1]
            pg.moveTo(xc+200, yc)
            speak("Cursor moved to the right")

        elif label=="cursor_left" and cf>65:
            xyzabc = pg.position()
            listtabc = list(xyzabc)
            xcoc = listtabc[0]
            ycoc = listtabc[1]
            pg.moveTo(xcoc-100, ycoc)
            speak("Cursor moved to the left")

        elif label=="cursor_up" and cf>65:
            xyz = pg.position()
            listt = list(xyz)
            xco = listt[0]
            yco = listt[1]
            pg.moveTo(xco, yco-200)
            speak("Cursor moved to up")

        elif label=="cursor_down" and cf>65:
            xyzabcv = pg.position()
            listtt = list(xyzabcv)
            x = listtt[0]
            y = listtt[1]
            pg.moveTo(x, y+200)
            speak("Cursor moved down")

        elif label=="enter" and cf>65:
            pg.press('enter')
            speak("Enter button clicked")

        elif label=="right_click" and cf>65:
            pg.rightClick()
            speak("Right click button pressed")

        elif label=="space" and cf>65:
            pg.press('space')
            speak("Space button clicked")

        elif label=="typing" and cf>65:
            speak("What do you want to type?")
            textbt = listen()
            pg.typewrite(textbt)
            speak(textbt+" typed. Do you want me to enter?")
            ch_enter = listen()
            if "y" in ch_enter:
                pg.press('enter')
                speak("Enter button clicked")
            speak("Please speak your next command")


        elif label=="movie" and cf>65:
            speak("Which movie do you want to watch?")
            ch_mov = listen()
            webbrowser.open("https://ww4.0123movie.net/search/"+ch_mov+".html")
            speak("Please speak your next command")
            """
            speak("Please choose one of the following websites to watch movies on")
            speak("Netflix")
            speak("Amazon Prime")
            speak("Please speak your choice now")
            mvc = listen()
            if "Netflix" in mvc:
                webbrowser.open("https://www.netflix.com/")
                print("Netflix opened")
                speak("Netflix opened")

            elif "Amazon Prime" in mvc:
                webbrowser.open("https://www.primevideo.com/")
                print("Amazon Prime opened")
                speak("Amazon Prime opened")
            """


        elif label=="open_google" and cf>65:
            webbrowser.open("https://www.google.com/")
            print("Google opened")
            speak("Google opened")


        elif label=="open_youtube" and cf>65:
            webbrowser.open("https://www.youtube.com/")
            print("Youtube opened")
            speak("Youtube opened")

        elif label=="shopping" and cf>65:
            speak("Please choose one of the following websites to buy stuff on")
            speak("Noon")
            speak("Amazon")
            speak("Namshi")
            speak("Please speak your choice now")
            svc = listen()
            if "noon" in svc:
                webbrowser.open("https://www.noon.com/uae-en/")
                print("Noon.com opened")
            elif "Amazon" in svc:
                webbrowser.open("https://www.primevideo.com/")
                print("Amazon opened")
            elif "namchi" in svc:
                webbrowser.open("https://fmovies.to/")
                print("Namshi opened")

        elif label=="food" and cf>65:
            speak("Please speak your preffered cuisine, and I shall search for the nearby restaurants matching the cuisine.")
            cuisine = listen()
            webbrowser.open("https://www.google.com/maps/search/"+str(cuisine))
            speak("Please speak your next command")

            """
            speak("Please choose one of the following cuisines.")
            speak("Chinese")
            speak("Japanese")
            speak("Arabic")
            speak("Please speak your choice now")
            chfod = listen()
            chfod = chfod.lower()
            if "chin" in chfod:
                print("Cuisine Choice: Chinese")
                speak("We have the following restaurants for chinese")
                speak("Chinese Palace")
                speak("Hot Plate")
                speak("Imperial Dragon")
                speak("Please speak your choice now")
                chfodchi = listen()
                chfodchi = chfodchi.lower()
                if "chinese palace" in chfodchi:
                    print("Restaurant Choice: Chinese Palace")
                    webbrowser.open("https://chinesepalacegroup.com/index.php?utm_source=google&utm_campaign=DTF2020&utm_medium=keyword-cgp&gclid=Cj0KCQiAjKqABhDLARIsABbJrGmpeSJ2heIB5Fc7OkNPTTsBgU_UN7J897e0_fPp61PIEDj9XqcmV8MaAszdEALw_wcB#Brands")
                elif "hot plate" in chfodchi:
                    print("Restaurant Choice: Hot Plate")
                    webbrowser.open("https://www.zomato.com/dubai/hot-plate-discovery-gardens")
                elif "imperial dragon" in chfodchi:
                    print("Restaurant Choice: Imperial Dragon")
                    webbrowser.open("http://www.imperialdragondxb.com/")
            if "jap" in chfod:
                print("Cuisine Choice: Japanese")
                speak("We have the following restaurants for japanese")
                speak("Yakitate")
                speak("wagama")
                speak("Please speak your choice now")
                chfodchi2 = listen()
                chfodchi2 = chfodchi2.lower()
                if "ya" in chfodchi2:
                    print("Restaurant Choice: Yakitate")
                    webbrowser.open("https://yakitate.co/")
                elif "wag" in chfodchi2:
                    print("Restaurant Choice: Wagamama")
                    webbrowser.open("https://www.wagamama.ae/")
            if "arab" in chfod:
                print("Cuisine Choice: Arabic")
                speak("We have the following restaurants for arabic")
                speak("Al Safadi")
                speak("Damasco")
                speak("Please speak your choice now")
                chfodchi3 = listen()
                chfodchi3 = chfodchi3.lower()
                if "al safadi" in chfodchi3:
                    print("Restaurant Choice: Al Safadi")
                    webbrowser.open("https://www.alsafadi.ae/")
                elif "damasco" in chfodchi3:
                    print("Restaurant Choice: Damasco")
                    webbrowser.open("https://www.damascorestaurant.com/")
            """

        elif label=="music" and cf>65:
            speak("What kind of music would you like to listen to?")
            speak("English")
            speak("Hindi")
            speak("Korean")
            speak("If you want to choose your own choice of music, just speak I want to choose my own style")
            speak("Please speak your choice now")
            chmusic = listen()
            chmusic = chmusic.lower()
            if "eng" in chmusic:
                print("Music Choice: English")
                speak("Choose any of the following genres for english music")
                speak("Pop")
                speak("Rock and Roll")
                speak("Old music")
                speak("Country")
                speak("Please speak your choice")
                chgm = listen()
                chgm = chgm.lower()
                if "pop" in chgm:
                    webbrowser.open("https://www.youtube.com/watch?v=2Vv-BfVoq4g&list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj")
                elif "rock" in chgm:
                    webbrowser.open("https://www.youtube.com/watch?v=fJ9rUzIMcZQ&list=PLNxOe-buLm6cz8UQ-hyG1nm3RTNBUBv3K")
                elif "old" in chgm:
                    webbrowser.open("https://www.youtube.com/watch?v=DjeXpV-AUzo&t=739s")
                elif "country" in chgm:
                    webbrowser.open("https://www.youtube.com/watch?v=3sE2grIDYNw")
            elif "hin" in chmusic:
                print("Music Choice: Hindi")
                speak("Choose any of the following genres for hindi music")
                speak("Rap")
                speak("Bollywood Pop")
                speak("Old songs")
                speak("Please speak your choice")
                chgm2 = listen()
                chgm2 = chgm2.lower()
                if "pop" in chgm2:
                    webbrowser.open("https://www.youtube.com/watch?v=nNCWKja8oxw&t=198s")
                elif "honey" in chgm2 or "ba" in chgm2:
                    webbrowser.open("https://www.youtube.com/watch?v=oz5TmtW8oOk")
                elif "rap" in chgm2:
                    webbrowser.open("https://www.youtube.com/watch?v=jFGKJBPFdUA&list=PLp4THQoCsDJgURO3do6PWz9KasnvPLo60")
                elif "old" in chgm2:
                    webbrowser.open("https://www.youtube.com/watch?v=lslZptXok8o&list=PL92D6833E06037526")
            elif "Kor" in chmusic:
                print("Music Choice: Korean")
                webbrowser.open("https://www.youtube.com/watch?v=z3szNvgQxHo&list=PL4QNnZJr8sRNKjKzArmzTBAlNYBDN2h-J")
            elif "my own style" in chmusic:
                speak("What kind of style do you want")
                chstyle = listen()
                webbrowser.open("https://www.youtube.com/results?&q="+chstyle)
                print(chstyle+" opened")
            speak("Please speak your next command")

        elif label=="news" and cf>65:
            webbrowser.open("https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en")
            print("News website opened")
            speak("Please speak your next command")

        elif label=="jokes" and cf>65:
            joke1 = pyjokes.get_joke(language='en', category= 'all')
            speak(joke1)


        elif label=="google_search" and cf>65:
            speak("Please speak your search query for google")
            tbsd = listen()
            webbrowser.open("https://www.google.com/search?&q="+str(tbsd))
            print(tbsd+" searched on google")
            speak("Please speak your next command")


        elif label=="youtube_search" and cf>65:
            speak("Please speak your search query for youtube")
            tbsdy = listen()
            webbrowser.open("https://www.youtube.com/results?&q="+str(tbsdy))
            print(tbsdy+" searched on youtube")
            speak("Please speak your next command")

        elif label=="wiki" and cf>65:
            speak("Please speak your search query for wikipedia")
            tbsdw = listen()
            sumw = wk.summary(tbsdw, sentences=2)
            speak(sumw)
            print(tbsdw+" searched on wikipedia :-")
            print(sumw+"\n")
            speak("Please speak your next command")

        elif label=="click" and cf>65:
            pg.click()
            print("Clicked")
            speak("Mouse clicked.")

        elif label=="maps" and cf>65:
            speak("Please speak the name of the place you want to search on google maps")
            chmaps = listen()
            webbrowser.open("https://www.google.com/maps/search/"+str(chmaps))
            speak("Please speak your next command")

        elif label=="hold_down_cursor" and cf>65:
            pg.mouseDown()
            speak("Cursor has been held down")

        elif label=="exit" and cf>65:
            speak("Thank you for using this service")
            break

        else:
            speak("Can you please speak your query again?")
            qu = listen()
            speak(genius(qu))

def instruct():
    webbrowser.open('https://github.com/ShashwatM3/Project-SUVE/blob/main/Documentation')

Label(root, text=" ").pack()
my_menu=Menu(root)
root.config(menu=my_menu)

file_menu=Menu(my_menu)
my_menu.add_cascade(label="Options", menu=file_menu)
file_menu.add_command(label="Exit", command=root.destroy)

file_menu2=Menu(my_menu)
my_menu.add_cascade(label="Docs", menu=file_menu2)
file_menu2.add_command(label="How to use", command=instruct)



Label(root, text=" ").pack()
Label(root, text="--------------------", font="Helvetica 16 bold").pack()
Label(root, text="Project SUVE", font="Helvetica 16 bold").pack()
Label(root, text="--------------------", font="Helvetica 16 bold").pack()
Label(root, text=" ").pack()
Button(root, text='AI Assistant Tara', font="Helvetica 13", command=tara).pack()
Label(root, text=" ").pack()
Button(root, text='AI Doctor', font="Helvetica 13", command=tara).pack()
Label(root, text=' ').pack()
img = ImageTk.PhotoImage(Image.open("logo.jpg"))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")




root.mainloop()
