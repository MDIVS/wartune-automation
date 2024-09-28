import time
from core.InputEvent import *
import mouse_actions

def time_now():
    now = time.localtime()
    return str(now.tm_year)+'/'+str(now.tm_mon)+'/'+str(now.tm_mday)+' '+str(now.tm_hour)+':'+str(now.tm_min)+':'+str(now.tm_sec)

def _input(event:InputEvent):
    if isinstance(event, InputKeyEvent):
        if event.name == 'esc': queue_exit()
        if event.name == 'space': switch_pause()
        if event.name == 'left': move_x(1500)
        if event.name == 'right': move_x(-1500)
        if event.name == 'up': change_ydirection(-1)
        if event.name == 'down': change_ydirection(1)

input_signal.connect(_input)

keep_going = True
paused = False
xmove = 0
ydirection = 1

def queue_exit():
    global keep_going
    keep_going = False
    print(time_now()+' finishing map search')

def switch_pause():
    global paused
    paused = not paused
    if paused: print('paused!')
    else: print('unpaused!')

def move_x(amount:int):
    if amount==0: return
    global xmove
    xmove += amount
    print("moving "+amount)

def change_ydirection(ydir:int):
    global ydirection
    ydirection = sign(ydir)
    if ydirection == 1: print("moving down")
    else: print("moving up")

print(time_now()+' starting map search')

# Exemplo de uso
start_x, start_y = 200, 200  # Coordenadas iniciais
end_x, end_y = 1000 , 1000      # Coordenadas finais
x_center = int((start_x+end_x)/2)
y_center = int((start_y+end_y)/2)
width = end_x-start_x
height = end_y-start_y

action_index = 0

def sign(n) -> int:
    return int((n>0) - (n<0))

while keep_going:
    if xmove != 0:
        amount = min(width, abs(xmove))*sign(xmove)
        if xmove > 0: mouse_actions.mouse_drag_and_drop(start_x, y_center, int(start_x+amount), y_center, .1)
        if xmove < 0: mouse_actions.mouse_drag_and_drop(end_x, y_center, int(end_x+amount), y_center, .1)
        xmove -= amount
    elif not paused:
        if ydirection > 0: mouse_actions.mouse_drag_and_drop(x_center, end_y, x_center, start_y, .1)
        if ydirection < 0: mouse_actions.mouse_drag_and_drop(x_center, start_y, x_center, end_y, .1)
        time.sleep(.5)
