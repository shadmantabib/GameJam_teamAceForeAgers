import pygame, sys
from settings import *
from level import Level
from ui import UI


Background=pygame.image.load("background.png")
About=pygame.image.load("about.png")
Play=pygame.image.load("Play.png")
Scores=pygame.image.load("scores.png")
Instruction=pygame.image.load("instruction.png")




class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Deadlock Paragon')
        self.clock = pygame.time.Clock()
        self.page_index=0
        self.a=1
       # self.highscore=0

        self.level = Level()
        main_sound = pygame.mixer.Sound('../audio/main.mp3')
        main_sound.play(loops=-1)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

            self.screen.fill('black')
            Font=pygame.font.SysFont('Comic Sans MS',30,True,True)
            Font1=pygame.font.SysFont('Berlin Sans FB Demi',72,True,False)
            if(self.page_index==1):
                self.level.run()
            elif(self.page_index==0):
                self.screen.blit(Background,(0,0))
                #text1=Font.render("NewGame",1,(255,0,0))
                #text2=Font.render("High Score",1,(255,0,0))
                #self.screen.blit(text1,(30,20))
                #self.screen.blit(text2,(450,20))
                text = Font1.render("Deadlock Paragon",1,(238, 75, 43))
                self.screen.blit(text,(360,60))
                self.screen.blit(Play,(530,160))
                self.screen.blit(About,(530,295))
                self.screen.blit(Instruction,(530,430))
                self.screen.blit(Scores,(530,565))
                if event.type==pygame.MOUSEBUTTONUP:
                    self.a=0
                    mmx, mmy = pygame.mouse.get_pos()
                    if(mmx>=500 and mmx<=800 and mmy>=158 and mmy<=255):
                        self.page_index=1
                    elif(mmx>=500 and mmx<=800 and mmy>=293 and mmy<=390):
                        self.page_index=3

                    elif(mmx>=500 and mmx<=800 and mmy>=428 and mmy<=525):
                        self.page_index=4
                    elif (mmx >= 500 and mmx <= 800 and mmy >= 563 and mmy <= 660):
                        self.page_index = 2
            elif(self.page_index==2):
                self.screen.blit(Background,(0,0))
                text3=Font.render("Back",1,(255,250,250))
                self.screen.blit(text3,(300,300))
                fp=open("highest_score.txt",'r')
                highscore=fp.read()
                text4 = Font.render("Highest Score : "+str(highscore), 1, (255, 0, 0))
                self.screen.blit(text4, (450, 200))
                if event.type == pygame.MOUSEBUTTONUP:
                    mx,my=pygame.mouse.get_pos()
                    if(mx>=290 and mx<=400 and my>=280 and my<=340):
                        self.page_index=0


            elif(self.page_index==4):
                self.screen.blit(Background, (0, 0))
                text5 = Font.render("1. Use up down,left,right arrow for moving the player.", 1, (255, 255, 255))
                text6 = Font.render("2. Press 'Spaceber' to kill your enemies.", 1, (255, 255, 255))
                text7 = Font.render("3. Press 'Left control' to use fire power.", 1, (255, 255, 255))
                text8 = Font.render("4. Press 'q' to change your weapon.", 1, (255, 255, 255))
                text9 = Font.render("Happy gaming..surprises are awaited for you.", 1, (255, 255, 255))
                text10 = Font.render("Good Luck!!!", 1, (255, 255, 255))
                text11 = Font.render("Back", 1, (255, 0, 0))

                self.screen.blit(text5, (170, 60))
                self.screen.blit(text6, (170, 100))
                self.screen.blit(text7, (170, 140))
                self.screen.blit(text8, (170, 180))
                self.screen.blit(text9, (170, 270))
                self.screen.blit(text10, (360, 320))
                self.screen.blit(text11, (800, 400))

                if event.type == pygame.MOUSEBUTTONUP:
                    mx, my = pygame.mouse.get_pos()
                    if (mx >= 790 and mx <= 900 and my >= 390 and my <= 450):
                        self.page_index = 0


            elif (self.page_index==3):
                self.screen.blit(Background,(0,0))
                text12=Font.render("While wandering in the desolated island Setsuko found two days ago,she observed",1,(255,255,255))
                text13=Font.render("a weird fact that  'is not supposed to do'. As long as the zombies are alive",1,(255,255,255))
                text14=Font.render("they are ok with their number. However,the scene changes quite drastically",1,(255,255,255))
                text15=Font.render("in case one attempts to terminate the monster.It immediately emreges from",1,(255,255,255))
                text16=Font.render("the nearest coordinates approaching the terminator all over again.",1,(255,255,255))
                text17=Font.render("Facing the unusual effect,Setsuko has nothing but escape,thus suck in a",1,(255,255,255))
                text18=Font.render("deadlock. Shooting and fighting against the enemies gonna be probable",1,(255,255,255))
                text19=Font.render("ultimate destiny !!!",1,(255,255,255))
                text20=Font.render("Back",1,(255,0,0))


                self.screen.blit(text12,(10,10))
                self.screen.blit(text13,(10,50))
                self.screen.blit(text14,(10,90))
                self.screen.blit(text15, (10,130))
                self.screen.blit(text16, (10, 170))
                self.screen.blit(text17, (20, 210))
                self.screen.blit(text18, (30, 250))
                self.screen.blit(text19, (60, 290))
                self.screen.blit(text20,(1050,600))

                if event.type == pygame.MOUSEBUTTONUP:
                    mx, my = pygame.mouse.get_pos()
                    if (mx >= 1050 and mx <= 1130 and my >= 595 and my <= 650):
                        self.page_index = 0







            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
