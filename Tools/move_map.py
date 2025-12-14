import pygame

class MoveMap:
	def __init__(self, settings):
		super().__init__()

		# Getting the Settings
		self.settings = settings

		# Setting the Scrolling speed
		self.speed = 10

	def scroll_up(self):
		# ***************** Left row ************************
		for rect_index, left_row_rect in enumerate(self.settings.cells_row):

			# Moving the rect
			self.settings.cells_row[rect_index].y -= self.speed

			# Moving the result rects
			for rect_index2, result_rect in enumerate(self.settings.other_cells[rect_index]):
				
				self.settings.other_cells[rect_index][rect_index2].y -= self.speed
			

	def scroll_down(self):
		for rect_index, left_row_rect in enumerate(self.settings.cells_row):

			# Moving the rect
			self.settings.cells_row[rect_index].y += self.speed

			# Moving the result rects
			for rect_index2, result_rect in enumerate(self.settings.other_cells[rect_index]):
				
				self.settings.other_cells[rect_index][rect_index2].y += self.speed


	def scroll_right(self):
		for rect_index, top_column_rect in enumerate(self.settings.cells_column):

			# Moving the rect
			self.settings.cells_column[rect_index].x += self.speed

			# Moving the result rects
			for rect_index2, result_rect in enumerate(self.settings.cells_row):
				
				self.settings.other_cells[rect_index2][rect_index].x += self.speed

	def scroll_left(self):
		for rect_index, top_column_rect in enumerate(self.settings.cells_column):

			# Moving the rect
			self.settings.cells_column[rect_index].x -= self.speed

			# Moving the result rects
			for rect_index2, result_rect in enumerate(self.settings.cells_row):
				
				self.settings.other_cells[rect_index2][rect_index].x -= self.speed


























