import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("Asteroids")

pointA = [100, 100]
pointB = [150,100]
pointC = [125, 150]
triangle_vertices = [pointA, pointB, pointC]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_w:
                for point in triangle_vertices:
                    point[1] -= 1
            if event.type == pygame.K_s:
                for point in triangle_vertices: 
                    point[1] += 1
            if event.type == pygame.K_a:
                for point in triangle_vertices:
                    point[0] += 1
            if event.type == pygame.K_d:
                for point in triangle_vertices:
                    point[0] += 1
                
    
    screen.fill((255, 255, 255))
    pygame.draw.polygon(screen, (255, 255, 255), triangle_vertices)
    pygame.display.flip()
pygame.quit()
