import pygame

class Cleaning:
	
	def __init__(self):
		super().__init__()

	def light_cleaning(self, settings):
		# CLEANING
		# Reseting the Top-Column Rectangles
		settings.cells_column.clear()
		# Reseting the Left-Row Rectangles
		settings.cells_row.clear()
		# other cells
		settings.other_cells.clear()
		settings.calculated_cells.clear()
		###########################################
		# Reseting the Top-Column-Possibilities(boolean) values
		settings.column_possibilities.clear()
		settings.calculation_values_column.clear()
		# Reseting the Left-Row-possibilities(boolean) values
		settings.row_possibilities.clear()
		settings.calculation_values_row.clear()
		# ****************************************************

		settings.row_inputs = ""
		settings.column_inputs = ""

		settings.row_inputs_surf = settings.font.render(settings.row_inputs,True, (0,0,255))
		settings.column_inputs_surf = settings.font.render(settings.column_inputs,True, (0,0,255))

		settings.row_inputs_rect = settings.row_inputs_surf.get_rect(center = (0,0))
		settings.column_inputs_rect = settings.column_inputs_surf.get_rect(center = (0,0))

		settings.row_inputs_box = pygame.Rect(0,0,(settings.row_inputs_rect.right - settings.row_inputs_rect.left)+20,
											  (settings.row_inputs_rect.bottom - settings.row_inputs_rect.top)+20)

		settings.row_inputs_box.midright = settings.cell_start.midleft


		settings.column_inputs_box = pygame.Rect(0,0, (settings.column_inputs_rect.right - settings.column_inputs_rect.left) + 20,
												 (settings.column_inputs_rect.bottom - settings.column_inputs_rect.top)+20)

		settings.column_inputs_box.midbottom = settings.cell_start.midtop

	def deep_cleaning(self, settings):

		settings.prime = False

		settings.user_input.clear()

		settings.prime_group : int = 0 

		settings.prime_line.clear()

		settings.delete : bool = False
		settings.del_group = None

		settings.inputs_entering.clear()
		settings.copy_inputs_entering.clear()

		settings.cells_column.clear()
		settings.cells_row.clear()

		settings.other_cells.clear()

		settings.column_possibilities.clear()
		settings.row_possibilities.clear()

		settings.calculate.clear()
		settings.calculated = None

		settings.calculation_values_column.clear()
		settings.calculation_values_row.clear()
		settings.combine = None

		settings.calculated_cells.clear()

		settings.input_value.clear
		
		settings.generate_map : bool = False

		settings.error = "Nothing" # stores the error situation

		settings.row_inputs = ""
		settings.column_inputs = ""

		settings.row_inputs_surf = settings.font.render(settings.row_inputs,True, (0,0,255))
		settings.column_inputs_surf = settings.font.render(settings.column_inputs,True, (0,0,255))

		settings.row_inputs_rect = settings.row_inputs_surf.get_rect(center = (0,0))
		settings.column_inputs_rect = settings.column_inputs_surf.get_rect(center = (0,0))

		settings.row_inputs_box = pygame.Rect(0,0,(settings.row_inputs_rect.right - settings.row_inputs_rect.left)+20,
											  (settings.row_inputs_rect.bottom - settings.row_inputs_rect.top)+20)

		settings.row_inputs_box.midright = settings.cell_start.midleft


		settings.column_inputs_box = pygame.Rect(0,0, (settings.column_inputs_rect.right - settings.column_inputs_rect.left) + 20,
												 (settings.column_inputs_rect.bottom - settings.column_inputs_rect.top)+20)

		settings.column_inputs_box.midbottom = settings.cell_start.midtop



