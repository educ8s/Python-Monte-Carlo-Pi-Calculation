import math, random, pygame
from sys import exit

class MonteCarlo:

    def __init__(self, window, circle_radius, points):
        pygame.init()
        print(f"The simulation will run for {points} iterations")
        self.screen = pygame.display.set_mode((window[0], window[1]), pygame.FULLSCREEN)
        self.screen.fill("Grey10")
        pygame.display.set_caption("Monte Carlo Pi Estimation")
        pygame.time.Clock().tick(1)
        pygame.display.flip()
        self.font_small = pygame.font.Font(None, 40)
        self.width = circle_radius*2
        self.height = circle_radius*2
        self.pi = 0.0
        self.inside = 0
        self.window = window
        self.points = points
        self.points_list = []
        self.display_title()
        self.display_square(circle_radius)
        self.draw_line()
        self.display_multiplication()
        pygame.display.update()
    
    def display_title(self):
        self.font = pygame.font.SysFont("arial", 50)
        self.title_surface = self.font.render("Monte Carlo Pi Estimation", True, "White")
        text_rect = self.title_surface.get_rect(center=(self.window[0]/2, 50))
        self.screen.blit(self.title_surface,text_rect)
    
    def display_number_of_red(self):
        subtitle = self.font_small.render(f"100000000", True, (224,72,52))
        subtitle_rect = subtitle.get_rect(center = (930, 830))
        subtitle.fill("Grey10")
        self.screen.blit(subtitle,subtitle_rect)
        subtitle = self.font_small.render(str(self.inside), True, (224,72,52))
        self.screen.blit(subtitle,subtitle_rect)

    def display_total_number(self):
        subtitle = self.font_small.render(f"100000000", True, "White")
        subtitle_rect = subtitle.get_rect(center = (930, 870))
        subtitle.fill("Grey10")
        self.screen.blit(subtitle,subtitle_rect)
        subtitle = self.font_small.render(str(len(self.points_list)), True, "White")
        self.screen.blit(subtitle,subtitle_rect)

    def display_square(self, circle_radius):
        pygame.draw.rect(self.screen, "White", (((self.window[0]-self.width)/2)-2, 98, ((circle_radius+3)*2),(circle_radius+3)*2), 2)  # width = 2

    def display_multiplication(self):
        mult = self.font_small.render( "4 *", True, "White")
        mult_rect = mult.get_rect(center = (770, 850))
        self.screen.blit(mult,mult_rect)

    def draw_line(self):
        print("Drawing line...")
        line = pygame.draw.line(self.screen, "White", (800,850), (1000,850), 2)

    def display_pi(self):
        subtitle = self.font_small.render(f"= 3.00000000  ", True, "White")
        subtitle_rect = subtitle.get_rect(center = (1110, 850))
        subtitle.fill("Grey10")
        self.screen.blit(subtitle,subtitle_rect)
        subtitle = self.font_small.render(f"= {self.pi}  ", True, "White")
        self.screen.blit(subtitle,subtitle_rect)

    def loop(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
            if len(self.points_list) < self.points:
                    self.calculate()

            self.display_pi()
            pygame.display.update()

    def generatePoint(self):
        x = random.randint(0, self.width)
        y = random.randint(0, self.height)
        return (x,y)

    def isPointInCircle(self,point):
        x = point[0] - self.width/2
        y = point[1] - self.width/2
        if x * x + y * y <= (self.width/2) * (self.height/2):
            return True
        else:
            return False

    def calculatePi(self):
        self.pi = round(4*(self.inside/len(self.points_list)),8)

    def draw(self,point):
        circle_surface= pygame.Surface((2,2))
        if self.isPointInCircle(point):
            circle_surface.fill((224,72,52)) #Red color
        else:
            circle_surface.fill((0,90,145))  #Blue color
        self.screen.blit(circle_surface,(((self.window[0]-self.width)/2)+point[0],100+point[1]) )
        
    def calculate(self):
        point = self.generatePoint()
        self.points_list.append(point)
        if self.isPointInCircle(point):
            self.inside += 1
        self.calculatePi()
        self.draw(point)
        self.display_number_of_red()
        self.display_total_number()