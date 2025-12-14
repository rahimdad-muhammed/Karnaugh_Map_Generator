import pygame
from pygame.font import Font
from pygame.math import Vector2

pygame.init()

""" User Keyboard Input """
operations : tuple = ("+","^")

prime: bool = False

user_input : list[str] = []


""" USER INTERACTIONS SET UP """
user_interactions = None # stores UserInteractions class

""" Text box set up """
# the font that gonna used for the whole program
font : Font = Font(None, 30)

# The top left location of the text box
text_location : Vector2 = Vector2(50, 50)

prime_group : int = 0 # group counter
# Width of the text box that user enters something
text_rect_width : int = 0
prime_line : dict[list] = {} # stores starting and finishing point of the line

text_box = None # stores TextBox class

""" DICTIONARY MANAGER SET UP """
delete : bool = False
del_group : int = None

dict_manage = None # stores DictManager class


""" Map generator_ cell generate set up """
inputs_entering : list = [] # input types that gonna used to create map like inputA inputB
copy_inputs_entering : list = [] # copy of input types with sorted version

""" LEFT-ROW AND TOP COLUMN """
# Stores the top column rects
cells_column : list[tuple] = []
# Stores the left row rects
cells_row : list[tuple] = []
""" ---------------------------------- """

# other cells (result rect)
other_cells : list[list[tuple]] = []

column_possibilities : list[str] = []# Stores Right-Column surface boolean
row_possibilities : list[str] = [] # Stores Left_Row surface boolean



""" calculation variables """
# Stores the functions the user wants to enter 
# used for calculate the results
calculate : list = []

# joined version of calculate list (used for to be used in eval function)
calculated : str = None

calculation_values_column : list[str] = [] # stores booleans as a string for columns
combine : str = None # combines the column and row values

calculated_cells : list[bool] = [] # stores calculations as a surface(calculations of result rects Q)

# The inputs that user entered(each input key stores boolean value
input_value : dict[str, bool] = {}

# If user enters to enter then create the map
generate_map : bool = False

map_generator = None # stores MapGenerator class

# the surface that the karnaugh map showed on
k_map_bed = None

move_map = None # Stores the MoveMap Class


# SCREEN dimensions
screen = None
screen_w = None
screen_h = None

you_cant = None # Stores the YouCant class

error = "Nothing" # stores the error situation

clear_font = font.render("CLEAR", True, (120,120,255))
clear_rect = clear_font.get_rect(topleft = (60,120))

clear_button_rect = pygame.Rect(0,0, (clear_rect.right - clear_rect.left) + 40, (clear_rect.bottom - clear_rect.bottom) + 40)
clear_button_rect.center = clear_rect.center


tutorial_table = None # Stores the TutorialTable class






















