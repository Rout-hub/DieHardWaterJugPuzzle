print("\nThe Water Jug Puzzle from Die Hard 3!\n\n")
print("The set up:  You have two empty jugs: a 5 gallon jug and a 3 gallon jug.\n")
print("Object of game: To get exactly 4 gallons of water into the 5 gallon jug.")
print("You can fill a jug, pour one jug into the other, or empty a jug.\n")

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
        
    #pouring water from one jug into another. This is for the receiving jug.
    def push(self, value):
        if self.has_space():
            volume_to_add = self.limit - self.currentvolume
            if value > volume_to_add:
                self.currentvolume += volume_to_add
            else:
                self.currentvolume += value
        else:
            print("The {} is already full.".format(self.name))

    #emptying a jug        
    def pop(self):
        if not self.is_empty():
            amt_poured_out = self.currentvolume
            self.currentvolume = 0
            return amt_poured_out
        else:
            print("The {} is empty.".format(self.name))

    #pouring from one jug to another. This is the jug that is being poured.
    def pour(self, value):
        if not self.is_empty():
            if self.currentvolume > value:
                self.currentvolume -=value
                return self.currentvolume
            else:
                self.currentvolume = 0
                return self.currentvolume
        else:
            print("{} is already empty.".format(self.name))



def list_of_moves(): 
    print("\nSelect one of the following:\n")
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
print("\nLet's get started!\n")


print("Select one of the following to start:\n")
print("1 to Fill Large Jug")
print("2 to Fill Small Jug\n")
print("What do you want to do?: ")
user_input = input("")



if user_input != "1" and user_input != "2":
    print("Invalid response. Try again.")
elif user_input == "1":
    large_jug.fill()
    print(large_jug)
    print(small_jug)
else:
    small_jug.fill()
    print(large_jug)
    print(small_jug)

while(large_jug.peek() != 4):

    list_of_moves()

    print("\nNext move? ")
    user_input = input("")
    
    #Fill large jug.
    if user_input == "1":
        current_volume = large_jug.peek()
        if current_volume == large_jug.limit:
            print("Large jug is full. Please try again.")
        else:
            large_jug.fill()
            print(large_jug)
            print(small_jug)
    
    #Fill small jug.
    elif user_input == "2":
        current_volume = small_jug.peek()
        if current_volume == small_jug.limit:
            print("Small jug is full. Please try again.")
        else:
            small_jug.fill()
            print(large_jug)
            print(small_jug)
    
    #Pour large jug into small jug.
    elif user_input == "3":
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
        elif large_jug_volume <= added_vol:
            small_jug.push(large_jug_volume)
            large_jug.pour(large_jug_volume)
            print(large_jug)
            print(small_jug)

    #Pour small jug into large jug.
    elif user_input == "4":
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
    
    #Empty large jug.
    elif user_input == "5":
        large_jug.pop()
        print(large_jug)
        print(small_jug)
    
    #Empty small jug.
    elif user_input == "6":
        small_jug.pop()
        print(large_jug)
        print(small_jug)   

    else:
        print("Invalid response. Please try again")    

print("\n\nCONGRATULATIONS!!! \n\nThe large jug has 4 gallons of water in it.  You've solved the puzzle.\n\n")
#The end
