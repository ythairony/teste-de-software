class Pilha:
    def __init__(self):
        self.items = []

    
    def enqueue(self, item):
        self.items.append(item)


    def dequeue(self):
        self.items.pop(len(self.items)-1)


    def is_empty(self):
        return len(self.items) == 0
    

    def length(self):
        return len(self.items)




