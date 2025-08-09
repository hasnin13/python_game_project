import pygame
from settings import Settings

class Ship:
    def __init__(self, screen):
        ship_image = pygame.image.load('./images/spaceship.png')
        self.ship_image = pygame.transform.scale(ship_image, (40,100))
        self.screen = screen

    def blitme(self):
        self.screen.blit(self.ship_image,(400,100))

class Main:

    def __init__(self):
        #pygame is a wrapper for SDL
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(size=(
            self.settings.width, 
            self.settings.height
            ))

        pygame.display.set_caption('Alien Invention')

        self.ship = Ship(self.screen)

        self.clock = pygame.time.Clock()
        #font for fps
        self.font = pygame.font.SysFont("Arial",24)
        
    
    
    def run_game(self):
         
         x= 100
         y= 100
         while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.screen.fill(self.settings.bg_color) # this is the bg
            self.render_fps(self.screen, self.clock, self.font)
            self.ship.blitme()


            pygame.draw.rect(self.screen, (255,255,255),(x, y,200,100)) 
            x+= .1
            y+= .2

            pygame.display.flip()
            self.clock.tick()

    def render_fps(self, screen,clock,font):
        fps = int(clock.get_fps())
        fps_text = font.render(f"FPS:{fps}", True, (0,0,0))
        screen.blit(fps_text, (10,10))





main = Main()
main.run_game()