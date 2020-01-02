import pygame
import time

pygame.init()
pygame.font.init()

width = 1000
height = 600

win = pygame.display.set_mode((width, height))

background = pygame.image.load("background.jpg")
planeImg = pygame.image.load("fighter.png")
helicopterImg = pygame.image.load("helicopter.png")
bulletImg = pygame.image.load("bullet.png")
explosion = pygame.image.load("explosion.png")
bulletImg = pygame.image.load("bullet.png")

bgX = 0
bgX2 = background.get_width()

pygame.display.set_caption("My Game")

x = 100
y = 150
s1 = 30
s2 = 85
helicopterX = 1500
helicopterY = 10
helicopters = []
bulletX = x + s1
bulletY = y + s2
bullets = []
vel = 5
speed = 5
shootLoop = 0
visible = [True, True, True, True]

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

def game_over_screen():
	font = pygame.font.SysFont("Arial", 50, True)
	text = font.render("GAME OVER", 50, (255, 0, 0))
	win.blit(text, (500, 300))
	win.blit(explosion, (x - 50, y - 50))
	pygame.display.update()	

def reDrawWindow():
	global helicopterX, helicopterY, helicopters, bulletX, bulletY, bullets, x, y, visible

	win.blit(background, (bgX, 0))
	win.blit(background, (bgX2, 0))
	win.blit(planeImg, (x, y))

	for i in range(4):
		helicopter = Helicopter(helicopterX + i * 200, helicopterY, visible[i])
		helicopter.draw()
		helicopters.append(helicopter)
	
	if helicopterX < 300:
		helicopterY += vel

	if len(bullets) > 0:
		for i in range(len(bullets)):
			win.blit(bulletImg, (bullets[i].x, bullets[i].y))

	pygame.display.update()

running = True

while running:
	if shootLoop > 0:
		shootLoop += 1
	if shootLoop > 3:
		shootLoop = 0

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

	for helicopter in helicopters:
		try:
			if helicopter.y + helicopterImg.get_height() - 20 < y + planeImg.get_height() - 20 and helicopter.y + helicopterImg.get_height() > y:
				if helicopter.x + helicopterImg.get_width() < x + planeImg.get_width() and helicopter.x + planeImg.get_width() > x:
					game_over_screen()
					running = False
					time.sleep(0.5)
		except Exception as e:
			print(e)

	for bullet in bullets:
		for i in range(4):
			if bullet.y + bulletImg.get_height() - 30 < helicopterY + helicopterImg.get_height() - 30 and bullet.y + bulletImg.get_height() > helicopterY:
				if bullet.x + bulletImg.get_width() < helicopterX + i * 200 + helicopterImg.get_width() and bullet.x + bulletImg.get_width() > helicopterX + i * 200:
					bullets.pop(bullets.index(bullet))
					visible[i] = False

			win.blit(bulletImg, (bullet.x, bullet.y))
				
		if bullet.x == width:
			bullets.pop(bullets.index(bullet))

		bullet.x += vel + 5

	helicopterX -= vel

	pygame.display.update()

pygame.quit()