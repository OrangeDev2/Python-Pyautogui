import pyautogui, time

time.sleep(1)

time.PAUSE = 0

for line in open("typeracer_text", "r"):
        pyautogui.typewrite(line)

