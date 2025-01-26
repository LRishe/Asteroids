import pygame
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shot import Shot


def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots= pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2, shots = shots)
	asteroid_field = AsteroidField()


	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0,0,0))	
		player.press_space()
		for item in updatable:
			item.update(dt)
		for asteroid in asteroids:
			if asteroid.collides(player) == True:
				sys.exit("Game over")
		for asteroid in asteroids:
			for shot in shots:
				if asteroid.collides(shot):
					shot.kill()
					asteroid.split()
		for item in drawable:
			item.draw(screen)
		pygame.display.flip()
		tick = clock.tick(60)
		dt = tick / 1000

	

	   

if __name__ == "__main__":
	main()