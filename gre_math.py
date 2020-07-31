import pyautogui

print(pyautogui.position())

pyautogui.PAUSE = 1.75

# Minimize sublime text (Coordinates = (1250, 11))
pyautogui.click(1250, 11)

# Double click on gre folder
pyautogui.click(335, 629, clicks =2, interval = 0.25)

# Double click on 3 month verbal
pyautogui.click(265, 212, clicks =2, interval = 0.25)

pyautogui.PAUSE = 0.1

pyautogui.keyDown('alt')  # hold down the alt key
pyautogui.press('space') # press space
pyautogui.keyUp('alt')    # release the alt key

pyautogui.press('down') # press down
pyautogui.press('down') # press down
pyautogui.press('down') # press down
pyautogui.press('down') # press down

pyautogui.PAUSE = 1.5

pyautogui.press('enter') # press enter

pyautogui.PAUSE = 1.75

# Minimize pdf
pyautogui.click(1250, 11)

# Double click on essential materials folder
pyautogui.click(307, 173, clicks =2, interval = 0.25)

# Double click on Manhattan folder
pyautogui.click(225, 189, clicks =2, interval = 0.25)

# Double click on Manhattan gre book
pyautogui.click(231, 149, clicks =2, interval = 0.25)

pyautogui.PAUSE = 0.1

pyautogui.keyDown('alt')  # hold down the alt key
pyautogui.press('space') # press space
pyautogui.keyUp('alt')    # release the alt key

pyautogui.press('down') # press down
pyautogui.press('down') # press down
pyautogui.press('down') # press down
pyautogui.press('down') # press down
pyautogui.press('enter') # press enter

pyautogui.PAUSE = 1.75

# Double click on page number text box
pyautogui.click(435, 59, clicks =2, interval = 0.25)

# Type page number
pyautogui.typewrite("10")

# press enter
pyautogui.typewrite(["enter"])

# Minimize pdf
pyautogui.click(1250, 11)

# Minimize folder
pyautogui.click(1250, 11)

pyautogui.PAUSE = 8

# Click on Google Chrome
pyautogui.click(567,758)

pyautogui.PAUSE = 0.1

pyautogui.keyDown('alt')  # hold down the alt key
pyautogui.press('space') # press space
pyautogui.keyUp('alt')    # release the alt key

pyautogui.press('down') # press down
pyautogui.press('down') # press down
pyautogui.press('down') # press down
pyautogui.press('down') # press down
pyautogui.press('down') # press down
pyautogui.press('enter') # press enter

pyautogui.PAUSE = 1

# Go to search bar
pyautogui.click(229, 57)

# Type in path to manhattan gre
pyautogui.typewrite("file:///C:/Users/Dell/Desktop/GRE/Essential%20materials/Manhattan/5%20lb.%20Book%20of%20GRE%20Practice%20Prob%20-%20Manhattan%20Prep.pdf")

# Press enter
pyautogui.typewrite(["enter"])

# Go to position
pyautogui.moveTo(1304, 131)

pyautogui.PAUSE = 0.25

# Click on chapters
pyautogui.click(1304, 131)

# Click on contents
pyautogui.click(1177, 269)

pyautogui.PAUSE = 1

# Click elsewhere to remove dropdown
pyautogui.click(1000, 269)

# Click on new tab
pyautogui.click(270, 18)

pyautogui.PAUSE = 4

# Go to Magoosh
pyautogui.click(215, 83)

pyautogui.PAUSE = 3.5

# Sign In
pyautogui.click(453, 605)

pyautogui.PAUSE = 1.5

# Minimize chrome
pyautogui.click(1250, 11)

# Go to position
pyautogui.moveTo(620, 744)

# Click on sublime text
pyautogui.click(620, 744)

# CLose sublime
pyautogui.click(1356, 5)
