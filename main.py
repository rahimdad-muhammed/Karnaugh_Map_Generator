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

		settings.screen = self.screen
		settings.screen_w = self.screen_w
		settings.screen_h = self.screen_h
		
		settings.k_map_bed = pygame.Surface((self.screen_w - 200, self.screen_h - 110))

		# text box set up
		settings.text_box = Tools.TextBox(self.screen, settings)

		# move map set up
		settings.move_map = Tools.MoveMap(settings)

		# YouCant set up
		settings.you_cant = Tools.YouCant(settings)

		# Cleaning set up
		settings.cleaning = Tools.Cleaning()

		# TutorialTable set up
		settings.tutorial_table = Tools.TutorialTable(settings)

		
	def game_loop(self) -> None:
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()

				# HANDLING ALL THE KEYBOARD INPUTS
				settings.user_interactions = Tools.UserInteractions(event,settings)
				settings.user_interactions.update()

				# move map set up
				settings.move_map = Tools.MoveMap(settings)

						

				# ----------------------------------------------------------

			# FILL BACKGROUND WITH BLACK COLOR
			self.screen.fill((0,0,0))

			# Draw the Surface that K-Map sleeps on it
			self.screen.blit(settings.k_map_bed, (200, 110))
			settings.k_map_bed.fill((0,0,0))

			# Draw tutorial table
			settings.tutorial_table.draw_table()

			# Clear button
			pygame.draw.rect(self.screen, (255,255,255), settings.clear_button_rect, 0, 100)
			self.screen.blit(settings.clear_font, settings.clear_rect)

			# TEXT BOX
			settings.text_box = Tools.TextBox(self.screen, settings)
			settings.text_box.update()

			# Managing Dictionaries
			settings.dict_manage = Tools.DictManager(settings)
			settings.dict_manage.update()


			settings.map_generator = Tools.MapGenerator(settings)
			try:
				settings.map_generator.update()
			except SyntaxError:
				settings.error = "not_start_end"
				settings.generate_map = False
				
				settings.cleaning.light_cleaning(settings)

			# Handling the errors that caused by the user
			settings.you_cant.matching(settings.error)



			
			


			
			pygame.display.update()
			self.clock.tick(60)


if __name__ == "__main__":
	Main().game_loop()




















