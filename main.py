# * * *    BETA 4.9    * * * #

import pygame
import time

pygame.init()
pygame.font.init()

width = 1250
height = 700

win = pygame.display.set_mode((width, height))

background = pygame.image.load("background.jpg")
planeImg = pygame.image.load("fighter.png")
helicopterImg = pygame.image.load("helicopter.png")
aeroplaneImg = pygame.image.load("aeroplane.png")
bulletImg = pygame.image.load("bullet.png")
explosionImg = pygame.image.load("explosion.png")
bulletImg = pygame.image.load("bullet.png")
bombImg = pygame.image.load("bomb.png")
iconImg = pygame.image.load("icon.png")
airplaneImg = pygame.image.load("airplane.png")

bgX = 0
bgX2 = background.get_width()

pygame.display.set_caption("My Game")
pygame.display.set_icon(iconImg)

x = 100
y = 150
s1 = 30
s2 = 85
helicopterX = 1500
helicopterY = 10
helicopterY1 = helicopterY + 100
helicopterY2 = 0
helicopterX1 = 2500
helicopterX2 = 800
helicopters = []
aeroplaneX = 2500
aeroplaneY = 250
aeroplanes = []
airplaneX = 2750
airplaneY = 500
airplanes = []
bulletX = x + s1
bulletY = y + s2
bombX = x + s1
bombY = y + s2
bombs = []
bullets = []
vel = 10
speed = 20
shootLoop = 0
shootLoopB = 0
visible = [True, True, True, True, True, True]
visibleA = [True, True, True, True, True, True]
visibleB = [True, True, True, True]
visibleH1 = [True, True, True]
visibleH2 = [True, True]
index = 0
down = True
up = False

class Aeroplane():
	def __init__(self, x, y, visible):
		self.visible = visible
		if self.visible:
			self.x = x
			self.y = y

	def draw(self):
		if self.visible:
			win.blit(aeroplaneImg, (self.x, self.y))

class Airplane():
	def __init__(self, x, y, visible):
		self.visible = visible
		if self.visible:
			self.x = x
			self.y = y

	def draw(self):
		if self.visible:
			win.blit(airplaneImg, (self.x, self.y)) 

class Helicopter():
	def __init__(self, x, y, visible):
		self.visible = visible
		if self.visible:
			self.x = x
			self.y = y

	def draw(self):
		if self.visible:
			win.blit(helicopterImg, (self.x, self.y))

class Bullet():
	global bulletX, bulletY
	def __init__(self, x, y):
		self.x = bulletX
		self.y = bulletY

class Bomb():
	global bombX, bombY
	def __init__(self, x, y):
		self.x = bombX
		self.y = bombY

def game_over_screen():
	font = pygame.font.SysFont("Arial", 50, True)
	text = font.render("GAME OVER", 50, (255, 0, 0))
	win.blit(text, (400, 300))
	win.blit(explosionImg, (x + 10, y + 10))
	pygame.display.update()

def you_won_screen():
	font = pygame.font.SysFont("Arial", 50, True)
	text = font.render("YOU WON!", 50, (255, 255, 255))
	win.blit(text, (400, 300))
	pygame.display.update()

def reDrawWindow():
	global helicopterX, helicopterY, helicopters, bulletX, bulletY, bullets, x, y, visible, aeroplaneX, aeroplaneY, aeroplanes, visibleA

	win.blit(background, (bgX, 0))
	win.blit(background, (bgX2, 0))
	win.blit(planeImg, (x, y))

	for i in range(4):
		helicopter = Helicopter(helicopterX + i * 200, helicopterY, visible[i])
		helicopter.draw()
		helicopters.append(helicopter)

	for i in range(3):
		helicopter = Helicopter(helicopterX1 + i * 200, helicopterY1, visibleH1[i])
		helicopter.draw()
		helicopters.append(helicopter)

	for i in range(6):
		aeroplane = Aeroplane(aeroplaneX + i * 200, aeroplaneY, visibleA[i])
		aeroplane.draw()
		aeroplanes.append(aeroplane)

	for i in range(4):
		airplane = Airplane(airplaneX + i * 200, airplaneY, visibleB[i])
		airplane.draw()
		airplanes.append(airplane)

	for i in range(2):
		helicopter = Helicopter(helicopterX2 + i * 200, helicopterY2, visibleH2[i])
		helicopter.draw()
		helicopters.append(helicopter)
	
	if helicopterX < 300:
		helicopterY += vel

	if len(bullets) > 0:
		for i in range(len(bullets)):
			win.blit(bulletImg, (bullets[i].x, bullets[i].y))

	if len(bombs) > 0:
		for i in range(len(bombs) - index):
			win.blit(bombImg, (bombs[i].x, bombs[i].y))

	pygame.display.update()

