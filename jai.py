import pyautogui
import time
import win32clipboard
import mysql.connector
from termcolor import colored
import psycopg2
import pyttsx3

def Talk(speech):
    engine = pyttsx3.init()
    voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty('voice',voice)
    engine.say(speech)
    engine.runAndWait()


# print(pyautogui.position())

def ExtractData():
    pyautogui.click(227, 764)
    pyautogui.click(227, 764)
    pyautogui.click(227, 764)

    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.1)
    print("Getting Question Name..")
    win32clipboard.OpenClipboard()
    Question = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    print(Question)
    Question = list(Question.split(": "))
    Question = list(Question[1].split('\r\n'))
    Question = str(Question[0])
    #print(Question)
    Talk("Searching Database ...")
    DataBase(Question)

def WriteCode(Code):
    pyautogui.click(1628, 772)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.keyDown("delete")
    # print("Length is : " + str(len(Code)))
    try:
        end = Code.rindex('}')
        # print(end)
        Code = Code[:end+1]
        pyautogui.typewrite(Code)
    except:
        Talk("NO CODE")

def DataBase(name):
    mydb = psycopg2.connect(
        host="HOST",
        database="DATABASE",
        user="USER",
        password="PASSWORD"
    )
    mycursor = mydb.cursor()
    name = "'"+name+"'"

    sql = 'SELECT "CODE" from elabdata WHERE "QUESTION_NAME" = '+name
    mycursor.execute(sql)
    result = mycursor.fetchone()
    # print(result)
    if result != None:
        print("Coding...")
        Talk("Code Found")
        Talk("Started Coding...")
        WriteCode(result[0])
    else:
        err = colored('Error : ', 'red')
        text = colored('Code not Found. Need to Code Manually..', 'green')
        print(err + text)
        Talk("Error, Code not Found. Need to Code Manually..")

for i in range(63, 100):
    Talk("Starting Question "+str(i+1))
    ExtractData()
    time.sleep(5)
    pyautogui.click(2595, 1654)
    Talk("Completed Question "+str(i+1))
    time.sleep(5)
    pyautogui.click(3704, 461)
    time.sleep(5)
# print(pyautogui.position())