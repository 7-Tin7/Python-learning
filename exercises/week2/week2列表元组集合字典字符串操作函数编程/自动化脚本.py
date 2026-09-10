import pyautogui
import time
import pyperclip
import random
from pyautogui import hotkey
text = ["你好","你好","你真的很好"]
time.sleep(5)
for _ in range(10):
    messages = random.choice(text)
    pyperclip.copy(messages)
    pyautogui,hotkey("ctrl","v")
    pyautogui.press("enter")
time.sleep(random.uniform(0.2,0.5))





import pyautogui
import time
import pyperclip
import random
text = ["想你了","你想了","了你想","了想你"]
for _ in range(10):
    messages = random.choice(text)
    pyperclip.copy(messages)
    pyautogui,hotkey("ctrl","v")
    pyautogui.press("enter")
time.sleep(random.uniform(0.2,0.5))





import pyperclip
import pyautogui
import random
import time
text = ["赢了","赚了","麻了"]
for _ in range(10):
    messages = random.choice(text)
    pyperclip.copy(messages)
    pyautogui,hotkey("ctrl","v")
    pyautogui.press("enter")
time.sleep(random.uniform(0.2,0.5))