running = True

while running:
	if shootLoop > 0:
		shootLoop += 1
	if shootLoop > 3:
		shootLoop = 0

	if shootLoopB > 0:
		shootLoopB += 1
	if shootLoopB > 3:
		shootLoopB = 0

	bgX -= speed
	bgX2 -= speed

	if bgX < background.get_width() * -1:
		bgX = background.get_width()
	if bgX2 < background.get_width() * -1:
		bgX2 = background.get_width()

	reDrawWindow()

	if pygame.event.get(pygame.QUIT):
		running = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_UP] and y > -30:
		y -= vel

	if keys[pygame.K_DOWN] and y < 500:
		y += vel

	if keys[pygame.K_LEFT] and x + vel > vel:
		x -= vel

	if keys[pygame.K_RIGHT] and x < width - 125:
		x += vel

	if keys[pygame.K_SPACE] and shootLoop == 0:
		bulletX = x + s1
		bulletY = y + s2
		if len(bullets) <= 10:
			bullet = Bullet(bulletX, bulletY)
			bullets.append(bullet)

		shootLoop = 1

	if keys[pygame.K_s] or keys[pygame.K_l] and shootLoopB == 0:
		if index < 8:
			bombX = x + s1
			bombY = y + s2
			if len(bombs) <= 8:
				bomb = Bomb(bombX, bombY)
				bombs.append(bomb)
		else:
			index += 1

		shootLoopB = 1

	for helicopter in helicopters:
		try:
			if helicopter.y + helicopterImg.get_height() - 20 < y + planeImg.get_height() - 20 and helicopter.y + helicopterImg.get_height() > y:
				if helicopter.x + helicopterImg.get_width() < x + planeImg.get_width() and helicopter.x + planeImg.get_width() > x:
					game_over_screen()
					running = False
					time.sleep(0.5)
		except:
			pass

	for aeroplane in aeroplanes:
		try:
			if aeroplane.y + aeroplaneImg.get_height() - 20 < y + planeImg.get_height() - 20 and aeroplane.y + aeroplaneImg.get_height() > y:
				if aeroplane.x + aeroplaneImg.get_width() < x + planeImg.get_width() and aeroplane.x + planeImg.get_width() > x:
					game_over_screen()
					running = False
					time.sleep(0.5)
		except:
			pass

	for airplane in airplanes:
		try:
			if airplane.y + airplaneImg.get_height() - 20 < y + planeImg.get_height() - 20 and airplane.y + airplaneImg.get_height() > y:
				if airplane.x + airplaneImg.get_width() < x + planeImg.get_width() and airplane.x + planeImg.get_width() > x:
					game_over_screen()
					running = False
					time.sleep(0.5)
		except:
			pass

	for bullet in bullets:
		for i in range(4):
			if bullet.y + bulletImg.get_height() - 30 < helicopterY + helicopterImg.get_height() - 30 and bullet.y + bulletImg.get_height() > helicopterY:
				if bullet.x + bulletImg.get_width() < helicopterX + i * 200 + helicopterImg.get_width() and bullet.x + bulletImg.get_width() > helicopterX + i * 200:
					try:
						bullets.pop(bullets.index(bullet))
					except:
						pass
					visible[i] = False

		for i in range(3):
			if bullet.y + bulletImg.get_height() - 30 < helicopterY1 + helicopterImg.get_height() - 30 and bullet.y + bulletImg.get_height() > helicopterY1:
				if bullet.x + bulletImg.get_width() < helicopterX1 + i * 200 + helicopterImg.get_width() and bullet.x + bulletImg.get_width() > helicopterX1 + i * 200:
					try:
						bullets.pop(bullets.index(bullet))
					except:
						pass
					visibleH1[i] = False

		for i in range(6):
			if bullet.y + bulletImg.get_height() - 30 < helicopterY2 + helicopterImg.get_height() - 30 and bullet.y + bulletImg.get_height() > helicopterY2:
				if bullet.x + bulletImg.get_width() < helicopterX2 + i * 200 + helicopterImg.get_width() and bullet.x + bulletImg.get_width() > helicopterX2 + i * 200:
					try:
						bullets.pop(bullets.index(bullet))
					except:
						pass
					visibleH2[i] = False

		win.blit(bulletImg, (bullet.x, bullet.y))
		
		for i in range(6):
			if bullet.y + bulletImg.get_height() - 30 < aeroplaneY + aeroplaneImg.get_height() - 30 and bullet.y + bulletImg.get_height() > aeroplaneY:
				if bullet.x + bulletImg.get_width() < aeroplaneX + i * 200 + aeroplaneImg.get_width() and bullet.x + bulletImg.get_width() > aeroplaneX + i * 200:
					try:
						bullets.pop(bullets.index(bullet))
					except:
						pass
					visibleA[i] = False

		for i in range(4):
			if bullet.y + bulletImg.get_height() - 30 < airplaneY + airplaneImg.get_height() - 30 and bullet.y + bulletImg.get_height() > airplaneY:
				if bullet.x + bulletImg.get_width() < airplaneX + i * 200 + airplaneImg.get_width() and bullet.x + bulletImg.get_width() > airplaneX + i * 200:
					try:
						bullets.pop(bullets.index(bullet))
					except:
						pass
					visibleB[i] = False

		if bullet.x == width:
			try:
				bullets.pop(bullets.index(bullet))
			except:
				pass

		bullet.x += vel * 4

	for bomb in bombs:
		for i in range(4):
			if bomb.y + bombImg.get_height() - 30 < helicopterY + helicopterImg.get_height() - 30 and bomb.y + bombImg.get_height() > helicopterY:
				if bomb.x + bombImg.get_width() < helicopterX + i * 200 + helicopterImg.get_width() and bomb.x + bombImg.get_width() > helicopterX + i * 200:
					visible[i] = False

		for i in range(3):
			if bomb.y + bombImg.get_height() - 30 < helicopterY1 + helicopterImg.get_height() - 30 and bomb.y + bombImg.get_height() > helicopterY1:
				if bomb.x + bombImg.get_width() < helicopterX1 + i * 200 + helicopterImg.get_width() and bomb.x + bombImg.get_width() > helicopterX1 + i * 200:
					visibleH1[i] = False

		for i in range(2):
			if bomb.y + bombImg.get_height() - 30 < helicopterY2 + helicopterImg.get_height() - 30 and bomb.y + bombImg.get_height() > helicopterY2:
				if bomb.x + bombImg.get_width() < helicopterX2 + i * 200 + helicopterImg.get_width() and bomb.x + bombImg.get_width() > helicopterX2 + i * 200:
					visibleH2[i] = False

		win.blit(bombImg, (bomb.x, bomb.y))
		
		for i in range(6):
			if bomb.y + bombImg.get_height() - 30 < aeroplaneY + aeroplaneImg.get_height() - 30 and bomb.y + bombImg.get_height() > aeroplaneY:
				visible[i] = False

		for i in range(6):
			if bomb.y + bombImg.get_height() - 30 < aeroplaneY + aeroplaneImg.get_height() - 30 and bomb.y + bombImg.get_height() > aeroplaneY:
				if bomb.x + bombImg.get_width() < aeroplaneX + i * 200 + aeroplaneImg.get_width() and bomb.x + bombImg.get_width() > aeroplaneX + i * 200:
					visibleA[i] = False

		for i in range(6):
			if bomb.y + bombImg.get_height() - 30 < airplaneY + airplaneImg.get_height() - 30 and bomb.y + bombImg.get_height() > airplaneY:
				if bomb.x + bombImg.get_width() < airplaneX + i * 200 + airplaneImg.get_width() and bomb.x + bombImg.get_width() > airplaneX + i * 200:
					try:
						visibleB[i] = False
					except:
						pass

		bomb.x += vel + 5

	helicopterX -= vel
	helicopterX1 -= vel
	aeroplaneX -= vel
	airplaneX -= vel
	helicopterX2 -= 0.5
	if down:
		helicopterY2 += vel
		up = False
		if helicopterY2 >= height:
			down = False
			up = True
	if up:
		helicopterY2 -= vel
		down = False
		if helicopterY2 <= 0:
			up = False	
			down = True

	if True not in visible:
		if True not in visibleH1:
			if True not in visibleH2:
				if True not in visibleA:
					if True not in visibleB:
						you_won_screen()
						running = False
						time.sleep(1)

	pygame.display.update()

pygame.quit()
