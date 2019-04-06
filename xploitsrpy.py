import pygame
import time
# ====XploitsR ScreenSaver===#

# load/import modules
pygame.init()
width, height = 800, 600
backgroundColor = 255, 255, 255
imageSpeed = [1, 1]

# set the display mode
screen = pygame.display.set_mode((width, height))

# set image
image = pygame.image.load("ok.png")
imageRect = image.get_rect()

while True:
    screen.fill(backgroundColor)
    screen.blit(image, imageRect)
    imageRect = imageRect.move(imageSpeed)

    if imageRect.left < 0 or imageRect.right > width:
        imageSpeed[0] = -imageSpeed[0]

    if imageRect.top < 0 or imageRect.bottom > height:
        imageSpeed[1] = -imageSpeed[1]

    pygame.display.flip()
    time.sleep(10 / 1000)
