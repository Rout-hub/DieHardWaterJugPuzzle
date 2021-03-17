print("Let's play the Water Jug game from Die Hard 3!\n\n")
print("The set up:  You have two empty jugs: a 5 gallon and a 3 gallon.")
print("Object of game: To get exactly 4 gallons of water into the 5 gallon jug.")
print("You can fill a jug, pour one jug into the other, or empty a jug.")

class Node:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_node):
        self.next_node = new_node

class Jug:
    def __init__(self, limit = None):
        self.top_item = None
        self.limit = limit
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def has_space(self):
        return self.limit > self.size

    def peek(self):
        if not is_empty():
            return self.top_item.get_value()
        else:
            print("The jug is empty.")

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            print(value)
            self.size += 1
        else:
            print("The jug is full.")
            
    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            ("The jug is empty.")
            
