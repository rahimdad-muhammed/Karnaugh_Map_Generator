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
		# Reseting the Left-Row-possibilities(boolean) values
		settings.row_possibilities.clear()
		settings.calculation_values_column.clear()
		# ****************************************************

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
		settings.combine = None

		settings.calculated_cells.clear()

		settings.input_value.clear
		
		settings.generate_map : bool = False

		settings.error = "Nothing" # stores the error situation



