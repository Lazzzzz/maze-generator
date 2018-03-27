import pygame
import random

pygame.init()

print("taille de l'ecran")
taille = int(input())

print("nombre de cases")
nb_case = int(input())

taille = [taille, taille]

taille_case = int(taille[0]/nb_case)

grille = [[0 for x in range(nb_case)] for y in range(nb_case)] 

done = False

fenetre = pygame.display.set_mode((taille))
pygame.display.set_caption('maze generator')

fenetre.fill((0,0,0))

class case():
	def __init__(self, j, i):

		self.i = i
		self.j = j

		self.visiter = False
		self.mur = [True, True, True, True]

	def update(self):

		if self.mur[0] == True:
			pygame.draw.line(fenetre, (255, 255, 255) , (self.i, self.j), (self.i + taille_case, self.j))	
			
		if self.mur[1] == True:	
			pygame.draw.line(fenetre, (255, 255, 255) , (self.i, self.j), (self.i, self.j + taille_case))
		
		if self.mur[2] == True:
			pygame.draw.line(fenetre, (255, 255, 255) , (self.i, self.j + taille_case), (self.i + taille_case, self.j + taille_case))	
		
		if self.mur[3] == True:
			pygame.draw.line(fenetre, (255, 255, 255) , (self.i + taille_case, self.j), (self.i + taille_case, self.j + taille_case))	

class mainCase():
	def __init__(self):
		
		self.i = 0
		self.j = 0

		self.autour = []
		self.choix = -1
	
		self.ancien = []

	def checkAutour(self):

		self.autour = []

		if self.j + 1 >= 0 and self.j + 1 < len(grille) :
			if grille[self.j + 1][self.i].visiter == False:
				self.autour.append(2)

		if self.j - 1 >= 0 and self.j - 1 < len(grille):
			if grille[self.j - 1][self.i].visiter == False:
				self.autour.append(0)

		if self.i + 1 >= 0 and self.i + 1 < len(grille[j]):
			if grille[self.j][self.i + 1].visiter == False:
				self.autour.append(3)

		if self.i - 1 >= 0 and self.i - 1 < len(grille[j]):
			if grille[self.j][self.i - 1].visiter == False:
				self.autour.append(1)

	def deplacement(self):

		self.choix = -1

		if len(self.autour) > 0:
			
			self.choix = random.choice(self.autour)
			self.ancien.append((self.i, self.j))

		else:

			if len(self.ancien) > 0:
				self.i, self.j = self.ancien.pop()
		
		if self.choix == 0:
			self.j = self.j - 1
			
			grille[self.j][self.i].mur[2] = False
			grille[self.j + 1][self.i].mur[0] = False

		if self.choix == 1:
			self.i = self.i - 1		
			
			grille[self.j][self.i].mur[3] = False
			grille[self.j][self.i + 1].mur[1] = False
		
		if self.choix == 2:
			self.j = self.j + 1
		
			grille[self.j][self.i].mur[0] = False
			grille[self.j - 1][self.i].mur[2] = False		

		if self.choix == 3:
			self.i = self.i + 1

			grille[self.j][self.i].mur[1] = False
			grille[self.j][self.i - 1].mur[3] = False

		grille[self.j][self.i].visiter = True


	def update(self):
		
		pygame.draw.rect(fenetre, (255, 0, 0), (self.i * taille_case + taille_case/4, self.j * taille_case + taille_case/4, taille_case/2, taille_case/2))

		self.checkAutour()

		self.deplacement()

		
mainCase = mainCase()

for i in range(nb_case):
	for j in range(nb_case):
		grille[i][j] = case(i * taille_case, j * taille_case)
		grille[i][j].update()

grille[mainCase.j][mainCase.i].visiter = True

while not done:
	
	for event in pygame.event.get():
			
		if event.type == pygame.QUIT:
			done = True

	fenetre.fill((0,0,0))

	for i in range(nb_case):
		for j in range(nb_case):	
			grille[i][j].update()

	mainCase.update()

	pygame.display.flip()
	pygame.time.Clock().tick(0)

pygame.quit()
