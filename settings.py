import pygame
from pygame.font import Font
from pygame.math import Vector2

pygame.init()

# User Keyboard Input
operations : tuple = ("+","^") # the operations user chan enter

# setting prime mode, used for creating user equations and drawing the prime lines
prime: bool = False 

# Stores everythings that user entered, Used for displaying on the screen
user_input : list[str] = []

# USER INTERACTIONS SET UP 
user_interactions = None # stores UserInteractions class

# Text box set up 
# the font that gonna used for the whole program
font : Font = Font(None, 30)

# The top left location of the text box
text_location : Vector2 = Vector2(50, 50)

prime_group : int = 0 # prime_eq group counter

# Width of the text box that user enters something
text_rect_width : int = 0

prime_line : dict[list] = {} # stores starting and finishing point of the line

text_box = None # stores TextBox class

# DICTIONARY MANAGER SET UP
# when user deletes something make sure applying change to the dictionaries so we are checking if we should apply change or not to dictionary
delete : bool = False

# we storing each not() function inside of the dictionary with keys of int each time we entered a not function the key_value also increases
# when we delete a not group completely then we removing that value from the dictionary
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
calculation_values_row : list[str] = []
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

# SETTING THE CLEAR BUTTON
# Setting the text for the button
clear_font = font.render("CLEAR", True, (120,120,255))
# getting rect of the clear text to place it into somewhere nice
clear_rect = clear_font.get_rect(topleft = (60,120))
# the background of the Clear button 
clear_button_rect = pygame.Rect(0,0, (clear_rect.right - clear_rect.left) + 40, (clear_rect.bottom - clear_rect.bottom) + 40)
# setting the position of the background of the clear button
clear_button_rect.center = clear_rect.center


tutorial_table = None # Stores the TutorialTable class

table_format = None # Stores the TableFormat class

# stores which format the user want to display the table, the default is "row"
format = "row"

# stores which inputs used for the left-row
row_inputs = ""
# stores which inputs used for the top column
column_inputs = ""

# getting the top-left cordinates of the K-Map table on the screen because K-map lives in another dimension
cell_start = pygame.Rect(0,0,80,60)
cell_start.topleft = (200,110)

# The triangle colours of the rect that lives on the top-left of K-Map, the default is black
# the colours will change when you move your mouse onto them
triangle_column_colour = (0,0,0)
triangle_row_colour = (0,0,0)

# stores which inputs wants to display when user move the mouse onto the triangles, top-column inputs or left-row inputs
display_input = "display_none"
# stores the row inputs as a surface to display when the user move the mouve onto the triangles
row_inputs_surf = font.render(row_inputs,True, (0,0,255))
# stores the column inputs as a surface to display when the user move the mouve onto the triangles
column_inputs_surf = font.render(column_inputs,True, (0,0,255))
# placing the input surface into a nice place
row_inputs_rect = row_inputs_surf.get_rect(center = (0,0))
column_inputs_rect = column_inputs_surf.get_rect(center = (0,0))
# background of the row-inputs surface
row_inputs_box = pygame.Rect(0,0,(row_inputs_rect.right - row_inputs_rect.left)+20,
							 (row_inputs_rect.bottom - row_inputs_rect.top)+20)
# placing the background
row_inputs_box.midright = cell_start.midleft

# background of the column-inputs surface
column_inputs_box = pygame.Rect(0,0, (column_inputs_rect.right - column_inputs_rect.left) + 20,
								(column_inputs_rect.bottom - column_inputs_rect.top)+20)
# placing the background
column_inputs_box.midbottom = cell_start.midtop

# stores the mouse_pos
mouse_pos = (0,0)

# Stores the Instructions class
instructions = None

# Grabbing the table with mouse, value activated when you click to the table
move = False

# the default scrolling speed of the table
speed = 10










