# pip install pyautogui
# Sometimes you will need to also pip install Pillow
from pyautogui import *
import pyautogui
import time
import mouse_actions
from core.InputEvent import *

ONE_CLICK_SELL:bool = False 
BTN_ONE_CLICK_SELL:list = [1325,640]
BTN_ONE_CLICK_SINTETIZE:list = [1050,640]
BTN_ONE_CLICK_SINTETIZE_CONFIRM:list = [780,580]

class Buttom:
    def __init__(self, pos, state, activated_color, name):
        self.pos = pos
        self.state = state
        self.activated_color = activated_color
        self.name = name

# get mouse positions and color with
# >>> import pyautogui
# >>> pyautogui.displayMousePosition()
buttons = [
    Buttom([600, 740], False, [150,150,150], 'Um'),
    Buttom([745, 740], False, [140,140,140], 'Dois'),
    Buttom([890, 740], False, [150,150,150], 'Três'),
    Buttom([1035, 740], False, [150,150,150], 'Quatro'),
    Buttom([1180, 740], False, [150,150,150], 'Cinco')
]

buttom_index:int = 0

def time_now():
    now = time.localtime()
    return str(now.tm_year)+'/'+str(now.tm_mon)+'/'+str(now.tm_mday)+' '+str(now.tm_hour)+':'+str(now.tm_min)+':'+str(now.tm_sec)

def _input(event:InputEvent):
    if isinstance(event, InputKeyEvent):
        if event.name == 'esc': queue_exit()
        if event.name == 'space': switch_pause()
        if event.name == 'enter': click_sintetize()

input_signal.connect(_input)

keep_going = True
paused = False
sintetize = False

def queue_exit():
    global keep_going
    keep_going = False
    print('quit pressed')

def switch_pause():
    global paused
    paused = not paused
    print('switch pause pressed')

def click_sintetize():
    global sintetize
    sintetize = True

def update_buttom_states():
    states = []
    first_buttom = True

    for b in buttons:
        gui_pixel = pyautogui.pixel(b.pos[0], b.pos[1])
        b.state = gui_pixel[0]>=b.activated_color[0] or gui_pixel[1]>=b.activated_color[1] or gui_pixel[2]>=b.activated_color[2]
        if first_buttom:
            b.state = True
            first_buttom = False
        states.append({gui_pixel, b.state})
    
    return states

def choose_buttom():
    previous = buttons[0]
    for b in buttons:
        if b.state == False: break
        previous = b
    return previous

def check_space():
    gui_pixel = pyautogui.pixel(last_astral_position[0], last_astral_position[1])
    return gui_pixel[0]>=150 or gui_pixel[1]>=150 or gui_pixel[2]>=150

[A_NONE, A_VERDE, A_AZUL, A_ROXO, A_LARANJA, A_VERMELHO] = [
    [0,0,0],
    [0,150,0],
    [0,0,150],
    [150,0,150],
    [150,150,0],
    [150,0,0]
]

class Astral:
    def __init__(self, cor):
        self.cor = cor
        self.pos = [0,0]

# função ainda não implementada, infelizmente é mais dificil doque eu pensava
def print_astrals():
    initial_pos = [554,405]
    final_pos = [1340,500]
    width = final_pos[0]-initial_pos[0]
    height = final_pos[1]-initial_pos[1]

    astrals = [
        [Astral(A_NONE), Astral(A_NONE), Astral(A_NONE), Astral(A_NONE), Astral(A_NONE), Astral(A_NONE), Astral(A_NONE), Astral(A_NONE)],
        [Astral(A_NONE), Astral(A_NONE), Astral(A_NONE), Astral(A_NONE), Astral(A_NONE), Astral(A_NONE), Astral(A_NONE), Astral(A_NONE)]
    ]

    positions = []
    for l in range(len(astrals)):
        for k in range(len(astrals[l])):
            jump_x_spaces = width/(len(astrals[l])-1)
            jump_y_spaces = height/(len(astrals)-1)
            astrals[l][k].pos = [int(initial_pos[0]+jump_x_spaces*k), int(initial_pos[1]+jump_y_spaces*l)]

            gui_pixel_1 = pyautogui.pixel(astrals[l][k].pos[0], astrals[l][k].pos[1])
            gui_pixel_2 = pyautogui.pixel(astrals[l][k].pos[0]-8, astrals[l][k].pos[1]+8)
            gui_pixel_3 = pyautogui.pixel(astrals[l][k].pos[0]-8, astrals[l][k].pos[1]-8)
            gui_pixel_4 = pyautogui.pixel(astrals[l][k].pos[0]+8, astrals[l][k].pos[1]+8)
            gui_pixel_5 = pyautogui.pixel(astrals[l][k].pos[0]+8, astrals[l][k].pos[1]-8)

            merged_pixel = [
                (gui_pixel_1[0]+gui_pixel_2[0]+gui_pixel_3[0]+gui_pixel_4[0]+gui_pixel_5[0])/5,
                (gui_pixel_1[1]+gui_pixel_2[1]+gui_pixel_3[1]+gui_pixel_4[1]+gui_pixel_5[1])/5,
                (gui_pixel_1[2]+gui_pixel_2[2]+gui_pixel_3[2]+gui_pixel_4[2]+gui_pixel_5[2])/5,
                l*8+k
            ]

            # b.state = gui_pixel[0]>=b.activated_color[0] or gui_pixel[1]>=b.activated_color[1] or gui_pixel[2]>=b.activated_color[2]
            
            positions.append(merged_pixel)
    
    # print(positions)

last_astral_position = [1339, 503]

print(time_now()+' starting wartune auto astral script')
while keep_going:
    if sintetize:
        sintetize = False
        paused = False
        mouse_actions.mouse_click(BTN_ONE_CLICK_SINTETIZE[0],BTN_ONE_CLICK_SINTETIZE[1])
        time.sleep(.05)
        mouse_actions.mouse_click(BTN_ONE_CLICK_SINTETIZE_CONFIRM[0],BTN_ONE_CLICK_SINTETIZE[1])
        time.sleep(.05)
    elif check_space():
        if ONE_CLICK_SELL:
            mouse_actions.mouse_click(BTN_ONE_CLICK_SELL[0],BTN_ONE_CLICK_SELL[1])
            time.sleep(2)
        if check_space():
            print('not enough space')
            # print_astrals()
            paused = True
        else:
            paused = False

    if paused: continue

    update_buttom_states()

    buttom_to_click = choose_buttom()
    print(buttom_to_click.name, end=" ", flush=True)
    mouse_actions.mouse_click(buttom_to_click.pos[0], buttom_to_click.pos[1])
    time.sleep(.5)