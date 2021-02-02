from time import sleep
import pyautogui
#48,64 is the opera location
#267,51 is the position of search tab
#print(pyautogui.position())
pyautogui.hotkey('win','d')
pyautogui.typewrite(['win'])
sleep(1)
pyautogui.click(917,366)                #917,366 is the opera in start
sleep(2)
pyautogui.click(267, 51)
pyautogui.typewrite("www.youtube.com")
pyautogui.typewrite(['enter'])
sleep(3)
pyautogui.click(573,131)                               #573,131 is postion of search bar
pyautogui.typewrite("yeu to banjar sa tha")
pyautogui.typewrite(['enter'])
sleep(2)
pyautogui.click(243,726)                                       #243,726 is the position of that video
