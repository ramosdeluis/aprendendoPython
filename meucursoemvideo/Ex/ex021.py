import pygame
pygame.init()
pygame.mixer.music.load('../Músicas/ex021.mp3')
pygame.mixer.music.play()
input('Curte o som!')
pygame.event.wait()
