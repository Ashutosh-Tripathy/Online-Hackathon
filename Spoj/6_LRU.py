class LRU:
    def __init__(self):
        self.queue = []
        self.hashValue = {}

    def get_value(self, page_number):
        if page_number not in hashValue:
            return None
        
