from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# get mouse positions and color with
# >>> import pyautogui
# >>> pyautogui.displayMousePosition()
BTN_MINERIUM:list = [81,528]
BTN_RRO:list = [1916,662]
BTN_CONFIRM:list = [950,599]
ACTION_SEQUENCE:list = [BTN_MINERIUM, BTN_RRO, BTN_CONFIRM]
ACTION_TIME:list = [12, 18, .5]

def click_btn(pos:list):
    click(pos[0],pos[1])

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def time_now():
    now = time.localtime()
    return str(now.tm_year)+'/'+str(now.tm_mon)+'/'+str(now.tm_mday)+' '+str(now.tm_hour)+':'+str(now.tm_min)+':'+str(now.tm_sec)

keep_going = True
def quit_action(callback):
    global keep_going
    keep_going = False
    print('quit pressed')

keyboard.on_press_key('space', quit_action)

print(time_now()+' starting wartune auto astral script')

action_index = 0
while keep_going:
    action = ACTION_SEQUENCE[action_index%len(ACTION_SEQUENCE)]
    timing = ACTION_TIME[action_index%len(ACTION_TIME)]
    action_index+=1

    click_btn(action)
    time.sleep(timing)
