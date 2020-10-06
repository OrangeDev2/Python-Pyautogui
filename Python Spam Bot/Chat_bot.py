import pyautogui, time

time.sleep(5)

time.PAUSE = 0

for line in open("sometext", "r"):
        pyautogui.typewrite(line)


