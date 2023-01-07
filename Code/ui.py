import pygame
from settings import *



class UI:
	def __init__(self):
		
		# general 
		self.display_surface = pygame.display.get_surface()
		self.font = pygame.font.Font(UI_FONT,UI_FONT_SIZE)

		# bar setup 
		self.health_bar_rect = pygame.Rect(10,10,HEALTH_BAR_WIDTH,BAR_HEIGHT)
		self.energy_bar_rect = pygame.Rect(10,34,ENERGY_BAR_WIDTH,BAR_HEIGHT)
		self.highest_score=0

		# convert weapon dictionary
		self.weapon_graphics = []
		for weapon in weapon_data.values():
			path = weapon['graphic']
			weapon = pygame.image.load(path).convert_alpha()
			self.weapon_graphics.append(weapon)

		# convert magic dictionary
		self.magic_graphics = []
		for magic in magic_data.values():
			magic = pygame.image.load(magic['graphic']).convert_alpha()
			self.magic_graphics.append(magic)


	def show_bar(self,current,max_amount,bg_rect,color):
		# draw bg 
		pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)

		# converting stat to pixel
		ratio = current / max_amount
		current_width = bg_rect.width * ratio
		current_rect = bg_rect.copy()
		current_rect.width = current_width

		# drawing the bar
		pygame.draw.rect(self.display_surface,color,current_rect)
		pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,bg_rect,3)

	def show_exp(self,exp):
		text_surf = self.font.render(str(int(exp)),False,TEXT_COLOR)
		x = self.display_surface.get_size()[0] - 30
		y = self.display_surface.get_size()[1] - 30
		text_rect = text_surf.get_rect(bottomright = (x,y))

		pygame.draw.rect(self.display_surface,UI_BG_COLOR,text_rect.inflate(20,20))
		self.display_surface.blit(text_surf,text_rect)
		pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,text_rect.inflate(20,20),3)
	def game_over(self,health):
		text_surf = self.font.render("GAMEOVER", False, TEXT_COLOR)
		x = self.display_surface.get_size()[0] - 600
		y = self.display_surface.get_size()[1] - 600
		text_rect = text_surf.get_rect(bottomright=(x, y))

		pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(200, 200))
		self.display_surface.blit(text_surf, text_rect)
		pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(200, 200), 3)
	def scoreshow(self,exp):
		text_surf = self.font.render("Your score is "+str(int(exp)), False, TEXT_COLOR)
		x = self.display_surface.get_size()[0] - 800
		y = self.display_surface.get_size()[1] - 300
		text_rect = text_surf.get_rect(bottomright=(x, y))

		pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(200, 200))
		self.display_surface.blit(text_surf, text_rect)
		pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(200, 200), 3)

	def selection_box(self,left,top, has_switched):
		bg_rect = pygame.Rect(left,top,ITEM_BOX_SIZE,ITEM_BOX_SIZE)
		pygame.draw.rect(self.display_surface,UI_BG_COLOR,bg_rect)
		if has_switched:
			pygame.draw.rect(self.display_surface,UI_BORDER_COLOR_ACTIVE,bg_rect,3)
		else:
			pygame.draw.rect(self.display_surface,UI_BORDER_COLOR,bg_rect,3)
		return bg_rect

	def weapon_overlay(self,weapon_index,has_switched):
		bg_rect = self.selection_box(10,630,has_switched)
		weapon_surf = self.weapon_graphics[weapon_index]
		weapon_rect = weapon_surf.get_rect(center = bg_rect.center)

		self.display_surface.blit(weapon_surf,weapon_rect)

	def magic_overlay(self,magic_index,has_switched):
		bg_rect = self.selection_box(80,635,has_switched)
		magic_surf = self.magic_graphics[magic_index]
		magic_rect = magic_surf.get_rect(center = bg_rect.center)

		self.display_surface.blit(magic_surf,magic_rect)

	def getHighestScore(self):
		with open("highest_score.txt","r") as f:
			return f.read()

	def display(self, player):
		try:
			highest_score = int(self.getHighestScore())
		except:
			highest_score = 0
		self.show_bar(player.health, player.stats['health'], self.health_bar_rect, HEALTH_COLOR)
		#self.show_bar(player.energy, player.stats['energy'], self.energy_bar_rect, ENERGY_COLOR)
		self.show_exp(player.exp)

		if player.health <= 0:
			# enemy.status = 'idle'
			if(highest_score<player.exp):
				highest_score=player.exp
			with open("highest_score.txt","w") as f:
				f.write(str(highest_score))
			self.game_over(player.health)



			'''text_surf = self.font.render("Your current score is:" + str(int(player.exp)), False, TEXT_COLOR)
			x = self.display_surface.get_size()[0] - 500
			y = self.display_surface.get_size()[1] - -400
			text_rect = text_surf.get_rect(bottomright=(x, y))

			pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(200, 200))
			self.display_surface.blit(text_surf, text_rect)
			pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(200, 200), 3)
			print(player.exp)'''

			text_surf = self.font.render("Your Cuurent score is:" + str(int(player.exp)), False, TEXT_COLOR)
			x = self.display_surface.get_size()[0] - 500
			y = self.display_surface.get_size()[1] - 200
			text_rect = text_surf.get_rect(bottomright=(x, y))

			pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(200, 200))
			self.display_surface.blit(text_surf, text_rect)
			pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(200, 200), 3)
		# self.scoreshow(player.health)

		# pygame.time.delay(5000000)
		# self.highscore(player.health)

		self.weapon_overlay(player.weapon_index, not player.can_switch_weapon)
		self.magic_overlay(player.magic_index, not player.can_switch_magic)