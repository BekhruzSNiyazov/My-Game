#  *** BETA 5.3 ***  #

import pygame
import time
import random

pygame.init()
pygame.font.init()

width = 1250
height = 700

level1 = pygame.display.set_mode((width, height))

background = pygame.image.load("background.jpg")
planeImg = pygame.image.load("fighter.png")
helicopterImg = pygame.image.load("helicopter.png")
aeroplaneImg = pygame.image.load("aeroplane.png")
bulletImg = pygame.image.load("bullet.png")
explosionImg = pygame.image.load("explosion.png")
bombImg = pygame.image.load("bomb.png")
iconImg = pygame.image.load("icon.png")
airplaneImg = pygame.image.load("airplane.png")
greatplaneImg = pygame.image.load("greatplane.png")

bgX = 0
bgX2 = background.get_width()

pygame.display.set_caption("Air Battle")
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
visibleGP = True
index = 0
down = True
up = False
greatPlaneX = 3000
greatPlaneY = -600
hitNum1 = 0
hitNum2 = 0
level1Completed = False

class GreatPlane():
	def __init__(self, x, y, visible):
		self.visible = visible
		if self.visible:
			self.x = x
			self.y = y

	def draw(self):
		if self.visible:
			level1.blit(greatplaneImg, (greatPlaneX, greatPlaneY))

class Aeroplane():
	def __init__(self, x, y, visible):
		self.visible = visible
		if self.visible:
			self.x = x
			self.y = y

	def draw(self):
		if self.visible:
			level1.blit(aeroplaneImg, (self.x, self.y))

class Airplane():
	def __init__(self, x, y, visible):
		self.visible = visible
		if self.visible:
			self.x = x
			self.y = y

	def draw(self):
		if self.visible:
			level1.blit(airplaneImg, (self.x, self.y)) 

class Helicopter():
	def __init__(self, x, y, visible):
		self.visible = visible
		if self.visible:
			self.x = x
			self.y = y

	def draw(self):
		if self.visible:
			level1.blit(helicopterImg, (self.x, self.y))

class Bullet():
	global bulletX, bulletY
	def __init__(self):
		self.x = bulletX
		self.y = bulletY

class Bomb():
	global bombX, bombY
	def __init__(self):
		self.x = bombX
		self.y = bombY

def game_over_screen():
	font = pygame.font.SysFont("Arial", 50, True)
	text = font.render("GAME OVER", 50, (255, 0, 0))
	level1.blit(text, (400, 300))
	level1.blit(explosionImg, (x + 10, y + 10))
	pygame.display.update()

def you_won_screen():
	font = pygame.font.SysFont("Arial", 50, True)
	text = font.render("YOU WON!", 50, (255, 255, 255))
	level1.blit(text, (400, 300))
	pygame.display.update()

