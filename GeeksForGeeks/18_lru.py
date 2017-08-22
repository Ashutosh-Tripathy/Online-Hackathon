class LRU:
    def __init__(self, size):
        self.size = size
        self.queue = []
        self.key_value = {}

    def get(self, key):
        value = self.key_value[key] if key in self.key_value else -1
        return value

    def set(self, key, value):
        if key in self.queue:
            self.queue.remove(key)
        elif len(self.queue) == self.size:
            item = self.queue.pop(0)
            del self.key_value[item]
        self.queue.append(key)
        self.key_value[key] = value
