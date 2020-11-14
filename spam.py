# importing required modules
import pyautogui, time

# small delay to open to desired chat
time.sleep(5)

# loading in the shreak script
script = open("gucci.txt", "r")

# iteratiing over all of the lines
for line in script:
    # typing the line
    pyautogui.typewrite(line)
    # pressing enter
    pyautogui.press("enter")