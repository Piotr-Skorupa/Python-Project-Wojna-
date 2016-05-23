import random, pygame, sys, pygame.mixer
from pygame.locals import *
import os.path
from pygame.mixer import *


class kartygracza(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.score =0
        self.text = "Twoje karty: %4d" % self.score
        self.font = pygame.font.SysFont("Comic Sans MS",30)
        self.image = self.font.render(self.text,1,NIEBIESKI)
        self.rect = self.image.get_rect()
        self.rect.center = (100, 200)
    def update(self,lista):
        self.score= len(lista)
        self.text = "Twoje karty: %4d" % self.score
        self.image = self.font.render(self.text,1,NIEBIESKI)
        self.rect = self.image.get_rect()
        self.rect.center = (100, 200)

class kartykompa(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.score = 0
        self.text = "Karty komputera: %4d" % self.score
        self.font = pygame.font.SysFont("Comic Sans MS",30)
        self.image = self.font.render(self.text,1,NIEBIESKI)
        self.rect = self.image.get_rect()
        self.rect.center = (650, 200)
    def update(self,lista):
        self.score= len(lista)
        self.text = "Karty komputera: %4d" % self.score
        self.image = self.font.render(self.text,1,NIEBIESKI)
        self.rect = self.image.get_rect()
        self.rect.center = (650, 200)

class Button1(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.image = loadImage("newgame.png", True)
        self.rect = self.image.get_rect()
        self.rect.center = (200, 200)

    def kliknij(self):
        click = pygame.mouse.get_pressed()
        maus= pygame.mouse.get_pos()
        if 200+334 > maus[0] > 200 and 200+66 > maus[1] > 200:
            if click[0]==1:
                print "klinales"

class Button2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = loadImage("continue.png", True)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

class Button3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = loadImage("wyniki.png", True)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

class Button4(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = loadImage("wyjscie.png", True)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


def wygrana(list1, list2):
    if len(list1.cards)==0:
        font = pygame.font.Font(None, 36)
        screen.blit(font.render('Przegrales ! :( [Esc] - Zakoncz', True, (255,0,0)), (200, 200))
        pygame.display.flip()
    elif len(list2.cards)==0:
        font = pygame.font.Font(None, 36)
        screen.blit(font.render('Wygrales ! :) [Esc] - Zakoncz', True, (255,0,0)), (200, 200))
        pygame.display.flip()




# tworzymy klase zapisu ilosci zebranych kart
class Pointns(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.score = 0
        self.text = "Zebrane karty: %4d" % self.score
        self.font = pygame.font.SysFont("Comic Sans MS",30)
        self.image = self.font.render(self.text,1,NIEBIESKI)
        self.rect = self.image.get_rect()

    def update(self):
        self.score += 1
        self.text = "Zebrane karty: %4d" % self.score
        self.image = self.font.render(self.text,1,NIEBIESKI)
        self.rect = self.image.get_rect()

# tworzymy klase kart do gry
class Card(pygame.sprite.Sprite):
    """Karta do gry"""
    RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS = ["c","d","h","s"]
    def __init__(self,rank,suit,strange):

        pygame.sprite.Sprite.__init__(self)
        self.image = loadImage("2s.png", True)
        self.rank = rank
        self.suit = suit
        self.strange = strange
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def change_coordinates(self,x,y):
        self.rect.center = (x,y)

    def update(self):
        pass
    def __str__(self):
        rep = self.rank+self.suit+" sila: %(self.strange)d" %{"self.strange":self.strange}
        return rep

# tworzymy klase Hand ktora posluzy jako reka gracza oraz stol rozgrywki

class Hand(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.cards = []
    def tasuj(self):
        random.shuffle(self.cards)
    def add(self, card):
        self.cards.append(card)
    def oddaj(self, card, other):
        self.cards.remove(card)
        other.add(card)
    def rozdawanie(self,hands, zakres = 1):
        for znak in range(zakres):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.oddaj(top_card,hand)


# funkcja ladowania obrazkow
def loadImage(name, useColorKey=False):
    fullname = os.path.join("data",name)
    image = pygame.image.load(fullname)
    image = image.convert()
    if useColorKey is True:
        colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey,RLEACCEL)

    return image

# parametry programu (zmienne globalne)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)
WHITE = (255,255,255)
NIEBIESKI = (0, 0, 255)
RED = (255, 0, 0)
x=300
y=421
k=500



# inicjujemy pygame

pygame.init()



screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Wojna")
pygame.mixer.music.load("wojna.mp3")
pygame.mixer.music.play(-1, 0.0)

# towrzymy obiekty klasy Card

dwapik = Card(rank="2", suit="s", strange=2)
dwakier = Card(rank="2", suit="h", strange=2)
dwakaro = Card(rank="2", suit="d", strange=2)
dwatrefl = Card(rank="2", suit="c", strange=2)

trzypik = Card(rank="3", suit="s", strange=3)
trzykier = Card(rank="3", suit="h", strange=3)
trzykaro = Card(rank="3", suit="d", strange=3)
trzytrefl = Card(rank="3", suit="c", strange=3)

czterypik = Card(rank="4", suit="s", strange=4)
czterykier = Card(rank="4", suit="h", strange=4)
czterykaro = Card(rank="4", suit="d", strange=4)
czterytrefl = Card(rank="4", suit="c", strange=4)

piecpik = Card(rank="5", suit="s", strange=5)
pieckier = Card(rank="5", suit="h", strange=5)
pieckaro = Card(rank="5", suit="d", strange=5)
piectrefl = Card(rank="5", suit="c", strange=5)

szescpik = Card(rank="6", suit="s", strange=6)
szesckier = Card(rank="6", suit="h", strange=6)
szesckaro = Card(rank="6", suit="d", strange=6)
szesctrefl = Card(rank="6", suit="c", strange=6)

siedempik = Card(rank="7", suit="s", strange=7)
siedemkier = Card(rank="7", suit="h", strange=7)
siedemkaro = Card(rank="7", suit="d", strange=7)
siedemtrefl = Card(rank="7", suit="c", strange=7)

osiempik = Card(rank="8", suit="s", strange=8)
osiemkier = Card(rank="8", suit="h", strange=8)
osiemkaro = Card(rank="8", suit="d", strange=8)
osiemtrefl = Card(rank="8", suit="c", strange=8)

dziewiecpik = Card(rank="9", suit="s", strange=9)
dziewieckier = Card(rank="9", suit="h", strange=9)
dziewieckaro = Card(rank="9", suit="d", strange=9)
dziewiectrefl = Card(rank="9", suit="c", strange=9)

dziesiecpik = Card(rank="10", suit="s", strange=10)
dziesieckier = Card(rank="10", suit="h", strange=10)
dziesieckaro = Card(rank="10", suit="d", strange=10)
dziesiectrefl = Card(rank="10", suit="c", strange=10)

waletpik = Card(rank="J", suit="s", strange=11)
waletkier = Card(rank="J", suit="h", strange=11)
waletkaro = Card(rank="J", suit="d", strange=11)
walettrefl = Card(rank="J", suit="c", strange=11)

damapik = Card(rank="Q", suit="s", strange=12)
damakier = Card(rank="Q", suit="h", strange=12)
damakaro = Card(rank="Q", suit="d", strange=12)
damatrefl = Card(rank="Q", suit="c", strange=12)

krolpik = Card(rank="K", suit="s", strange=13)
krolkier = Card(rank="K", suit="h", strange=13)
krolkaro = Card(rank="K", suit="d", strange=13)
kroltrefl = Card(rank="K", suit="c", strange=13)

aspik = Card(rank="A", suit="s", strange=14)
askier = Card(rank="A", suit="h", strange=14)
askaro = Card(rank="A", suit="d", strange=14)
astrefl = Card(rank="A", suit="c", strange=14)

joker = Card(rank="JOKER", suit="", strange=15)
joker2 = Card(rank="JOKER", suit="", strange=15)

# pakujemy karty do tali
talia = Hand()
talia.cards=[dwapik, dwakaro, dwakier, dwatrefl, trzykaro, trzykier, trzypik, trzytrefl, czterykaro, czterykier, czterypik,
         czterytrefl, piectrefl, pieckaro, piecpik, pieckier, szesckaro, szesckier, szescpik, szesctrefl, siedemkaro,
         siedemkier, siedempik, siedemtrefl, osiemkaro, osiemkier, osiempik, osiemtrefl, dziewieckaro, dziewieckier,
         dziewiecpik, dziewiectrefl, dziesieckaro, dziesieckier, dziesiecpik, dziesiectrefl, waletkaro, waletkier,
         waletpik, walettrefl, damakaro, damakier, damapik, damatrefl, krolkaro, krolkier, krolpik, kroltrefl, askaro,
         askier, aspik, astrefl, joker, joker2]

# tasujemy karty

talia.tasuj()


gracz = Hand()
komp = Hand()
hands = [gracz, komp]
talia.rozdawanie(hands, zakres = 27)


# tworzymy stol do gry

stolik= Hand()

# nadajemy obiektom klasy Card obrazki oraz tworzymy tlo okna

background_image = loadImage("back.png")
screen.blit(background_image,(0,0))
dwapik = loadImage("2s.png",True)
dwakier.image = loadImage("2h.png",True)
dwatrefl.image = loadImage("2c.png",True)
dwakaro.image = loadImage("2d.png",True)

trzypik.image = loadImage("3s.png",True)
trzykier.image = loadImage("3h.png",True)
trzytrefl.image = loadImage("3c.png",True)
trzykaro.image = loadImage("3d.png",True)

czterypik.image = loadImage("4s.png",True)
czterykier.image = loadImage("4h.png",True)
czterytrefl.image = loadImage("4c.png",True)
czterykaro.image = loadImage("4d.png",True)

piecpik.image = loadImage("5s.png",True)
pieckier.image = loadImage("5h.png",True)
piectrefl.image = loadImage("5c.png",True)
pieckaro.image = loadImage("5d.png",True)

szescpik.image = loadImage("6s.png",True)
szesckier.image = loadImage("6h.png",True)
szesctrefl.image = loadImage("6c.png",True)
szesckaro.image = loadImage("6d.png",True)

siedempik.image = loadImage("7s.png",True)
siedemkier.image = loadImage("7h.png",True)
siedemtrefl.image = loadImage("7c.png",True)
siedemkaro.image = loadImage("7d.png",True)

osiempik.image = loadImage("8s.png",True)
osiemkier.image = loadImage("8h.png",True)
osiemtrefl.image = loadImage("8c.png",True)
osiemkaro.image = loadImage("8d.png",True)

dziewiecpik.image = loadImage("9s.png",True)
dziewieckier.image = loadImage("9h.png",True)
dziewiectrefl.image = loadImage("9c.png",True)
dziewieckaro.image = loadImage("9d.png",True)

dziesiecpik.image = loadImage("10s.png",True)
dziesieckier.image = loadImage("10h.png",True)
dziesiectrefl.image = loadImage("10c.png",True)
dziesieckaro.image = loadImage("10d.png",True)

waletpik.image = loadImage("js.png",True)
waletkier.image = loadImage("jh.png",True)
walettrefl.image = loadImage("jc.png",True)
waletkaro.image = loadImage("jd.png",True)

damapik.image = loadImage("ds.png",True)
damakier.image = loadImage("dh.png",True)
damatrefl.image = loadImage("dc.png",True)
damakaro.image = loadImage("dd.png",True)

krolpik.image = loadImage("ks.png",True)
krolkier.image = loadImage("kh.png",True)
kroltrefl.image = loadImage("kc.png",True)
krolkaro.image = loadImage("kd.png",True)

aspik.image = loadImage("as.png",True)
askier.image = loadImage("ah.png",True)
astrefl.image = loadImage("ac.png",True)
askaro.image = loadImage("ad.png",True)

joker.image = loadImage("joker.png",True)
joker2.image = loadImage("joker.png",True)

# tworzymy obrazki tali kart gracza i komputera

gracztyl = loadImage("tyl.png",True)
kompu = loadImage("tyl.png",True)
screen.blit(gracztyl,(10,321))
screen.blit(kompu,(600,321))
pygame.display.flip()

# tworzymy obiekt klasy Pointns , czyli licznik kart
wynik=Pointns()
k1 = kartygracza()
k2 = kartykompa()
kartSprite = pygame.sprite.RenderClear()
kart2Sprite = pygame.sprite.RenderClear()
k1.update(gracz.cards)
k2.update(komp.cards)
kartSprite.add(k1)
kart2Sprite.add(k2)
kartSprite.draw(screen)
kart2Sprite.draw(screen)
pygame.display.flip()
# tworzymy kontenery na Sprity
stolSprite = pygame.sprite.RenderClear()
stol2Sprite = pygame.sprite.RenderClear()
scoreSprite = pygame.sprite.RenderClear()
scoreSprite.add(wynik)
scoreSprite.draw(screen)
pygame.display.flip()
score = 0
running = True

# pora na glowna petle gry

while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if len(gracz.cards)==0 or len(komp.cards)==0:
                    wygrana(gracz,komp)
                else:
                    gracz.oddaj(gracz.cards[0],stolik)
                    komp.oddaj(komp.cards[0],stolik)
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                   running = False


            #else:
                #print event
        kartSprite.update(gracz.cards)
        kart2Sprite.update(komp.cards)
        kartSprite.clear(screen, background_image)
        kart2Sprite.clear(screen, background_image)
        kartSprite.draw(screen)
        kart2Sprite.draw(screen)
        pygame.display.flip()

        for namiar in range(len(gracz.cards)):
            gracz.cards[namiar].change_coordinates(x,y)

        for namiar in range(len(komp.cards)):
            komp.cards[namiar].change_coordinates(k,y)


        if not len(stolik.cards)==0:
            stolSprite.clear(screen, background_image)
            stol2Sprite.clear(screen, background_image)
            stolSprite.empty()
            stol2Sprite.empty()
            pygame.display.flip()
            stolSprite.add(stolik.cards[0])
            stol2Sprite.add(stolik.cards[1])
            stolSprite.draw(screen)
            pygame.display.flip()
            stol2Sprite.draw(screen)
            pygame.display.flip()            
            if stolik.cards[0].strange < stolik.cards[1].strange:
                stolik.oddaj(stolik.cards[0],komp)
                stolik.oddaj(stolik.cards[0],komp)
            elif stolik.cards[1].strange < stolik.cards[0].strange:
                stolik.oddaj(stolik.cards[0],gracz)
                stolik.oddaj(stolik.cards[0],gracz)
                score += 1
                scoreSprite.update()
                scoreSprite.clear(screen, background_image)
                scoreSprite.draw(screen)
                pygame.display.flip()
            else:
                print "wojna"
                    
                for a in range(0,3):
                    if len(gracz.cards)==0 or len(komp.cards)==0:
                        wygrana(gracz,komp)
                    else:
                        gracz.oddaj(gracz.cards[0],stolik)
                        komp.oddaj(komp.cards[0],stolik)
                if stolik.cards[-2].strange < stolik.cards[-1].strange:
                    stolik.oddaj(stolik.cards[0],komp)
                    stolik.oddaj(stolik.cards[0],komp)
                    stolik.oddaj(stolik.cards[0],komp)
                    stolik.oddaj(stolik.cards[0],komp)
                    stolik.oddaj(stolik.cards[0],komp)
                    stolik.oddaj(stolik.cards[0],komp)
                    print "-"
                elif stolik.cards[-1].strange < stolik.cards[-2].strange:
                    stolik.oddaj(stolik.cards[0],gracz)
                    stolik.oddaj(stolik.cards[0],gracz)
                    stolik.oddaj(stolik.cards[0],gracz)
                    stolik.oddaj(stolik.cards[0],gracz)
                    stolik.oddaj(stolik.cards[0],gracz)
                    stolik.oddaj(stolik.cards[0],gracz)
                    print "+"
                    score += 6
                    scoreSprite.update()
                    scoreSprite.update()
                    scoreSprite.update()
                    scoreSprite.update()
                    scoreSprite.update()
                    scoreSprite.clear(screen, background_image)
                    scoreSprite.draw(screen)
                    pygame.display.flip()
