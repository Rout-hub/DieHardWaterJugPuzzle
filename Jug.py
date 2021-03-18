print("Let's play the Water Jug game from Die Hard 3!\n\n")
print("The set up:  You have two empty jugs: a 5 gallon and a 3 gallon.")
print("Object of game: To get exactly 4 gallons of water into the 5 gallon jug.")
print("You can fill a jug, pour one jug into the other, or empty a jug.")

class Jug:
    def __init__(self, name, limit = None):
        self.name = name
        self.currentvolume = 0
        self.limit = limit

    def __repr__(self):
        return "The {} has {} gallons of water in it.".format(self.name, self.currentvolume)

    def fill(self):
        self.currentvolume = self.limit
        return self.currentvolume        

    def is_empty(self):
        return self.currentvolume == 0

    def has_space(self):
        return self.limit > self.currentvolume

    def peek(self):
        return self.currentvolume
        

    def push(self, value):
        if self.has_space():
            if value > self.limit - self.currentvolume:
                addedvolume = self.limit - self.currentvolume
                self.currentvolume += addedvolume
                print("{} now has {} gallons in it.".format(self.name, self.currentvolume))
            else:
                self.currentvolume += value
                print("{} now has {} gallons in it.".format(self.name, self.currentvolume))
        else:
            print("The jug is full.")
            
    def pop(self):
        if not self.is_empty():
            amt_poured_out = self.currentvolume
            self.currentvolume = 0
            return amt_poured_out
        else:
            ("The jug is empty.")

    def pour(self, value):
        if not self.is_empty():
            if self.currentvolume > value:
                self.currentvolume -=value
                return self.currentvolume
            else:
                self.currentvolume = 0
                return current_volume
        else:
            print("{} is already empty.".format(self.name))



def list_of_moves(): 
    print("Select one of the following:\n")
    print("1 to Fill Large Jug")
    print("2 to Fill Small Jug")
    print("3 to Pour Large Jug into Small Jug")
    print("4 to Pour Small Jug into Large Jug")
    print("5 to Empty Large Jug")
    print("6 to Empty Small Jug")


large_jug = Jug("Large Jug", 5)
small_jug = Jug("Small Jug", 3)

print(large_jug)
print(small_jug)

#Start game
print("Let's get started!\n")


print("Select one of the following to start:\n")
print("1 to Fill Large Jug")
print("2 to Fill Small Jug")
print("What do you want to do?: ")
user_input = int(input(""))



if user_input != 1 and user_input != 2:
    print("Invalid response. Try again.")
elif user_input == 1:
    print("You chose 1")
    large_jug.fill()
    print(large_jug)
    print(small_jug)
else:
    print("You chose 2")
    small_jug.fill()
    print(large_jug)
    print(small_jug)

#while(large_jug.peek() != 4):
list_of_moves()

print("Next move? ")
user_input = int(input(""))

if user_input == 1:
    current_volume = large_jug.peek()
    if current_volume == large_jug.limit:
        print("Jug is full. Try again.")
    else:
        large_jug.fill()
        print(large_jug)
        print(small_jug)
elif user_input == 2:
    current_volume = small_jug.peek()
    if current_volume == small_jug.limit:
        print("Jug is full. Try again") 
    else:
        small_jug.fill()
        print(large_jug)
        print(small_jug)
elif user_input == 3:
    large_jug_volume = large_jug.peek()
    small_jug_volume = small_jug.peek()
    added_vol = small_jug.limit - small_jug_volume
    if small_jug_volume == small_jug.limit:
        print("Small jug is already full. Try again.") 
    elif large_jug_volume == 0:
        print("Large jug is empty. Try again.") 
    elif large_jug_volume > added_vol:
        small_jug.fill()
        large_jug.pour(added_vol)
        print(large_jug)
        print(small_jug)

elif user_input == 4:
    large_jug_volume = large_jug.peek()
    small_jug_volume = small_jug.peek()
    added_vol = large_jug.limit - large_jug_volume
    if large_jug_volume == large_jug.limit:
        print("Large jug is already full. Try again.") 
    elif small_jug_volume == 0:
        print("Small jug is empty. Try again.") 
    elif small_jug_volume > added_vol:
        large_jug.fill()
        small_jug.pour(added_vol)
        print(large_jug)
        print(small_jug)
    elif small_jug_volume < added_vol:
        large_jug.push(small_jug_volume)
        small_jug.pop()
        print(large_jug)
        print(small_jug)
        






