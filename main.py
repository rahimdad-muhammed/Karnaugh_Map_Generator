import pygame
from sys import exit
import math
from copy import deepcopy

import settings # import all the data
import Tools


class Main:
	def __init__(self) -> None:
		super().__init__()
		""" STARTER VALUES """
		pygame.init()
		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		pygame.display.set_caption("Boolean Logic")
		self.clock = pygame.time.Clock()
		""" -------------------------------------- """
		# Screen Size
		self.screen_w, self.screen_h = self.screen.get_size()

		# text box set up
		settings.text_box = Tools.TextBox(self.screen, settings)
		

		# TRIAL
		self.trial_rect = pygame.Rect(0,0,80,60)
		self.trial_rect.topleft = (200,110)
		
	def game_loop(self) -> None:
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()

				# HANDLING ALL THE KEYBOARD INPUTS
				settings.user_interactions = Tools.UserInteractions(event,settings)
				settings.user_interactions.update()

						

				# ----------------------------------------------------------

			# FILL BACKGROUND WITH BLACK COLOR
			self.screen.fill((0,0,0))

			# TEXT BOX
			settings.text_box = Tools.TextBox(self.screen, settings)
			settings.text_box.update()

			# Managing Dictionaries
			settings.dict_manage = Tools.DictManager(settings)
			settings.dict_manage.update()


			settings.map_generator = Tools.MapGenerator(self.screen, settings)
			settings.map_generator.update()


			
			


			
			pygame.display.update()
			self.clock.tick(60)


if __name__ == "__main__":
	Main().game_loop()




















