import pygame

class Main:

    def __init__(self):
        #pygame is a wrapper for SDL
        pygame.init()

        self.screen = pygame.display.set_mode(size=(1200,800))

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                
            pygame.display.flip()

main = Main()
main.run_game()