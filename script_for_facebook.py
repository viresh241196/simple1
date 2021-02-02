from time import sleep
import pyautogui
#48,64 is the opera location
#267,51 is the position of search tab
#print(pyautogui.position())
pyautogui.hotkey('win', 'd')
pyautogui.typewrite(['win'])
sleep(1)
pyautogui.click(917, 366)                #917,366 is the opera in start
sleep(2)
pyautogui.click(267, 51)
pyautogui.typewrite("https://www.facebook.com")
pyautogui.typewrite(['enter'])
sleep(2)
pyautogui.click(829,145)                            #829,145 is the position for email id
pyautogui.typewrite("8655899904")
pyautogui.click(998,147)                            #998,147 is the position for password
pyautogui.typewrite("mywindows8")
pyautogui.click(1161,149)                           #1161,149 is position for login button