import pyautogui
import keyboard

pyautogui.PAUSE = 0
while True:
  while True:
    # press p to start it up
    if keyboard.is_pressed('p'):
      break
     
  while True:
  # pyautogui.click() will click
  # if you want it to right click change pyautogui.click() to pyautogui.click(button='right')
    pyautogui.click()
    # press o to stop it
    if keyboard.is_pressed('o'):
      break
