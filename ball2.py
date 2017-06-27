# Import a library of functions called 'pygame'
import pygame
# Initialize the game engine
pygame.init()
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
size = (1200, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
class Ball():
    def __init__(self):
        # --- Class Attributes ---
        # Ball position
        self.x = 0
        self.y = 0
 
        # Ball's vector
        self.change_x = 0
        self.change_y = 0
 
        # Ball size
        self.size = 10
 
        # Ball color
        self.color = [255,255,255]

    def move(self):
        self.x = self.x + self.change_x
        self.y += self.change_y
 
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size )

theBall = Ball()
theBall.x = 100
theBall.y = 100
theBall.change_x = 0
theBall.change_y = 0
theBall.color = [255,0,0]
walkingleft = 1
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
    screen.fill(WHITE)
    background_image = pygame.image.load("Town.png").convert()
    screen.blit(background_image, [0, 0])
    
  
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                theBall.change_y= -4
                from pygame.locals import*
                img = pygame.image.load('Military(back).png')
                screen.blit(img,(theBall.x,theBall.y))
            elif event.key == pygame.K_s:
                theBall.change_y = 4
                from pygame.locals import*
                img = pygame.image.load('Military(front).png')
                screen.blit(img,(theBall.x,theBall.y))
            elif event.key == pygame.K_a:
                theBall.change_x = -4
                if walkingleft >= 3 and walkingleft <= 5:
                    from pygame.locals import*
                    img = pygame.image.load('Military(left.1).png')
                    screen.blit(img,(theBall.x,theBall.y))
                elif walkingleft >= 6 and walkingleft <= 8:
                    from pygame.locals import*
                    img = pygame.image.load('Military(left.2).png')
                    screen.blit(img,(theBall.x,theBall.y))
                elif walkingleft == 9 or walkingleft == 2 or walkingleft == 1:
                    from pygame.locals import*
                    img = pygame.image.load('Military(left.3).png')
                    screen.blit(img,(theBall.x,theBall.y))
            elif event.key == pygame.K_d:
                theBall.change_x = 4
                from pygame.locals import*
                img = pygame.image.load('Military(right).png')
                screen.blit(img,(theBall.x,theBall.y))
    elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                theBall.change_y = 0
                theBall.change_x = 0
                from pygame.locals import*
                img = pygame.image.load('Military(back).png')
                screen.blit(img,(theBall.x,theBall.y))
            elif event.key == pygame.K_s:
                theBall.change_y = 0
                theBall.change_x = 0
                from pygame.locals import*
                img = pygame.image.load('Military(front).png')
                screen.blit(img,(theBall.x,theBall.y))
            elif event.key == pygame.K_a:
                theBall.change_y = 0
                theBall.change_x = 0
                from pygame.locals import*
                img = pygame.image.load('Military(left).png')
                screen.blit(img,(theBall.x,theBall.y))
            elif event.key == pygame.K_d:
                theBall.change_y = 0
                theBall.change_x = 0
                from pygame.locals import*
                img = pygame.image.load('Military(right).png')
                screen.blit(img,(theBall.x,theBall.y))
        
 
    # --- Class Methods ---
    
    if walkingleft == 9:
        walkingleft = 0
    walkingleft = walkingleft + 1
    theBall.move()
  
    

 
##    pygame.draw.ellipse(screen, WHITE, [ballx, bally, 20, 20], 0)
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
pygame.quit()
