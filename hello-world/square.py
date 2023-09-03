
class Square:
    def __init__(self):
          self.__height = 2
          self.__width = 2
    def set_side(self, new_side):
          self.__height = new_side
          self.__width = new_side

square = Square()
square.__height = 3 # raises AttributeError

# Create a square with the default side length of 2
my_square = Square()
print(f"Height: {my_square.height}, Width: {my_square.width}")

# Change the side length to 5
my_square.set_side(5)
print(f"Height: {my_square.height}, Width: {my_square.width}")
