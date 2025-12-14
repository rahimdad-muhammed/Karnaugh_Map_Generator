import pygame
from copy import deepcopy

class MapGenerator:
	def __init__(self, settings) -> None:
		super().__init__()
		
		self.settings = settings # getting settings from the settings file

		self.col_in : int = int(len(settings.inputs_entering) // 2) # How many inputs top column will use -> int
		# How many inputs left row will use -> int
		self.row_in : int = int(len(settings.inputs_entering) - (len(settings.inputs_entering) // 2))

		# How many cells should I use for the top column -> int(input possibilities of the top column)
		settings.map_column : int = 2 ** (len(settings.inputs_entering) // 2)
		# How many cells should I use for the left row -> int (input possibilities of the left row)
		settings.map_row : int = 2 ** (len(settings.inputs_entering) - (len(settings.inputs_entering) // 2))

		self.cell_rect = pygame.Rect(0,0,80,60) # rect that gonna used to create map (I will copy it for many times)

		# Start POINT, and Start CELL
		self.cell_start = pygame.Rect(0,0,80,60)
		self.cell_start.topleft = (0, 0)
		# ************

	def generate_possibilities(self) -> None:
		"""
		This is a function for generating the possibilities of Top-Column and Left-Row
		"""
		self.settings.cleaning.light_cleaning(self.settings)


		# ****************** ADDING THE STARTING RECTANGLES OF THE TOP_COLUMN AND THE LEFT_ROW *************************************
		self.settings.cells_column.append(self.cell_start)
		self.settings.cells_row.append(self.cell_start)
		

		# ************************* GENERATING THE POSSIBILITIES OF THE TOP COLUMN ************************************
		
		# A loop for generating the input possibilities for the top column (2^n)
		# I will take the number of input possibilities used for the top column then turning it into a boolean expression
		# iterating through the number of column possibilities to turn every possibility to binary
		
		for binary in range(self.settings.map_column): # binary value is integer whole number


			self.settings.cells_column.append(deepcopy(self.cell_rect)) # Copying the default rect to the list
			self.settings.cells_column[-1].topleft = self.settings.cells_column[-2].topright # shift the rects to the right
			
			convert : str = f"{binary:b}" # A f-string method to convert a integer to a boolean value
			
			# If length of the boolean string is smaller than number of input type used on the top column then add zeros to the 
			# beginning of the string |v|
			# because even if you have 4 different input type you can get something like "10" it ignores the zeros in the beginning
			
			if len(convert) < self.col_in:
				multi = self.col_in - len(convert) # Calculating how many zeros I should add to the beginning of the string
				convert = f"{'0' * multi}" + convert # Adding the zeros to the beginning of the string

			# Adding the possibility of the top-column cells to the list as a Font (used for display the top-column possibilities)
			self.settings.column_possibilities.append(self.settings.font.render(f"{convert}", True, (0,255,0)))
			
			# Adding the actual result (boolean string) to another list (this list will be used to calculate result cells value)
			self.settings.calculation_values_column.append(f"{convert}")

		self.settings.cells_column.pop(0) # deleting the first rect because we dont need this anymore.
		

		# ***************************** GENERATING THE POSSIBILITIES OF THE LEFT ROW ***************************************
		
		# A loop for generating the input possibilities for the Left-Row (2^n)
		# I will take the number of input possibilities used for the left row then turning it into a boolean expression
		# iterating through the number of row possibilities to turn every possibility to binary
		
		for binary2 in range(self.settings.map_row): # binary2 value is integer whole number

			self.settings.cells_row.append(deepcopy(self.cell_rect)) # Copying the default rect to the list
			self.settings.cells_row[-1].topleft = self.settings.cells_row[-2].bottomleft # shifts the rect to the down
			
			convert2 = f"{binary2:b}" # A f-string method to convert a integer to a boolean value
			
			# If length of the boolean string is smaller than number of input type used on the left-row then add zeros to the 
			# beginning of the string |v| 
			# because even if you have 4 different input type you can get something like "10" it ignores the zeros in the beginning
			
			if len(convert2) < self.row_in:
				multi2 = self.row_in - len(convert2) # Calculatin how many zeros I should add to the beginning of the string
				convert2 = f"{'0' * multi2}" + convert2 # Adding the zeros to the beginning of the string

			# Adding the possibility of the left-row cells to the list as a Font (used for display the left row possibilities)
			self.settings.row_possibilities.append(self.settings.font.render(f"{convert2}", True, (0,255,0)))

			# ------------------------- OTHER CELLS SET UP-----------------------------------
			# Copying the Top Rect list for creating the other cells(result rects)
			self.settings.other_cells.append(deepcopy(self.settings.cells_column))
			self.settings.calculated_cells.append([])

			# A loop that shift down last element list of (horizontal) result rect lists
			for cells_index, other_cells in enumerate(self.settings.other_cells[-1]):
				# Shifting the rectangle to the down
				self.settings.other_cells[-1][cells_index].bottom = self.settings.cells_row[-1].bottom

				# Conjugenate the row boolean string value to column string value
				# combined string have same length of input_types_dictionary_keys
				self.settings.combine = f"{convert2}{self.settings.calculation_values_column[cells_index]}"

				# Iterating through the keys of input_type_dictionary_sorted to get the values of the input_types
				for order, value in enumerate(list(self.settings.input_value.keys())):
					# if boolean_string_index equals to "1" dictionary's input_type_value equals to True(1)
					if self.settings.combine[order] == "1":
						self.settings.input_value[value] = True

					else: # if boolean_string_index equals  to "0" dictionary's input_type_value equals to False(0)
						self.settings.input_value[value] = False

				# if the result of boolean equation is True then display 1 on the result rect
				# eval used to take the result of boolean equation that stored as a string
				if eval(self.settings.calculated) == True:
					self.settings.enter = "1"
				else: # if the result of the boolean equation is False then display 0 on the result rect
					self.settings.enter = "0"

				# Adding the displaying value as a Font value to the list(this list used to display the results "Q")
				self.settings.calculated_cells[-1].append(self.settings.font.render(self.settings.enter, True, (255,255,255)))

		
		if len(self.settings.column_possibilities) == 1:
			
			self.settings.column_possibilities[0] = self.settings.font.render("", True, (0,255,0))


		self.settings.cells_row.pop(0)

	def draw(self):
		"""
		A function for drawing the karnaugh map
		"""
			

		# ***************************** LEFT ROW AND RESULTS *********************************************
		# a loop for drawing the left-row, and result rect group
		for draw_index, draw_rect in enumerate(self.settings.cells_row):

			# ****************** Result Rectangles **********************
			# A loop for drawing the rectangle group inside the element list
			for draw_index2, draw_rect2 in enumerate(self.settings.other_cells[draw_index]):
				
				pygame.draw.rect(self.settings.k_map_bed, (255,255,255), draw_rect2, 3)

				#draws the results of the result rectangles True, False( 1 , 0 )
				self.settings.k_map_bed.blit(self.settings.calculated_cells[draw_index][draw_index2], self.settings.calculated_cells[draw_index][draw_index2].get_rect(center = (draw_rect2.center)))

			# *********************** LEFT ROW *********************************
			# Drawing the Left-Row Rect
			pygame.draw.rect(self.settings.k_map_bed, (0,0,0), draw_rect)
			pygame.draw.rect(self.settings.k_map_bed, (255,255,255), draw_rect, 3)

			# Drawing the possibility of Left-Row(boolean string) Font, Rect
			self.settings.k_map_bed.blit(self.settings.row_possibilities[draw_index], self.settings.row_possibilities[draw_index].get_rect(center = (draw_rect.center)))


		# ***************************** TOP COLUMN ***********************************************
		# a loop for drawing the top-column rect group
		for draw_index, draw_rect in enumerate(self.settings.cells_column):

			# Drawing the top Column Rect
			pygame.draw.rect(self.settings.k_map_bed, (0,0,0), draw_rect)
			pygame.draw.rect(self.settings.k_map_bed, (255,255,255), draw_rect, 3)

			# Drawing the possibility of Top-Column(boolean string) Font,Rect
			self.settings.k_map_bed.blit(self.settings.column_possibilities[draw_index], self.settings.column_possibilities[draw_index].get_rect(center = (draw_rect.center)))


		# Draw the left-top Cell (Starting Rectangle)
		pygame.draw.rect(self.settings.k_map_bed, (0,0,0), self.cell_start)
		pygame.draw.rect(self.settings.k_map_bed, (255,255,255), self.cell_start, 3)
		

	def update(self):
		if self.settings.generate_map: # if the generate_map mode is open then do these functions
			self.generate_possibilities()
			# After every map generation step is done then turn of the generate_map mode
			self.settings.generate_map = False

		# draw the karnaugh map
		self.draw()





















