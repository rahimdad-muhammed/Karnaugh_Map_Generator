import pygame
from sys import exit

import settings # import all the data
import Tools # importing all the tools and core mechanics for my program


class Main:
	def __init__(self) -> None:
		"""
		Creating all the starting values and class variables to run the program
		"""
		super().__init__() # initialize better
		""" STARTER VALUES """
		pygame.init() # initialize all the pygame modules
		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) # creating a pygamescreen that cover whole screen
		pygame.display.set_caption("Karnaugh Map Generator") # settings the title of the program
		self.clock = pygame.time.Clock() # setting the clock value to change frame rate later
		
		# Getting the screen dimensions
		self.screen_w, self.screen_h = self.screen.get_size()

		# storing screen surface inside the settings to use it on every file for drawing things
		settings.screen = self.screen
		# Getting the screen dimensions inside the settings
		settings.screen_w = self.screen_w # width
		settings.screen_h = self.screen_h # height

		# the surface that K_Map will sleep on
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

		# settings up the table_format to give freedom to user to change table format
		settings.table_format = Tools.TableFormat()

		# MapGenerator class set up
		settings.map_generator = Tools.MapGenerator(settings)

		# Instrunctions class set
		settings.instructions = Tools.Instrunctions(settings)
		
	def game_loop(self) -> None:
		"""
		The loop that gonna used for running the whole program, the function that meant to be run
		"""
		while True: # creating an infinite loop
			for event in pygame.event.get(): # getting all the user events
				if event.type == pygame.QUIT: # if user press to the X button on the screen then finish the program
					pygame.quit() # end pygame modules
					exit() # finish the program completely

				# HANDLING ALL THE KEYBOARD INPUTS, and MOUSE EVENTS
				settings.user_interactions = Tools.UserInteractions(event,settings)
				settings.user_interactions.update()

				# move map set up, to update the values, because after handling the mouse events we have to change table cordinates
				settings.move_map = Tools.MoveMap(settings)

						

				# ----------------------------------------------------------

			# FILL BACKGROUND WITH BLACK COLOR
			self.screen.fill((0,0,0))

			# Draw the Surface that K-Map sleeps on it
			self.screen.blit(settings.k_map_bed, (200, 110))
			# Filling the Suface that house for K-map
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

			# Updating map values
			settings.map_generator = Tools.MapGenerator(settings)
			# handling the function because we can run into some trouble
			try:
				# Updates everything, draws table, creates table, does everythin about table
				settings.map_generator.update()
			except SyntaxError: # the only error we encour when we running the function above
				# This error happens because when user enter some invalid equation like this "not(ABC++)" when we run the user equation inside the eval() function it will raise syntaxerror because the user didn't entered an invalid equation but we dont want to end the program because of the some stupid errors we want to display where the user did wrong so we are setting the error type. If user entered a not equation that starts with '+', '^' then user be able to see an error message on top-right of the screen
				settings.error = "not_start_end"
				# disenabling generate_map function because the user equation is not valid
				settings.generate_map = False
				# reseting the values, but not that deep
				settings.cleaning.light_cleaning(settings)

			# Handling the errors that caused by the user
			settings.you_cant.matching(settings.error)


			# Draw the format choose rects
			settings.table_format.draw(self.screen)

			# draw instructions
			settings.instructions.draw()


			
			


			
			# pygame.display.update()
			pygame.display.flip()
			# setting the frame to the 60 fps
			self.clock.tick(60)


# not running the funtion if we importing this file into another file. because we dont want it run when we importing it into the another file
if __name__ == "__main__":
	# running the game
	Main().game_loop()




















