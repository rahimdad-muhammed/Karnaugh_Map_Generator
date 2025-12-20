import pygame

class Instrunctions:

	def __init__(self, settings):
		super().__init__()

		self.settings = settings

		self.rect_circ = pygame.Rect(settings.screen_w - 60 ,0,60,60)

		font = pygame.font.Font(None, 50)
		
		self.rect_circ_symbol = font.render("i", True, (255,255,255))

		self.rect_circ_symbol_rect = self.rect_circ_symbol.get_rect(center = (self.rect_circ.centerx, self.rect_circ.centery + 3))

		self.rect_circ_circ = pygame.Rect(0,0,
										  (self.rect_circ_symbol_rect.bottom - self.rect_circ_symbol_rect.top) + 10,
										  (self.rect_circ_symbol_rect.bottom - self.rect_circ_symbol_rect.top) + 10
										 )
		self.rect_circ_circ.center = self.rect_circ.center

		self.instructions_surf = settings.font.render(
			("1) By pressing any letter on your keyboard you can add a input type to your equation (A,B,C,etc.)\n\n" +
			 "2) By pressing the SPACE key you can enable the prime mode. In prime mod what ever you write you will\n      see a upperline on your input. You can disenable it by pressing the space key again.\n\n" +
			 "3) By pressing to BACKSPACE key you can delete the things you just entered\n\n" +
			 "4) By pressing to ('^','+') symbols on your keyboard (the keys above the letters)\n      you can add 'or', 'xor' operations to your boolean equation.\n\n" +
			 "5) If you enter input types next to next the and operation will be used otomatically\n      so you don't have to do anything to add this operation.\n\n" +
			 "6) If you press to ENTER key the Karnaugh-Map will be created based on your equation.\n\n" +
			 "7) If you click to CLEAR button that under the text box you can reset everything.\n\n" +
			 "8) When you enter a invalid equation you will see a text on topright of the screen about what you did wrong.\n\n" +
			 "9) Under the CLEAR button you will see format options, by clicking to one of them you can change the table format.\n\n" +
			 "10) You can enter 1 and 0 to your equation.\n\n" +
			 "11) On the bottomleft of the screen you will see the basic equations. You can use as a reference.\n\n" +
			 "12) On the topleft of the K-Map you will see a rectangle seperated by 2 triangles.\n      By moving your mouse on triangles you can display the inputs that used for that 'column' or 'row'.\n\n" +
			 "13) You can scrool the table by using the touchpad of laptop.\n\n" +
			 "14) Actually you can move the table by just holding the K-Map with left-click"),
			True, (255,0,255))

		self.instructions_rect = self.instructions_surf.get_rect(topright = self.rect_circ.bottomleft)

		self.instructions_bg = pygame.Surface(((self.instructions_rect.right - self.instructions_rect.left) + 40,
										   (self.instructions_rect.bottom - self.instructions_rect.top + 40)),pygame.SRCALPHA)
		self.instructions_bg_pos = (self.instructions_rect.left - 20, self.instructions_rect.top -20)
		transparent_color = (0,0,0,200)
		self.instructions_bg.fill(transparent_color)

	def draw(self):

		pygame.draw.rect(self.settings.screen, (255,125,0), self.rect_circ, 0, 50)
		
		self.settings.screen.blit(self.rect_circ_symbol, self.rect_circ_symbol_rect)

		pygame.draw.rect(self.settings.screen, (255,255,255), self.rect_circ_circ, 3, 50)

		if self.rect_circ.collidepoint(self.settings.mouse_pos):
			self.settings.screen.blit(self.instructions_bg, self.instructions_bg_pos)
			self.settings.screen.blit(self.instructions_surf, self.instructions_rect)












