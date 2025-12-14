import pygame

class YouCant:
	def __init__(self, settings):
		super().__init__()

		self.settings = settings

	def no_input_type(self):
		
		error_surf = self.settings.font.render("YOU HAVE TO ENTER AT LEAST ONE INPUT TYPE (A, B, C, D, etc.)", True, (255,0,0))
		error_rect = error_surf.get_rect(topright = (self.settings.screen_w - 20, 20))

		error_bg = pygame.Rect(0,0,(error_rect.right - error_rect.left) + 40, (error_rect.bottom - error_rect.top) + 40)
		error_bg.topright = (self.settings.screen_w, 0)

		pygame.draw.rect(self.settings.screen, (255,255,255), error_bg)
		self.settings.screen.blit(error_surf, error_rect)
		

	def cant_start_end(self):
		
		error_surf = self.settings.font.render("A boolean equation can't start or end with or(+), xor(^) operators", True, (255,0,0))
		error_rect = error_surf.get_rect(topright = (self.settings.screen_w - 20, 20))

		error_bg = pygame.Rect(0,0,(error_rect.right - error_rect.left) + 40, (error_rect.bottom - error_rect.top) + 40)
		error_bg.topright = (self.settings.screen_w, 0)

		pygame.draw.rect(self.settings.screen, (255,255,255), error_bg)
		self.settings.screen.blit(error_surf, error_rect)

	def not_start_end(self):
		
		error_surf = self.settings.font.render("You can't finish or start a not(prime) function with or(+), xor(^) operators", True, (255,0,0))
		error_rect = error_surf.get_rect(topright = (self.settings.screen_w - 20, 20))

		error_bg = pygame.Rect(0,0,(error_rect.right - error_rect.left) + 40, (error_rect.bottom - error_rect.top) + 40)
		error_bg.topright = (self.settings.screen_w, 0)

		pygame.draw.rect(self.settings.screen, (255,255,255), error_bg)
		self.settings.screen.blit(error_surf, error_rect)

	def next_to_next(self):
		error_surf = self.settings.font.render("You cant enter next to next like this (++),(^^), (+^),(^+)", True, (255,0,0))
		error_rect = error_surf.get_rect(topright = (self.settings.screen_w - 20, 20))

		error_bg = pygame.Rect(0,0,(error_rect.right - error_rect.left) + 40, (error_rect.bottom - error_rect.top) + 40)
		error_bg.topright = (self.settings.screen_w, 0)

		pygame.draw.rect(self.settings.screen, (255,255,255), error_bg)
		self.settings.screen.blit(error_surf, error_rect)

	def matching(self, error):
		
		match error:
			case "no_input_type":
				return self.no_input_type()

			case "cant_start_end":
				return self.cant_start_end()

			case "not_start_end":
				return self.not_start_end()

			case "next_to_next":
				return self.next_to_next()
		







