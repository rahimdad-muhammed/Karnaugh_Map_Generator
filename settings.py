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
font : Font = Font(None, 30)

text_location : Vector2 = Vector2(50, 50)

prime_group : int = 0 # group counter
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

cells_column : list[tuple] = []
cells_row : list[tuple] = []

# other cells set up
other_cells : list[list[tuple]] = []
cells_bottom : list[int] = []

column_possibilities : list[str] = []# surface
row_possibilities : list[str] = [] # surface

column_surface_rect : list = [] # stores rect for cordinates
row_surface_rect : list = [] # stores rect for cordinates



""" calculation variables """
calculate : list = []

calculated : str = None

calculation_values_column : list[str] = [] # stores booleans as a string for columns
calculation_values_row : list[str] = [] # stores booleans as a string for rows
combine : str = None # combines the column and row values

calculated_cells : list[bool] = [] # stores calculations as a surface
calculated_rect : list[tuple] = [] # cordinates of the calculated cells

enter : str = None

input_value : dict[str, bool] = {}

generate_map : bool = False

map_generator = None # stores MapGenerator class























