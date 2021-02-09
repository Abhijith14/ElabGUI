import pyautogui
import time
import os.path
#Evaluate = 974, 676
#Download = 1276, 515
#print(pyautogui.position())

def renaming():
    path = "C:/Users/DSLR/Desktop/ELAB PYTHON/"
    t = 0
    for i in range(1, 101):
        if t > 0:
            name = "report ("+str(t)+").png"
        else:
            name = "report.png"

        for c in avoid:
            if c == str(t+1):
                print("Q.no"+str(c)+" Not Found...")
                t = t + 1

        FileName = "Q. "+str(t+1)+".png"


        if(check(name)):
            os.rename(os.path.join(path,name), os.path.join(path,FileName))
            print("Renamed "+FileName)
        else:
            print("Skipped "+name)
        t = t + 1

def elab():
    time.sleep(1)
    pyautogui.click(910, 594)
    time.sleep(1)
    pyautogui.click(1285, 651)

def check(name):
    time.sleep(2)
    if os.path.isfile("C:/Users/DSLR/Desktop/ELAB PYTHON/" + name) == False:
        return False
    else:
        return True
avoid = []
t = 0
disp = 0
for i in range(1,101):
    if t > 0:
        name = "report ("+str(t)+").png"
    else:
        name = "report.png"

    elab()
    n = 0
    while check(name) == False:
        n = n + 1
        if n <= 3:
            print("Rechecking "+str(disp+1))
            if check(name) == False:
                elab()
        else:
            print("Skipped "+str(disp+1))
            t = t - 1
            avoid.append(disp+1)
            break
    if n < 4:
        print("Q.no." + str(disp + 1)+" Downloaded!!")
    t = t + 1
    disp = disp + 1
    pyautogui.click(1313, 179)

renaming()
#pyautogui.hotkey("ctrl","a")
#pyautogui.typewrite("Abhijith Udayakumar")