def reDrawWindow():
	global helicopterX, helicopterY, helicopters, bulletX, bulletY, bullets, x, y, visible, aeroplaneX, aeroplaneY, aeroplanes, visibleA, visibleGP, greatplaneImg, greatPlaneX, greatPlaneY, gpBulletX, gpBulletY, directions, vel

	level1.blit(background, (bgX, 0))
	level1.blit(background, (bgX2, 0))
	level1.blit(planeImg, (x, y))

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
			level1.blit(bulletImg, (bullets[i].x, bullets[i].y))

	if len(bombs) > 0:
		for i in range(len(bombs) - index):
			level1.blit(bombImg, (bombs[i].x, bombs[i].y))

	greatPlane = GreatPlane(greatPlaneX, greatPlaneY, visibleGP)
	greatPlane.draw()
	
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

	if keys[pygame.K_UP] and y - vel > 0:
		y -= vel

	if keys[pygame.K_DOWN] and y + vel < height - planeImg.get_height():
		y += vel

	if keys[pygame.K_LEFT] and x - vel > 0:
		x -= vel

	if keys[pygame.K_RIGHT] and x + vel < width - planeImg.get_width():
		x += vel

	if keys[pygame.K_SPACE] and shootLoop == 0:
		bulletX = x + s1
		bulletY = y + s2
		bullet = Bullet()
		bullets.append(bullet)

		shootLoop = 1

	if keys[pygame.K_s] or keys[pygame.K_l] and shootLoopB == 0:
		if index < 5:
			bombX = x + s1
			bombY = y + s2
			if len(bombs) <= 5:
				bomb = Bomb()
				bombs.append(bomb)
		else:
			index += 1

		shootLoopB = 1

	try:
		if greatPlane.y + greatplaneImg.get_height() < y + planeImg.get_height() - 20 and greatPlane.y + greatplaneImg.get_height() > y:
			if greatPlane.x + greatplaneImg.get_width() < x + planeImg.get_height() and greatPlane.x + planeImg.get_width() > x:
				game_over_screen()
				running = False
				time.sleep(0.1)
	except:
		pass

	for helicopter in helicopters:
		try:
			if helicopter.y + helicopterImg.get_height() - 20 < y + planeImg.get_height() - 20 and helicopter.y + helicopterImg.get_height() > y:
				if helicopter.x + helicopterImg.get_width() < x + planeImg.get_width() and helicopter.x + planeImg.get_width() > x:
					game_over_screen()
					running = False
					time.sleep(0.1)
		except:
			pass

	for aeroplane in aeroplanes:
		try:
			if aeroplane.y + aeroplaneImg.get_height() - 20 < y + planeImg.get_height() - 20 and aeroplane.y + aeroplaneImg.get_height() > y:
				if aeroplane.x + aeroplaneImg.get_width() < x + planeImg.get_width() and aeroplane.x + planeImg.get_width() > x:
					game_over_screen()
					running = False
					time.sleep(0.1)
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
					try:
						visible[i] = False
					except:
						pass

		for i in range(3):
			if bullet.y + bulletImg.get_height() - 30 < helicopterY1 + helicopterImg.get_height() - 30 and bullet.y + bulletImg.get_height() > helicopterY1:
				if bullet.x + bulletImg.get_width() < helicopterX1 + i * 200 + helicopterImg.get_width() and bullet.x + bulletImg.get_width() > helicopterX1 + i * 200:
					try:
						bullets.pop(bullets.index(bullet))
					except:
						pass
					try:
						visibleH1[i] = False
					except:
						pass

		for i in range(6):
			if bullet.y + bulletImg.get_height() - 30 < helicopterY2 + helicopterImg.get_height() - 30 and bullet.y + bulletImg.get_height() > helicopterY2:
				if bullet.x + bulletImg.get_width() < helicopterX2 + i * 200 + helicopterImg.get_width() and bullet.x + bulletImg.get_width() > helicopterX2 + i * 200:
					try:
						bullets.pop(bullets.index(bullet))
					except:
						pass
					try:
						visibleH2[i] = False
					except:
						pass

		level1.blit(bulletImg, (bullet.x, bullet.y))
		
		for i in range(6):
			if bullet.y + bulletImg.get_height() - 30 < aeroplaneY + aeroplaneImg.get_height() - 30 and bullet.y + bulletImg.get_height() > aeroplaneY:
				if bullet.x + bulletImg.get_width() < aeroplaneX + i * 200 + aeroplaneImg.get_width() and bullet.x + bulletImg.get_width() > aeroplaneX + i * 200:
					try:
						bullets.pop(bullets.index(bullet))
					except:
						pass
					try:
						visibleA[i] = False
					except:
						pass

		for i in range(4):
			if bullet.y + bulletImg.get_height() - 30 < airplaneY + airplaneImg.get_height() - 30 and bullet.y + bulletImg.get_height() > airplaneY:
				if bullet.x + bulletImg.get_width() < airplaneX + i * 200 + airplaneImg.get_width() and bullet.x + bulletImg.get_width() > airplaneX + i * 200:
					try:
						bullets.pop(bullets.index(bullet))
					except:
						pass
					try:
						visibleB[i] = False
					except:
						pass

		if bullet.y + bulletImg.get_height() - 30 < greatPlaneY + greatplaneImg.get_height() and bullet.y + bulletImg.get_height() > greatPlaneY:
			if bullet.x + bulletImg.get_width() < greatPlaneX + greatplaneImg.get_width() and bullet.x + bulletImg.get_width() > greatPlaneX:
				try:
					bullets.pop(bullets.index(bullet))
				except:
					pass
				try:
					if hitNum1 >= 800:
						visibleGP = False
					else:
						hitNum1 += 1
				except:
					pass

		if bullet.x == width:
			try:
				bullets.pop(bullets.index(bullet))
			except:
				pass

		bullet.x += vel * 6

	for bomb in bombs:
		for i in range(4):
			if bomb.y + bombImg.get_height() - 30 < helicopterY + helicopterImg.get_height() - 30 and bomb.y + bombImg.get_height() > helicopterY:
				if bomb.x + bombImg.get_width() < helicopterX + i * 200 + helicopterImg.get_width() and bomb.x + bombImg.get_width() > helicopterX + i * 200:
					try:
						visible[i] = False
					except:
						pass

		for i in range(3):
			if bomb.y + bombImg.get_height() - 30 < helicopterY1 + helicopterImg.get_height() - 30 and bomb.y + bombImg.get_height() > helicopterY1:
				if bomb.x + bombImg.get_width() < helicopterX1 + i * 200 + helicopterImg.get_width() and bomb.x + bombImg.get_width() > helicopterX1 + i * 200:
					try:
						visibleH1[i] = False
					except:
						pass

		for i in range(2):
			if bomb.y + bombImg.get_height() - 30 < helicopterY2 + helicopterImg.get_height() - 30 and bomb.y + bombImg.get_height() > helicopterY2:
				if bomb.x + bombImg.get_width() < helicopterX2 + i * 200 + helicopterImg.get_width() and bomb.x + bombImg.get_width() > helicopterX2 + i * 200:
					try:
						visibleH2[i] = False
					except:
						pass

		level1.blit(bombImg, (bomb.x, bomb.y))
		
		for i in range(6):
			if bomb.y + bombImg.get_height() - 30 < aeroplaneY + aeroplaneImg.get_height() - 30 and bomb.y + bombImg.get_height() > aeroplaneY:
				try:
					visible[i] = False
				except:
					pass

		for i in range(6):
			if bomb.y + bombImg.get_height() - 30 < aeroplaneY + aeroplaneImg.get_height() - 30 and bomb.y + bombImg.get_height() > aeroplaneY:
				if bomb.x + bombImg.get_width() < aeroplaneX + i * 200 + aeroplaneImg.get_width() and bomb.x + bombImg.get_width() > aeroplaneX + i * 200:
					try:
						visibleA[i] = False
					except:
						pass

		for i in range(6):
			if bomb.y + bombImg.get_height() - 30 < airplaneY + airplaneImg.get_height() - 30 and bomb.y + bombImg.get_height() > airplaneY:
				if bomb.x + bombImg.get_width() < airplaneX + i * 200 + airplaneImg.get_width() and bomb.x + bombImg.get_width() > airplaneX + i * 200:
					try:
						visibleB[i] = False
					except:
						pass

		if bomb.y + bombImg.get_height() - 30 < greatPlaneY + greatplaneImg.get_height() - 30 and bomb.y + bombImg.get_height() > greatPlaneY:
			if bomb.x + bombImg.get_width() < greatPlaneX + greatplaneImg.get_width() and bomb.x + bombImg.get_width() > greatPlaneX:
				try:
					if hitNum2 >= 400:
						visibleGP = False
					else:
						hitNum2 += 1
				except:
					pass

		if bomb.x == width:
			try:
				bomb.pop(bombs.index(bombs))
			except:
				pass

		bomb.x += vel + 5

	helicopterX -= vel
	helicopterX1 -= vel
	aeroplaneX -= vel
	airplaneX -= vel

	if greatPlaneX >= 700:
		greatPlaneX -= vel / 2
	if greatPlaneX <= 700:
		if greatPlaneY < 200:
			greatPlaneY += vel
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

	if not visibleGP:
		you_won_screen()
		level1Completed = True
		running = False
		time.sleep(0.1)

	if True not in visible:
		if True not in visibleH1:
			if True not in visibleH2:
				if True not in visibleA:
					if True not in visibleB:
						you_won_screen()
						level1Completed = True
						running = False
						time.sleep(0.1)

	pygame.display.update()

exit()

if level1Completed:
	pass
