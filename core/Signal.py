class Signal:
    def __init__(self):
        self.__connections = []

    def connect(self, func):
        for i in self.__connections:
            if i == func: return
        self.__connections.append(func)

    def disconnect(self, func):
        self.__connections.remove(func)
    
    def emit(self, *args):
        for i in self.__connections:
            i(*args)