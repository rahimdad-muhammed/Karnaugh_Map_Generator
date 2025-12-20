import pygame

class MoveMap:
	def __init__(self, settings):
		super().__init__()

		# Getting the Settings
		self.settings = settings



	def scroll_up(self):

		match self.settings.format:

			case "row":
				# ***************** Left row ************************
				for rect_index, left_row_rect in enumerate(self.settings.cells_row):

					# Moving the rect
					self.settings.cells_row[rect_index].y -= self.settings.speed

					# Moving the result rects
					for rect_index2, result_rect in enumerate(self.settings.other_cells[rect_index]):
				
						self.settings.other_cells[rect_index][rect_index2].y -= self.settings.speed


			case "column":
				# ***************** Left row ************************
				for rect_index, left_row_rect in enumerate(self.settings.cells_row):

					# Moving the rect
					self.settings.cells_row[rect_index].y -= self.settings.speed

					# Moving the result rects
					for rect_index2, column_rect in enumerate(self.settings.cells_column):
				
						self.settings.other_cells[rect_index2][rect_index].y -= self.settings.speed
			

	def scroll_down(self):

		match self.settings.format:

			case "row":
				
				for rect_index, left_row_rect in enumerate(self.settings.cells_row):

					# Moving the rect
					self.settings.cells_row[rect_index].y += self.settings.speed
		
					# Moving the result rects
					for rect_index2, result_rect in enumerate(self.settings.other_cells[rect_index]):
				
						self.settings.other_cells[rect_index][rect_index2].y += self.settings.speed

			case "column":
				for rect_index, left_row_rect in enumerate(self.settings.cells_row):

					# Moving the rect
					self.settings.cells_row[rect_index].y += self.settings.speed
		
					# Moving the result rects
					for rect_index2, result_rect in enumerate(self.settings.cells_column):
				
						self.settings.other_cells[rect_index2][rect_index].y += self.settings.speed


	def scroll_right(self):

		match self.settings.format:

			case "row":
				for rect_index, top_column_rect in enumerate(self.settings.cells_column):

					# Moving the rect
					self.settings.cells_column[rect_index].x += self.settings.speed

					# Moving the result rects
					for rect_index2, result_rect in enumerate(self.settings.cells_row):
				
						self.settings.other_cells[rect_index2][rect_index].x += self.settings.speed

			case "column":
				
				for rect_index, top_column_rect in enumerate(self.settings.cells_column):

					# Moving the rect
					self.settings.cells_column[rect_index].x += self.settings.speed

					# Moving the result rects
					for rect_index2, result_rect in enumerate(self.settings.cells_row):
				
						self.settings.other_cells[rect_index][rect_index2].x += self.settings.speed
						

	def scroll_left(self):

		match self.settings.format:

			case "row":
				for rect_index, top_column_rect in enumerate(self.settings.cells_column):

					# Moving the rect
					self.settings.cells_column[rect_index].x -= self.settings.speed

					# Moving the result rects
					for rect_index2, result_rect in enumerate(self.settings.cells_row):
						
						self.settings.other_cells[rect_index2][rect_index].x -= self.settings.speed

			case "column":
				for rect_index, top_column_rect in enumerate(self.settings.cells_column):

					# Moving the rect
					self.settings.cells_column[rect_index].x -= self.settings.speed

					# Moving the result rects
					for rect_index2, result_rect in enumerate(self.settings.cells_row):
						
						self.settings.other_cells[rect_index][rect_index2].x -= self.settings.speed




























