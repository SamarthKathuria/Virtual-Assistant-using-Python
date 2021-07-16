import webbrowser as wb
import os
import pyttsx3
import datetime
import sys
import time
from datetime import date
import wikipedia
import requests




def zone():
    today = date.today()
    speak(today)

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume',0.7)

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def greeting():
    current = int(datetime.datetime.now().hour)
    if current >=0 and  current < 12:
        speak('Good Morning ' + name + '!')
    elif current >=12 and current < 16:
        speak('Good Afternoon ' + name + '!')
    else:
        speak('Good Evening ' + name + '!')

def myCommand():
   
    try:
        query = input()
        print(name + ' : ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try once again!')
        query = input( name + ' : ')

    return query


passw = 'India'
guess = ''
guess_count = 0
guess_limit = 4
out_of_guess = False

while guess != passw and not(out_of_guess):
    if guess_limit>guess_count:
        speak(('Enter Password : '))
        guess = input('')
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print(speak('Password Incorrect'))
else:
    speak('Enter Your Name : ')
    name = input('')
    greeting() 
    speak('My Name Is Tony! How Can I Help You?: ')
    while True:

         query = myCommand();
         query = query.lower()
         if 'open google' in query:
             speak('Opening Google....')
             wb.open('www.google.com')      
         elif 'open youtube' in query:
             speak('Opening Youtube....')
             wb.open('www.youtube.com')
         elif 'open amazon' in query :
             speak('Opening Amazon....')
             wb.open('www.amazon.in')
         elif 'open gmail' in query:
             speak('Opening Gmail....')
             wb.open('www.gmail.com')
         elif 'open facebook' in query:
             speak('Opening Facebook...')
             wb.open('www.facebook.com')
         elif 'open mix it' in query:
             speak('Opening Mixit...')
             wb.open('www.youtube.com/c/mixitred')
         elif query == ('what\'s up tony') or query == ('what\'s up tony'):
             speak('nothing much! Just doing my thing. What Can I do for You?')
         elif query == ('how are you') or query == ('how are you tony'):
             speak('I am Great! How can I Help You?')
         elif query == ('hello') or query == ('hello tony'):
             speak('Hello ' + name + ' It is pleasure working for you')
         elif 'the time' in query:
             speak(name + ' The Current time is : ' + time.strftime('%I : %M %p'))
         elif 'the date'  in query:
              speak(name + ' The Current date is : ')
              zone()
        
         elif 'do you have a girlfriend' in query or 'do you have any girlfriend' in query:
             speak('No, I dont have a girlfriend but i have a crush on siri and i am friends with alexa and google assistant')
         elif 'siri is better than you' in query:
             speak('oh! I do Have a crush on her')
         elif 'is better than you' in query:
             speak('I am good in my way')
         elif 'are you jealous' in query or 'are you mad' in query or 'are you crazy' in query or 'are you angry' in query:
             speak('I dont have this emotion')
         elif 'i am sad' in query or 'i\'m sad' in query:
             speak('Oh! there there')
         elif 'i am happy' in query or 'i\'m happy' in query:
             speak('That\'s Great, this makes me happy too, how can i help you:')
         elif 'i am angry' in query or 'i\'m angry' in query:
             speak('i am sorry if i did something wrong , how can i make you feel better:')
         elif 'wikipedia' in query:
             speak('Searching Wikipedia')
             query = query.replace('wikipedia' , '')
             result = wikipedia.summary(query , sentences='2')
             speak('According to Wikipedia: ' + result)
         elif 'open hotstar' in query:
             speak('Opening Hotstar')
             wb.open('www.hotstar.com')
        
         else:

             speak('Searching....')
             wb.open('https://www.google.com/search?q=' + query)
