import win32api, win32con # pip install pywin32
import time

def mouse_click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def move_mouse_to(x, y):
    win32api.SetCursorPos((x, y))

def mouse_drag_and_drop(start_x, start_y, end_x, end_y, delay=0):
    # Move o cursor para a posição inicial
    move_mouse_to(start_x, start_y)
    
    # Pressiona o botão esquerdo do mouse
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, start_x, start_y, 0, 0)
    if delay>0: time.sleep(delay/2)  # Pequeno atraso para simular um comportamento mais natural
    
    # Arrasta o mouse para a posição final
    move_mouse_to(end_x, end_y)
    
    if delay>0: time.sleep(delay/2)  # Outro pequeno atraso
    
    # Solta o botão esquerdo do mouse
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, end_x, end_y, 0, 0)