import pygame
from pygame import Surface
from pygame.font import Font
from pygame.math import Vector2


class TextBox:
	def __init__(self, screen : Surface, settings) -> None:

		self.settings = settings
		self.screen : surface = screen

		# TEXT SET UP
		self.text : str = str("".join(settings.user_input))
		
		self.text_surface : surface = settings.font.render(self.text, True, (255,255,255))

		self.text_rect : rect = self.text_surface.get_rect(topleft = (settings.text_location))

		# Text edit rect set up
		self.edit_rect_width : int = (self.text_rect.right - self.text_rect.left) + 20
		
		self.edit_rect : rect = pygame.Rect(0, 0, self.edit_rect_width, 60)

		self.edit_rect.center = self.text_rect.center

	def prime_line(self) -> None:
		self.settings.text_rect_width : int = self.text_rect.right


	def draw(self) -> None:
		# text draw
		self.screen.blit(self.text_surface, self.text_rect)

		# edit rect draw
		pygame.draw.rect(self.screen, (255,255,255), self.edit_rect, 5, 5)

		# draw prime_line's
		for group, position in self.settings.prime_line.items():

			if not(self.edit_rect.collidepoint(position[0])):
				self.settings.delete = True
				self.settings.prime = False
				self.settings.calculate.pop(-1) #*********
				self.settings.del_group = group
				continue

			if len(position) == 2:

				if position[0] == position[1]:
					self.settings.delete = True
					self.settings.del_group = group
					continue
				
				if not(self.edit_rect.collidepoint(position[1])):
					
					self.settings.prime_line[group][1] = (self.text_rect.right, 48)
				
				pygame.draw.line(self.screen, (255,255, 255), position[0], position[1], 3)

			else:
				pygame.draw.line(self.screen, (255,255,255), position[0], (self.text_rect.right, 48), 3)

	
	def update(self) -> None:

		self.draw()










		