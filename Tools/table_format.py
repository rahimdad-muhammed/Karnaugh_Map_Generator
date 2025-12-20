import pygame

class TableFormat:

	def __init__(self):
		super().__init__()

		# Row format
		self.format_row_rect = pygame.Rect(0,0, 90, 90)
		self.format_row_rect.topleft = (10, 170)
		self.row_rgb = (128,128,128)
		# Symbol
		self.symbol_row_rect = pygame.Rect(0,0,20, 60)
		self.symbol_row_rect.center = (self.format_row_rect.centerx - 10, self.format_row_rect.centery)
		self.symbol_row_rect2 = pygame.Rect(0,0,20,20)
		self.symbol_row_rect2.topleft = self.symbol_row_rect.topright

		# Column Format
		self.format_column_rect = pygame.Rect(0,0, 90, 90)
		self.format_column_rect.topleft = self.format_row_rect.topright
		self.column_rgb = (255,255,255)
		# Symbol
		self.symbol_column_rect = pygame.Rect(0,0,60, 20)
		self.symbol_column_rect.center = (self.format_column_rect.centerx, self.format_column_rect.centery - 10)
		self.symbol_column_rect2 = pygame.Rect(0,0,20,20)
		self.symbol_column_rect2.topleft = self.symbol_column_rect.bottomleft
		

	
	def clicked(self, format, settings):

		match format:
		
			case "row":
				self.row_rgb = (128,128,128)
				self.column_rgb = (255,255,255)
				settings.format = "row"

			case "column":
				self.column_rgb = (128,128,128)
				self.row_rgb = (255,255,255)
				settings.format = "column"

	
	def draw(self, screen):
		# row format
		pygame.draw.rect(screen, self.row_rgb, self.format_row_rect, 0, 0)
		pygame.draw.rect(screen, (0,0,0), self.symbol_row_rect, 0,0)
		pygame.draw.rect(screen, (255,0,0), self.symbol_row_rect2,0,0)

		# column format
		pygame.draw.rect(screen, self.column_rgb, self.format_column_rect, 0, 0)
		pygame.draw.rect(screen, (0,0,0), self.symbol_column_rect, 0,0)
		pygame.draw.rect(screen, (255,0,0), self.symbol_column_rect2, 0,0)























