import keyboard # pip install keyboard
from core.Signal import *

input_signal = Signal()

class InputEvent:
    """Abstract base class of all types of input events."""

    device = 0

    def __init__(self):
        self.device = 0

class InputKeyEvent(InputEvent):
    scan_code = None
    name = None
    modifiers = None

    def __init__(self):
        super().__init__()

def __emit_input_signal(callback: keyboard.KeyboardEvent):
    event = InputKeyEvent()
    event.device = callback.device
    event.scan_code = callback.scan_code
    event.name = callback.name
    event.modifiers = callback.modifiers

    input_signal.emit(event)

keyboard.on_press(__emit_input_signal)