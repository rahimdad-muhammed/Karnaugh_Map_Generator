import pygame
class UserInteractions:
	def __init__(self, event, settings):
		
		self.settings = settings
		self.event = event

	def keyboard(self):
		""" Handling ALL the keyboard inputs """
		
		if self.event.type == pygame.KEYDOWN:

			self.settings.error = "Nothing"

			if pygame.K_0 <= self.event.key <= pygame.K_1:

				number_pressed = self.event.key - pygame.K_0

				if number_pressed == 1: # TRUE

					self.settings.user_input.append("1")

					if (len(self.settings.calculate) > 0) and (self.settings.calculate[-1] != "^ ") and (self.settings.calculate[-1] != "or ") and (self.settings.calculate[-1] != "not("):
				
						self.settings.calculate.append("and ")
						self.settings.calculate.append("True ")

					else: # if one of the conditions fails then just add the input type to the list
						self.settings.calculate.append("True ")

				#  ***********************************
					

				else: # if not 1 then its 0 FALSE
					self.settings.user_input.append("0")

					if (len(self.settings.calculate) > 0) and (self.settings.calculate[-1] != "^ ") and (self.settings.calculate[-1] != "or ") and (self.settings.calculate[-1] != "not("):
				
						self.settings.calculate.append("and ")
						self.settings.calculate.append("False ")

					else: # if one of the conditions fails then just add the input type to the list
						self.settings.calculate.append("False ")

				#  ***********************************
					
			# ************************** IF ANY LETTER IS PRESSED ADD TO THE LIST ***************************************
			if pygame.K_a <= self.event.key <= pygame.K_z:	

				letter_pressed = str(chr(self.event.key)).upper() # capitalize the letter
				
				self.settings.user_input.append(letter_pressed) # adding the letter to the list that gonna showed on the screen

				# If  there is multiple expressions showed on the screen
				# if the calculate list NOT ended with any opeation (^, +)
				# if the calculate list NOT ended with not( 
				# Then add the and operator before the input type to the list,
				# after the ") ", "input_type" the and operator will be added
				if (len(self.settings.calculate) > 0) and (self.settings.calculate[-1] != "^ ") and (self.settings.calculate[-1] != "or ") and (self.settings.calculate[-1] != "not("):
				
					self.settings.calculate.append("and ")
					self.settings.calculate.append(f"self.settings.input_value['{letter_pressed}'] ")

				else: # if one of the conditions fails then just add the input type to the list
					self.settings.calculate.append(f"self.settings.input_value['{letter_pressed}'] ")

				#  ***********************************

				# If new input type is used then add this input type to the input_types list
				if letter_pressed not in self.settings.inputs_entering:		
					self.settings.inputs_entering.append(letter_pressed)

			# ************************************************************************************************************************
					

			# **************************** USER PRESSED TO THE "+" OR "^" OPERATION THEN ADD TO THE LIST ************************
				
			#""" If user operation is valid then add to the list """
			elif self.event.unicode in self.settings.operations:

				self.settings.user_input.append(str(self.event.unicode)) # user input that showed on the screen

				# add the operation to the calculation list in the proper format 
				# (this list used to calculate results of the result rects)
				if self.event.unicode == "^":
					self.settings.calculate.append("^ ")
				else:
					self.settings.calculate.append("or ")

			# ***********************************************************************************************************************

			# ***************************** IF PRESSED TO THE SPACE KEY THEN SET PRIME MODE OF OR ON ********************************
			
			#""" If pressed to the space key than prime set to """
			elif self.event.key == pygame.K_SPACE:

				############################################# SET PRIME TO TRUE #####################################################
				# If prime mode is on that means user wants to turn it of so set the prime to the False
				if self.settings.prime:
					self.settings.prime = False

					# if user turned the prime mode of that means we have to end the prime line 
					# so add the finish point to the prime_line_list
					self.settings.text_box.prime_line()
					self.settings.prime_line[self.settings.prime_group].append((self.settings.text_rect_width, 48)) # finish line

					# CALCULATE THE USER INPUT

					# if user entered something at least one thing then check if the calculate list ended with "not("
					# because if the list ended with "not(" that means user dont want to add any "not(" expression yet so just delete it
					if len(self.settings.calculate) >= 1:
						if self.settings.calculate[-1] == "not(":
							self.settings.calculate.pop(-1)

							# if there still some operations before the "not(" and the "and " operator used right before it then delete
							if len(self.settings.calculate) >= 1:
								if self.settings.calculate[-1] == "and ":
									self.settings.calculate.pop(-1)
							
						else: # if user want to end the not expression than finish the not expression so add ") "
							self.settings.calculate.append(") ")

				#######################################################################################################################

				############################################# SET PRIME TO FALSE #####################################################
				# IF THE USER WANT TO TURN ON THE PRIME MODE
				else:
					self.settings.prime = True # turn on the prime mode
					self.settings.prime_group += 1 # user will enter new not expression group

					# Add the new key to the dictionary that stores starting and finish point of the prime lines
					# Uses the prime group number as a key
					self.settings.text_box.prime_line()
					self.settings.prime_line[self.settings.prime_group] = [(self.settings.text_rect_width, 48)] # start line

					# If user want to start the prime mode while there is no expression entered yet then just add "not(" operation
					if len(self.settings.calculate) == 0:
						self.settings.calculate.append("not(")

					# If the calculate list ended with "^ " or "or " operator then just add "not(" operation
					elif self.settings.calculate[-1] == "^ " or self.settings.calculate[-1] == "or ":
						self.settings.calculate.append("not(")

					# If the calculate list ended with any "input_type" or the ending of the not not expression ") " 
					# then add both "and " and "not(" operation
					else:
						self.settings.calculate.append("and ")
						self.settings.calculate.append("not(")

				#######################################################################################################################
			
			# **************************************************************************************************************************
							

			# *********************** IF THE USER PRESSED TO THE BACKSPACE THEN DELETE LAST ELEMENT ************************************
			
			#""" IF USER PRESS TO THE BACKSPACE THEN DELETE LAST ELEMENT """
			elif self.event.key == pygame.K_BACKSPACE and len(self.settings.user_input) >= 1:

				# Delete the last element of the list that displayed on the screen
				self.settings.user_input.pop(-1)

				# delete the input type
				if len(self.settings.inputs_entering) >= 1:
					# If the last element of the input_types list is not displayed on the screen that means the user not using that 
					# kind of input type anymore so remove the input type from the list
					if self.settings.inputs_entering[-1] not in self.settings.user_input: 
						self.settings.inputs_entering.pop(-1)

				# CALCULATE THE USER INPUT
				# if the calculate list ended with ") " then we have delete the element before it(input_type, "^", "or ")
				if self.settings.calculate[-1] == ") ":
					self.settings.calculate.pop(-1)
					self.settings.calculate.pop(-1)

					if len(self.settings.calculate) >= 1:
						# if there is "and " operator used before the element input_type then delete it from the list
						if self.settings.calculate[-1] == "and ":
							self.settings.calculate.pop(-1)

					if len(self.settings.calculate) >= 1:
						# if the "not(" operator used before the element then delete it to
						if self.settings.calculate[-1] == "not(":
							self.settings.calculate.pop(-1)
							self.settings.prime = False

							if len(self.settings.calculate) >= 1:
								# if the "and " operator used before the "not( " operator then delete it to
								if self.settings.calculate[-1] == "and ":
									self.settings.calculate.pop(-1)

						# if the list not ended with "not(" operation that means the "not(" operation is still used and it's not closed
						# so close it
						else:
							self.settings.calculate.append(") ")


				else: # if the last element of element NOT ended with ") " then delete just the last element
					if self.settings.calculate[-1] == "not(":
						self.settings.calculate.pop(-1)
						self.settings.prime = False

						if self.settings.calculate[-1] == "and ":
							self.settings.calculate.pop(-1)
							# Deleting the input type comes before the "and "
							self.settings.calculate.pop(-1)

							if self.settings.calculate[-1] == "and ":
								self.settings.calculate.pop(-1)

					else:
						self.settings.calculate.pop(-1)

						if len(self.settings.calculate) >= 1:
							# if the "and " operator used before the deleted element then delete it to
							if self.settings.calculate[-1] == "and ":
								self.settings.calculate.pop(-1)

					
			# ********************************** IF USER WANTS TO CREATE THE MAP **************************************************

			#Create the map
			elif self.event.key == pygame.K_RETURN:

				if len(self.settings.inputs_entering) < 1: ### Create a new functionality for here
					self.settings.error = "no_input_type"
					# CLEANING
					self.settings.cleaning.light_cleaning(self.settings)
					
					print("You have to enter at least one input type.")

				elif self.settings.user_input[0] in self.settings.operations or self.settings.user_input[-1] in self.settings.operations: # Create a new functionality for here
					self.settings.error = "cant_start_end"
					# CLEANING
					self.settings.cleaning.light_cleaning(self.settings)
					print("The boolean equation cant start or end with or('+'), xor('^') operators")

				else:
					for input_index, input in enumerate(self.settings.user_input):
						if input in self.settings.operations and self.settings.user_input[input_index + 1] in self.settings.operations:
							self.settings.error = "next_to_next"
							self.settings.cleaning.light_cleaning(self.settings)
							break

						if input_index == len(self.settings.user_input) - 2 or input_index == len(self.settings.user_input) - 1:
							self.settings.generate_map = True
							break

				
				if self.settings.prime: # If user didn't close the prime mode then close it automatically
					self.settings.prime = False

					self.settings.text_box.prime_line()
					self.settings.prime_line[self.settings.prime_group].append((self.settings.text_rect_width, 48)) # finish line

					# CALCULATE THE USER INPUT

					if len(self.settings.calculate) >= 1:
						if self.settings.calculate[-1] == "not(":
							self.settings.calculate.pop(-1)

							if len(self.settings.calculate) >= 1:
								if self.settings.calculate[-1] == "and ":
									self.settings.calculate.pop(-1)
										
						
							
						else:
							self.settings.calculate.append(") ")


			print(f"{'Calculate list-> str:':<25} {''.join(self.settings.calculate)}")
			print(f"{'Inputs_Type(unique):':<25} {self.settings.inputs_entering}")
			print(f"{'User_Input(display):':<25} {self.settings.user_input}")
			print(f"{'Prime(boolean):':<25} {self.settings.prime}")
			print(f"{'Prime_Group:':<25} {self.settings.prime_group}")
			print()


		# ------------------------------------------------ MOUSE ACTIONS --------------------------------------------------------------

		if self.event.type == pygame.MOUSEWHEEL and len(self.settings.cells_row) > 0 and len(self.settings.cells_column) > 0:


			# Vertical Scrolling $$$$$$$$$$$$$$$$$$$$$
			# Scrolling to the up
			if self.event.y > 0 and self.settings.cells_row[-1].bottom > 120:
				
				self.settings.move_map.scroll_up()
				
				if self.settings.cells_row[-1].bottom < 120:
					
					self.settings.speed = 120 - self.settings.cells_row[-1].bottom
					
					self.settings.move_map.scroll_down()

					self.settings.speed = 10

			# Scrolling to the down
			if self.event.y < 0 and self.settings.cells_row[0].top < 60:
				
				self.settings.move_map.scroll_down()

				if self.settings.cells_row[0].top > 60:

					self.settings.speed = self.settings.cells_row[0].top - 60

					self.settings.move_map.scroll_up()

					self.settings.speed = 10

			# Horizontal Scrolling $$$$$$$$$$$$$$$$$4
			# Scrolling to the right
			if self.event.x > 0 and self.settings.cells_column[0].left < 80:
				
				self.settings.move_map.scroll_right()

				if self.settings.cells_column[0].left > 80:

					self.settings.speed = self.settings.cells_column[0].left - 80

					self.settings.move_map.scroll_left()

					self.settings.speed = 10

			# Scrolling to the left
			if self.event.x < 0 and self.settings.cells_column[-1].right > 160:
				
				self.settings.move_map.scroll_left()

				if self.settings.cells_column[-1].right < 160:

					self.settings.speed = 160 - self.settings.cells_column[-1].right

					self.settings.move_map.scroll_right()

					self.settings.speed = 10

				

		if self.event.type == pygame.MOUSEBUTTONDOWN:
			
			if self.event.button == 1:

				# clear button 
				if self.settings.clear_button_rect.collidepoint(self.event.pos):
					self.settings.cleaning.deep_cleaning(self.settings)

				# choosing format
				elif self.settings.table_format.format_row_rect.collidepoint(self.event.pos):
					self.settings.table_format.clicked("row", self.settings)
					self.settings.generate_map = True

				elif self.settings.table_format.format_column_rect.collidepoint(self.event.pos):
					self.settings.table_format.clicked("column", self.settings)
					self.settings.generate_map = True

				# move the table by grabbing with mouse
				elif len(self.settings.cells_column) > 0:
					if self.event.pos[0] <= (self.settings.cell_start.left + self.settings.cells_column[-1].right):
						if self.event.pos[1] <= (self.settings.cell_start.top + self.settings.cells_row[-1].bottom):
							if self.event.pos[0] > self.settings.cell_start.left and self.event.pos[1] > self.settings.cell_start.top:

								self.settings.move = True
					
								self.settings.previous = self.event.pos

								print(f"({self.settings.cells_column[-1].right}, {self.settings.cells_row[-1].bottom})")

		if self.event.type == pygame.MOUSEBUTTONUP:

			self.settings.move = False
			self.settings.speed = 10

	
		if self.event.type == pygame.MOUSEMOTION:

			self.settings.mouse_pos = self.event.pos

			# if mouse touching to info circle or not 
			if self.settings.cell_start.collidepoint(self.event.pos):
				
				self.settings.map_generator.display_inputs(self.event.pos, 80, 60)
				

			else:
				self.settings.triangle_column_colour = (0,0,0)
				self.settings.triangle_row_colour = (0,0,0)
				self.settings.display_input = "display_none"

			# moving the table
			if self.settings.move:
				# move to the left
				if self.event.pos[0] < self.settings.previous[0] and self.settings.cells_column[-1].right > 160:

					self.settings.speed = self.settings.previous[0] - self.event.pos[0]

					self.settings.move_map.scroll_left()
					
					self.settings.previous = (self.event.pos[0], self.settings.previous[1])

					if self.settings.cells_column[-1].right < 160:

						self.settings.speed = 160 - self.settings.cells_column[-1].right

						self.settings.move_map.scroll_right()



				# move to the right
				if self.event.pos[0] > self.settings.previous[0] and self.settings.cells_column[0].left < 80:

					self.settings.speed = self.event.pos[0] - self.settings.previous[0]

					self.settings.move_map.scroll_right()

					self.settings.previous = (self.event.pos[0], self.settings.previous[1])

					if self.settings.cells_column[0].left > 80:

						self.settings.speed = self.settings.cells_column[0].left - 80

						self.settings.move_map.scroll_left()


				# move to the down
				if self.event.pos[1] > self.settings.previous[1] and self.settings.cells_row[0].top < 60:

					self.settings.speed = self.event.pos[1] - self.settings.previous[1]

					self.settings.move_map.scroll_down()

					self.settings.previous = (self.settings.previous[0], self.event.pos[1])

					if self.settings.cells_row[0].top > 60:

						self.settings.speed = self.settings.cells_row[0].top - 60

						self.settings.move_map.scroll_up()

				# move to the up
				if self.event.pos[1] < self.settings.previous[1] and self.settings.cells_row[-1].bottom > 120:

					self.settings.speed = self.settings.previous[1] - self.event.pos[1]

					self.settings.move_map.scroll_up()

					self.settings.previous = (self.settings.previous[0], self.event.pos[1])

					if self.settings.cells_row[-1].bottom < 120:

						self.settings.speed = 120 - self.settings.cells_row[-1].bottom

						self.settings.move_map.scroll_down()

	
	def update(self):
		self.keyboard()




























