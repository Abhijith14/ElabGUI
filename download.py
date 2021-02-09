import pyautogui
import time

# url = "https://care.srmist.edu.in/mysqlelabsh/login/student/code/dbms/dbms.code.php?id=1&value="
pyautogui.click(1850, 853)
for i in range(100):
    print("Question " + str(i + 1))
    time.sleep(2)
    pyautogui.click(3308,1375)
    time.sleep(1)
    pyautogui.click(2317, 1503)
    time.sleep(5)
    pyautogui.click(2582, 1504)
    time.sleep(5)
    pyautogui.click(3597, 1644)
    time.sleep(5)
    pyautogui.click(3713, 460)
# print(pyautogui.position())