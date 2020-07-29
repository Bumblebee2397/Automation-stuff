import pyautogui

# Pause 2 seconds in between each function call
pyautogui.PAUSE = 2

# Minimize sublime text (Coordinates = (1250, 11))
pyautogui.click(1250, 11, interval = 1)

# Pause 10 seconds in between each function call
pyautogui.PAUSE = 10

# Double click on "Apowersoft screenrecording app"
pyautogui.click(260, 120, clicks =2, interval = 0.25)

# Pause 2 seconds in between each function call
pyautogui.PAUSE = 1

# Maximize screen for recording
pyautogui.click(510, 606, interval = 1)

# Click on "REC"
pyautogui.click(342, 677, interval = 1)

# On pop-up "Are you ready?"
pyautogui.click(876, 469, interval = 1)

# Click on Zoom app in the taskbar
pyautogui.click(670, 761, interval = 1)

# Click on Join Meeting
pyautogui.click(536, 288, interval = 1)

# Click on text box
pyautogui.click(551, 323, interval = 1)

# Type in meeting id
pyautogui.typewrite("403 155 8868")

# Join the meeting
pyautogui.click(706, 499, interval = 1)

# Click on text box
pyautogui.click(566, 322, interval = 1)

# Type in meeting passcode
pyautogui.typewrite("289110")

# Click on Join Meeting
pyautogui.click(678, 496, interval = 1)

print(pyautogui.position())
 