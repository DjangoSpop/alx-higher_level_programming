#!/usr/bin/python3
class Square:
    def __init__(self, size):
        # This is the magic box (square), and 'size' is the special thing inside it.
        # We're locking the box (making 'size' private) to keep it safe.
        self.__size = size

    def calculate_area(self):
        # This method helps us find out how much space is inside the square.
        # We're following special rules to do this.
        return self.__size * self.__size

# Let's create a square and use it:

# We make a new square with a size of 5.
my_square = Square(5)

# Now, let's find out how much space is inside our square using the special method.
area = my_square.calculate_area()

# We can print the result:
print("The area of my square is:", area)
   