# -*- coding: utf-8 -*-
from tkinter import *
import time, pygame

class Sprite :
    # 생성자		
    def __init__(self, image, x, y):
        self.img = image	# 스프라이트가 가지고 있는 이미지
        self.x = x		# 현재 위치의 x좌표
        self.y = y		# 현재 위치의 y좌표
        self.dx = 0		# 단위시간에 움직이는 x방향 거리
        self.dy = 0      # 단위시간에 움직이는 y방향 거리
                
    # 스프라이트의 가로 길이 반환		
    def getWidth(self) :
        return self.img.width()

    # 스프라이트의 세로 길이 반환		
    def  getHeight(self) :
        return self.img.height()

    # 스프라이트를 화면에 그리기
    def draw(self, g) :
        g.create_image(self.x, self.y, anchor=NW, image=self.img)

    # 스프라이트를 움직이는 메소드
    def move(self) :
        self.x += self.dx # x축 누적
        self.y += self.dy # y축 누적

    # dx를 설정하는 설정자 메소드 
    def  setDx(self, dx) :
        self.dx = dx

    # dy를 설정하는 설정자 메소드 
    def  setDy(self, dy) :
        self.dy = dy

    # dx를 반환하는 접근자 메소드 
    def  getDx(self) :
        return self.dx

    # dy를 반환하는 접근자 메소드 
    def  getDy(self) :
        return self.dy

    # x를 반환하는 접근자 메소드 
    def  getX(self) :
        return self.x

    # y를 반환하는 접근자 메소드 
    def  getY(self) :
        return self.y

    # 다른 스프라이트와의 충돌 여부를 계산한다. 충돌이면 true를 반환한다.
    # 3장의 Lab 문제를 참조한다. 
    def  checkCollision(self, other) :
        p1x = self.x
        p1y = self.y
        p2x = self.x+self.getWidth()
        p2y = self.y+self.getHeight()
        p3x = other.x
        p3y = other.y
        p4x = other.x+other.getWidth()
        p4y = other.y+other.getHeight()

        overlapped = not( p4x < p2x or
            p3x > p2x or
            p2y < p3y or
            p1y > p4y)
        return overlapped

    # 충돌을 처리한다. 현재는 아무 일도 하지 않는다. 자식 클래스에서 오버라이드된다. 
    def  handleCollision(self, other) :
        pass

# 우리의 우주선을 나타내는 클래스
class StarShipSprite(Sprite):
    def __init__(self, game, image, x, y):
        super().__init__(image, x, y)
        self.game = game
        self.dx = 0
        self.dy = 100 # 윈도우 화면에서 우주선 초기 위치 (수정함)

    # 우주선을 움직인다. 만약 윈도우의 경계를 넘으려고 하면 움직이지 않는다.  
    def move(self):
        if ((self.dx < 0) and (self.x < 10)) : # 왼쪽으로 가는데 x좌표가 10보다 작으면
            return
        if ((self.dx > 0) and (self.x > 725)) : # 오른쪽으로 가는데 x좌표가 725보다 크면
            return
        if ((self.dy < 0) and (self.y < 50)) : # 위쪽으로 가는데 y좌표가 50보다 작으면 (추가함))
            return
        if ((self.dy > 0) and (self.y > 650)) : # 아래쪽으로 가는데 좌y표가 650보다 크면 (추가함)
            return
        super().move()
        self.dx = 0
        self.dy = 0 # 방향키 1회 클릭에 1회만 작동시키기 위한 코드 (수정함)

    # 충돌을 처리한다. 외계인 우주선과 충돌하면 게임이 종료된다. 
    def handleCollision(self, other) :
        if  type(other) is AlienSprite :
            self.game.endGame()

# 외계인 우주선을 나타내는 클래스
class AlienSprite(Sprite):
    def __init__(self, game, image, x, y):
        super().__init__(image, x, y)
        self.game = game
        self.dx = -5		# x 방향으로만 움직임, 속도 조절 (수정함)

    # 외계인 우주선을 움직이는 메소드 
    # 윈도우에 경계에 도달하면 한칸 아래로 이동한다. 
    def move(self):
        if (((self.dx < 0) and (self.x < 10)) or ((self.dx > 0) and (self.x > 750))) : # 윈도우 양쪽 끝에 도달하면
            self.dx = -self.dx # 방향 전환
            self.y += 70 # y축으로 70만큼 내려감 (수정함)
            if (self.y > 700) :	
                game.endGame()
        super().move()

# 포탄을 나타내는 클래스
class ShotSprite(Sprite):
    def __init__(self, game, image, x, y):
        super().__init__(image, x, y)
        self.game = game
        self.dy = -20 # 포탄 속도

    # 화면을 벗어나면 객체를 리스트에서 삭제한다. 
    def move(self):
        super().move()
        if (self.y < -100) :
            self.game.removeSprite(self)

    # 충돌을 처리한다. 포탄과 외계인 우주선 객체를 모두 리스트에서 삭제한다. 
    def handleCollision(self, other) :
        if  type(other) is AlienSprite :
            self.game.removeSprite(self)
            self.game.removeSprite(other)
            pygame.mixer.init()
            sound_boom = pygame.mixer.Sound('boom.wav') 
            sound_boom.play() # 충돌했을 떄 효과음 (추가함)
        
