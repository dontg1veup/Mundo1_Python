import pygame
pygame.init()
pygame.mixer.music.load('exemplo3s.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()
pygame.quit()
pygame.display.quit()

