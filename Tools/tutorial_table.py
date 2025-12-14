import pygame

class TutorialTable:

	def __init__(self, settings):
		super().__init__()

		self.settings = settings

		# BUFFER
		self.buffer_rect = pygame.Rect(0,0,90,60)
		self.buffer_rect.bottomleft = (0,settings.screen_h)
		self.buffer_surf = settings.font.render("BUFFER", True, (255,0,0))
		self.buffer_surf_rect = self.buffer_surf.get_rect(center = (self.buffer_rect.center))
		# BUFFER Equation
		self.buffer_eq_rect = pygame.Rect(0,0,90,60)
		self.buffer_eq_rect.bottomleft = self.buffer_rect.bottomright
		self.buffer_eq_surf = settings.font.render("A", True, (255,0,0))
		self.buffer_eq_surf_rect = self.buffer_eq_surf.get_rect(center = (self.buffer_eq_rect.center))

		# NOT 
		self.not_rect = pygame.Rect(0,0,90,60)
		self.not_rect.bottomleft = self.buffer_rect.topleft
		self.not_surf = settings.font.render("NOT", True, (255,0,0))
		self.not_surf_rect = self.not_surf.get_rect(center = (self.not_rect.center))
		# NOT Equation
		self.not_eq_rect = pygame.Rect(0,0,90,60)
		self.not_eq_rect.bottomleft = self.not_rect.bottomright
		self.not_eq_surf = settings.font.render("A", True, (255,0,0))
		self.not_eq_surf_rect = self.not_eq_surf.get_rect(center = (self.not_eq_rect.center))
		self.not_line1 = (self.not_eq_surf_rect.left, self.not_eq_surf_rect.top - 2)
		self.not_line2 = (self.not_eq_surf_rect.right, self.not_eq_surf_rect.top - 2)

		# XNOR
		self.xnor_rect = pygame.Rect(0,0,90,60)
		self.xnor_rect.bottomleft = self.not_rect.topleft
		self.xnor_surf = settings.font.render("XNOR", True, (255,0,0))
		self.xnor_surf_rect = self.xnor_surf.get_rect(center = (self.xnor_rect.center))
		# XNOR Equation
		self.xnor_eq_rect = pygame.Rect(0,0,90,60)
		self.xnor_eq_rect.bottomleft = self.xnor_rect.bottomright
		self.xnor_eq_surf = settings.font.render("A^B", True, (255,0,0))
		self.xnor_eq_surf_rect = self.xnor_eq_surf.get_rect(center = (self.xnor_eq_rect.center))
		self.xnor_line1 = (self.xnor_eq_surf_rect.left, self.xnor_eq_surf_rect.top - 2)
		self.xnor_line2 = (self.xnor_eq_surf_rect.right, self.xnor_eq_surf_rect.top - 2)

		# XOR
		self.xor_rect = pygame.Rect(0,0,90,60)
		self.xor_rect.bottomleft = self.xnor_rect.topleft
		self.xor_surf = settings.font.render("XOR", True, (255,0,0))
		self.xor_surf_rect = self.xor_surf.get_rect(center = (self.xor_rect.center))
		# XOR Equation
		self.xor_eq_rect = pygame.Rect(0,0,90,60)
		self.xor_eq_rect.bottomleft = self.xor_rect.bottomright
		self.xor_eq_surf = settings.font.render("A^B", True, (255,0,0))
		self.xor_eq_surf_rect = self.xor_eq_surf.get_rect(center = (self.xor_eq_rect.center))

		# NOR
		self.nor_rect = pygame.Rect(0,0,90,60)
		self.nor_rect.bottomleft = self.xor_rect.topleft
		self.nor_surf = settings.font.render("NOR", True, (255,0,0))
		self.nor_surf_rect = self.nor_surf.get_rect(center = (self.nor_rect.center))
		# NOR Equation
		self.nor_eq_rect = pygame.Rect(0,0,90,60)
		self.nor_eq_rect.bottomleft = self.nor_rect.bottomright
		self.nor_eq_surf = settings.font.render("A+B", True, (255,0,0))
		self.nor_eq_surf_rect = self.nor_eq_surf.get_rect(center = (self.nor_eq_rect.center))
		self.nor_line1 = (self.nor_eq_surf_rect.left, self.nor_eq_surf_rect.top - 2)
		self.nor_line2 = (self.nor_eq_surf_rect.right, self.nor_eq_surf_rect.top - 2)

		# NAND
		self.nand_rect = pygame.Rect(0,0,90,60)
		self.nand_rect.bottomleft = self.nor_rect.topleft
		self.nand_surf = settings.font.render("NAND", True, (255,0,0))
		self.nand_surf_rect = self.nand_surf.get_rect(center = (self.nand_rect.center))
		# NAND Equation
		self.nand_eq_rect = pygame.Rect(0,0,90,60)
		self.nand_eq_rect.bottomleft = self.nand_rect.bottomright
		self.nand_eq_surf = settings.font.render("AB", True, (255,0,0))
		self.nand_eq_surf_rect = self.nand_eq_surf.get_rect(center = (self.nand_eq_rect.center))
		self.nand_line1 = (self.nand_eq_surf_rect.left, self.nand_eq_surf_rect.top - 2)
		self.nand_line2 = (self.nand_eq_surf_rect.right, self.nand_eq_surf_rect.top - 2)

		# OR
		self.or_rect = pygame.Rect(0,0,90,60)
		self.or_rect.bottomleft = self.nand_rect.topleft
		self.or_surf = settings.font.render("OR", True, (255,0,0))
		self.or_surf_rect = self.or_surf.get_rect(center = (self.or_rect.center))
		# OR Equation
		self.or_eq_rect = pygame.Rect(0,0,90,60)
		self.or_eq_rect.bottomleft = self.or_rect.bottomright
		self.or_eq_surf = settings.font.render("A+B", True, (255,0,0))
		self.or_eq_surf_rect = self.or_eq_surf.get_rect(center = (self.or_eq_rect.center))

		# AND
		self.and_rect = pygame.Rect(0,0,90,60)
		self.and_rect.bottomleft = self.or_rect.topleft
		self.and_surf = settings.font.render("AND", True, (255,0,0))
		self.and_surf_rect = self.and_surf.get_rect(center = (self.and_rect.center))
		# AND Equation
		self.and_eq_rect = pygame.Rect(0,0,90,60)
		self.and_eq_rect.bottomleft = self.and_rect.bottomright
		self.and_eq_surf = settings.font.render("AB", True, (255,0,0))
		self.and_eq_surf_rect = self.and_eq_surf.get_rect(center = (self.and_eq_rect.center))

	def draw_table(self):

		# Buffer
		pygame.draw.rect(self.settings.screen, (255,255,0), self.buffer_rect, 2)
		self.settings.screen.blit(self.buffer_surf, self.buffer_surf_rect)
		pygame.draw.rect(self.settings.screen, (255,255,0), self.buffer_eq_rect, 2)
		self.settings.screen.blit(self.buffer_eq_surf, self.buffer_eq_surf_rect)

		# NOT
		pygame.draw.rect(self.settings.screen, (255,255,0), self.not_rect, 2)
		self.settings.screen.blit(self.not_surf, self.not_surf_rect)
		pygame.draw.rect(self.settings.screen, (255,255,0), self.not_eq_rect, 2)
		self.settings.screen.blit(self.not_eq_surf, self.not_eq_surf_rect)
		pygame.draw.line(self.settings.screen, (255,0,0), self.not_line1, self.not_line2, 2)

		# XNOR
		pygame.draw.rect(self.settings.screen, (255,255,0), self.xnor_rect, 2)
		self.settings.screen.blit(self.xnor_surf, self.xnor_surf_rect)
		pygame.draw.rect(self.settings.screen, (255,255,0), self.xnor_eq_rect, 2)
		self.settings.screen.blit(self.xnor_eq_surf, self.xnor_eq_surf_rect)
		pygame.draw.line(self.settings.screen, (255,0,0), self.xnor_line1, self.xnor_line2, 2)

		# XOR
		pygame.draw.rect(self.settings.screen, (255,255,0), self.xor_rect, 2)
		self.settings.screen.blit(self.xor_surf, self.xor_surf_rect)
		pygame.draw.rect(self.settings.screen, (255,255,0), self.xor_eq_rect, 2)
		self.settings.screen.blit(self.xor_eq_surf, self.xor_eq_surf_rect)

		# NOR
		pygame.draw.rect(self.settings.screen, (255,255,0), self.nor_rect, 2)
		self.settings.screen.blit(self.nor_surf, self.nor_surf_rect)
		pygame.draw.rect(self.settings.screen, (255,255,0), self.nor_eq_rect, 2)
		self.settings.screen.blit(self.nor_eq_surf, self.nor_eq_surf_rect)
		pygame.draw.line(self.settings.screen, (255,0,0), self.nor_line1, self.nor_line2, 2)

		# NAND
		pygame.draw.rect(self.settings.screen, (255,255,0), self.nand_rect, 2)
		self.settings.screen.blit(self.nand_surf, self.nand_surf_rect)
		pygame.draw.rect(self.settings.screen, (255,255,0), self.nand_eq_rect, 2)
		self.settings.screen.blit(self.nand_eq_surf, self.nand_eq_surf_rect)
		pygame.draw.line(self.settings.screen, (255,0,0), self.nand_line1, self.nand_line2, 2)

		# OR
		pygame.draw.rect(self.settings.screen, (255,255,0), self.or_rect, 2)
		self.settings.screen.blit(self.or_surf, self.or_surf_rect)
		pygame.draw.rect(self.settings.screen, (255,255,0), self.or_eq_rect, 2)
		self.settings.screen.blit(self.or_eq_surf, self.or_eq_surf_rect)

		# AND
		pygame.draw.rect(self.settings.screen, (255,255,0), self.and_rect, 2)
		self.settings.screen.blit(self.and_surf, self.and_surf_rect)
		pygame.draw.rect(self.settings.screen, (255,255,0), self.and_eq_rect, 2)
		self.settings.screen.blit(self.and_eq_surf, self.and_eq_surf_rect)
		
























