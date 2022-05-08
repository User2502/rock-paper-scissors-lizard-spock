import pygame
import math
import random
pygame.init()


pygame.display.set_caption('Rock, Paper, Scissors')
SIZE = WIDTH, HEIGHT = 1920, 1080
win = pygame.display.set_mode(SIZE)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (220, 65, 96)
LIGHT_GREY = (223, 223, 223)
DARK_BLUE = (25, 38, 72)
DARK_BLUE2 = (62,66,91)
REALLY_DARK_BLUE = (17, 26, 50)
BLUE = (79, 106, 245)
GREY = (184, 191, 209)
GREY2 = (91, 107, 132)
GREY3 = (87,85,106)
GREY4 = (135,139,166)
ORANGE = (235, 163, 29)
PURPLE = (136, 87, 228)
LIGHT_BLUE = (73, 185, 207)
TOP_BORDER_COLOR_OUTLINE = (59, 76, 102)
TOP_BORDER_COLOR = (92, 110, 134)
BETTER_WHITE = (247, 247, 247)
SCORE_TEXT_COLOR = (68, 76, 159)
def PerfectionistFont(size=30):
    return pygame.font.Font('Perfectionist.ttf', size)
FPS = 60
clicked_choice = False
score = 0
rule_popup_active = False
game_data = ()
color_match = {'rock': RED, 'paper': BLUE, 'scissors': ORANGE, 'lizard': PURPLE, 'spock': LIGHT_BLUE}


def draw_win():
    global clicked_choice, score, rule_popup_active, game_data, color_match
    if not rule_popup_active:
        win.fill(DARK_BLUE)
    else:
        win.fill(REALLY_DARK_BLUE)
    
    def draw_icon(name,pos,color):
        pygame.draw.circle(win, GREY, pos, 120)
        pygame.draw.circle(win, LIGHT_GREY, (pos[0],pos[1]+5), 100)
        pygame.draw.circle(win, color, pos, 120, 20)
        item = pygame.image.load(f'images/icon-{name}.png')
        item = pygame.transform.scale(item, (80, 80))
        win.blit(item, (pos[0]-40,pos[1]-40))

    def get_length(pos):
        x1,y1 = pos
        x2,y2 = (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
        return math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))

    def calc_win(c1,c2):
        global score
        dictionary = {'lizard': ('scissors', 'rock'), 'spock': ('lizard','paper'), 'scissors': ('spock', 'rock'), 'paper': ('scissors', 'lizard'), 'rock': ('paper', 'spock')}
        if c1 in dictionary[c2]:
            score += 1
            return ('You Won!', c1, c2)
        return (('You Lost!', c1, c2) if c2 in dictionary[c1]
        else ('Draw!', c1, c2))


    pygame.draw.rect(win, TOP_BORDER_COLOR_OUTLINE, (458, 8, 1000, 250), 8, 20)
    pygame.draw.rect(win, TOP_BORDER_COLOR, (460, 10, 996, 246), 4, 20)
    logo = pygame.image.load('images/logo-bonus.png')
    logo = pygame.transform.scale(logo, (160, 160))
    win.blit(logo, (500,52))
    pygame.draw.rect(win, BETTER_WHITE, (1190,52,220,155), border_radius=15)
    score_title_text = PerfectionistFont(70).render('SCORE', 1, SCORE_TEXT_COLOR)
    win.blit(score_title_text, (1190+((220-score_title_text.get_width())//2), 62))
    score_text = PerfectionistFont(70).render(str(score), 1, GREY3)
    win.blit(score_text, (1190+((220-score_text.get_width())//2), 132))
    pygame.draw.rect(win, GREY4, (1580, 915, 300, 125), 4, 20)
    score_text = PerfectionistFont(90).render('RULES', 1, BETTER_WHITE)
    win.blit(score_text, (1730-score_text.get_width()//2, 915+125//2-score_text.get_height()//2+5))

    if not clicked_choice:
            pentagon = pygame.image.load('images/bg-pentagon.png')
            pentagon = pygame.transform.scale(pentagon, (500, 500))
            win.blit(pentagon, (710,400))
            for item in [['rock',(1100,885),RED],['paper',(1190,595),BLUE],['scissors',(970,400),ORANGE],['lizard',(810,885),PURPLE],['spock',(730,595),LIGHT_BLUE]]:
                draw_icon(item[0],item[1],item[2])
                if pygame.mouse.get_pressed()[0] and not rule_popup_active:
                    if get_length(item[1])<=120:
                        game_data = calc_win(item[0],random.choice(['rock','paper','scissors','lizard','spock']))
                        clicked_choice = True
    else:
        for item in [[game_data[1],(580,595)],[game_data[2],(1340,595)]]:
            draw_icon(item[0],item[1],color_match[item[0]])
        you_text = PerfectionistFont(100).render('YOU', 1, BETTER_WHITE)
        win.blit(you_text, (580-you_text.get_width()//2,370))
        computer_text = PerfectionistFont(100).render('COMPUTER', 1, BETTER_WHITE)
        win.blit(computer_text, (1340-computer_text.get_width()//2,370))
        outcome_text = PerfectionistFont(100).render(game_data[0], 1, BETTER_WHITE)
        win.blit(outcome_text, (960-outcome_text.get_width()//2,545-outcome_text.get_height()//2))
        pygame.draw.rect(win, BETTER_WHITE, (860, 595, 200, 125), border_radius=20)
        play_again_text = PerfectionistFont(60).render('Play Again?', 1, DARK_BLUE2)
        win.blit(play_again_text, (960-play_again_text.get_width()//2,660-play_again_text.get_height()//2))
        if pygame.mouse.get_pressed()[0] and not rule_popup_active:
            if 860<pygame.mouse.get_pos()[0]<1060 and 595<pygame.mouse.get_pos()[1]<720:
                clicked_choice = False



    if pygame.mouse.get_pressed()[0] and not rule_popup_active and 1580<pygame.mouse.get_pos()[0]<1880 and 915<pygame.mouse.get_pos()[1]<1040:
        rule_popup_active = True
    if rule_popup_active:
        pygame.draw.rect(win, BETTER_WHITE, (560, 340, 800, 500), border_radius=10)
        close_popup_icon = pygame.image.load('images/icon-close.png')
        close_popup_icon = pygame.transform.scale(close_popup_icon, (60, 60))
        win.blit(close_popup_icon, (1280,360))
        rules_popup_text = PerfectionistFont(70).render('RULES', 1, DARK_BLUE2)
        win.blit(rules_popup_text, (630,380))
        rules_guide = pygame.image.load('images/image-rules-bonus.png')
        rules_guide = pygame.transform.scale(rules_guide, (360, 360))
        win.blit(rules_guide, (960-rules_guide.get_width()//2,440))
    if pygame.mouse.get_pressed()[0] and rule_popup_active and 1280<pygame.mouse.get_pos()[0]<1340 and 360<pygame.mouse.get_pos()[1]<420:
        rule_popup_active = False

    pygame.display.update()


def main():
    running = True
    clock = pygame.time.Clock()
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        draw_win()
    pygame.quit()


if __name__ == '__main__':
    main()