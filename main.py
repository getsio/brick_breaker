import pygame
import pygame.display
import pygame.draw
import pygame.time
import pygame.event
from abc import ABCMeta, abstractmethod
from src.character import GameCharacter

class Game:
  def __init__(self, fps) -> None:
    pygame.init()
    self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    self.fps = fps
    self.game_running = True

  def run(self):
    clock = pygame.time.Clock()

    while self.game_running:
      for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
          self.game_running = False
        elif ev.type == pygame.KEYDOWN:
          if ev.key == pygame.K_ESCAPE:
            self.game_running = False
      
      clock.tick(self.fps)

if __name__ == '__main__':
  game = Game(60)
  game.run()