# 게임을 나타내는 클래스
class GalagaGame():

    # 왼쪽 화살표 키 이벤트를 처리하는 함수
    def keyLeft(self, event) :
        self.starship.setDx(-10) # 한번 클릭시 -10
        return

    # 오른쪽 화살표 키 이벤트를 처리하는 함수
    def keyRight(self, event) :
        self.starship.setDx(+10) # 한번 클릭시 +10
        return

    def keyUp(self, event) :
        self.starship.setDy(-10) # 한번 클릭시 -10
        return

    def keyDown(self, event) :
        self.starship.setDy(+10) # 한번 클릭시 +10
        return

    # 스페이스 키 이벤트를 처리하는 함수
    def keySpace(self, event) :
        self.fire()
        return

    # 게임에 필요한 스프라이트를 생성하는 메소드
    # 왼쪽, 오른쪽을 구분하여 양쪽에서 외계인 우주선이 등장하도록 함
    def  initSprites_L(self) : # 왼쪽
        self.starship = StarShipSprite(self, self.shipImage, 370, 550)
        self.sprites.append(self.starship)
        for y in range(0, 1): # 한 층
            for x in range(0, 8): # 층마다 8개
                alien = AlienSprite(self, self.alienImage, -100 + (-x * 130), -30 + y * 30) # 왼쪽에서 처음 등장하는 위치, 간격 (수정함)
                self.sprites.append(alien)

    def  initSprites_R(self) : # 오른쪽
        for y in range(0, 1): # 한 층
            for x in range(0, 8): # 층마다 8개
                alien = AlienSprite(self, self.alienImage, 900 + (x * 130), 40 + y * 30) # 오른쪽에서 처음 등장하는 위치, 간격 (수정함)
                self.sprites.append(alien)

    # 생성자 메소드
    def __init__(self, master):
        self.master = master
        self.sprites = []
        self.canvas = Canvas(master, width=800, height=1000) # 캔버스 크기 (수정함)
        self.canvas.pack()
        self.shotImage = PhotoImage(file="fire.png") # 포탄을 나타내는 이미지
        self.shipImage = PhotoImage(file="starship.png") # 우주선을 나타내는 이미지
        self.alienImage = PhotoImage(file="alien.png") # 외계인 우주선을 나타내는 이미지
        self.running = True
        self.initSprites_L() # 왼쪽에서 등장하는 외계인 우주선
        self.initSprites_R() # 오른쪽에서 등장하는 외계인 우주선
        master.bind("<Left>",  self.keyLeft) # 왼쪽 방향키
        master.bind("<Right>", self.keyRight) # 오른쪽 방향키
        master.bind("<Up>", self.keyUp) # 위쪽 방향키
        master.bind("<Down>", self.keyDown) # 아래쪽 방향키
        master.bind("<space>", self.keySpace) # 스페이스키
        
    # 게임을 시작하는 메소드 
    def startGame(self) :
        self.sprites.clear()
        initSprites_L()
        initSprites_R()

    # 게임을 종료하는 메소드
    # 게임 종료시 종료를 알려주는 윈도우 창 띄우기
    def endGame(self) :
        pygame.init()
        screen_width = 640 # 윈도우 창 너비
        screen_height = 480 # 윈도우 창 높이
        display_surface = pygame.display.set_mode((screen_width, screen_height)) # 윈도우 창 띄우기
        pygame.display.set_caption("Game Over") # 윈도우 창 이름
        self.running = False
        pass
    
    # 스프라이트를 리시트에서 삭제한다. 
    def removeSprite(self, sprite) :
        if( sprite in self.sprites):
            self.sprites.remove(sprite)
            del sprite

    # 포탄을 발사하는 메소드 
    def fire(self) :
        shot = ShotSprite(self, self.shotImage, self.starship.getX() + 10,	self.starship.getY() - 30) # 우주선의 가운데에서 포탄 발사
        self.sprites.append(shot)

    # 화면을 그리는 메소드 
    def paint(self, g) :
        self.canvas.delete(ALL)
        self.canvas.create_rectangle(0, 0, 800, 1000, fill="black")
        for sprite in self.sprites:
            sprite.draw(self.canvas)

    # 게임 루프
    def  gameLoop(self) :
        for  sprite in self.sprites:
            sprite.move()

        # 스프라이트 리스트 안의 객체끼리의 충돌을 검사한다. 
        for  me in self.sprites: 
            for  other in self.sprites :
                if me != other:
                    if (me.checkCollision(other)) :
                        me.handleCollision(other)
                        other.handleCollision(me)
        self.paint(self.canvas)
        if( self.running ):
            self.master.after(10, self.gameLoop)  

root = Tk()
root.title("Galaga Game") # 윈도우 이름 설정 (추가함)
g = GalagaGame(root)

# 배경음악을 재생하는 코드
pygame.mixer.init()
sound_bg = pygame.mixer.Sound('background.wav')
sound_bg.play()

root.after(10, g.gameLoop())
root.mainloop()
