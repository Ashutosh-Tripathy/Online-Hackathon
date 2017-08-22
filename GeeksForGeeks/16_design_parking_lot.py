class Vehicle:
    def __init__(self):
        self.spot_type = None

class MotorCycle(Vehicle):
    def __init__(self):
        self.spot_type = 1

def is_char_avaliable(char):
    a = ['e', 'r', 'c']
    if char in a:
        return True
    else:
        return False




