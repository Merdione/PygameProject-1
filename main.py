import pygame
import random
pygame.init()
height = 720
width = 720
playerH = 15
playerW = 15
i = 0

running = True
speed = 0.5

screen = pygame.display.set_mode((height,width))
class player():
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(self.x,self.y,playerH,playerW)
    def update(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,playerH,playerW))
        self.rect = pygame.Rect(self.x,self.y,playerH,playerW)
    def right(self):
        self.x += speed    
    def left(self):
        self.x -= speed

    def down(self):
        self.y += speed    

    def up(self):
        self.y -= speed   



class cherry():
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(self.x,self.y,50,50)
    def update(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,50,50))
        self.rect = pygame.Rect(self.x,self.y,50,50)
      
    def randomP(self):
     self.x = random.randint(50,670) 
     self.y = random.randint(50,670) 


class strawberry():
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(self.x,self.y,55,55)
    def update(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,55,55))
        self.rect = pygame.Rect(self.x,self.y,55,55)
    def randomP(self):
     self.x = random.randint(50,670) 
     self.y = random.randint(50,670) 
class rock():
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(self.x,self.y,50,50)
    def update(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,50,50))
        self.rect = pygame.Rect(self.x,self.y,50,50)
    def randomP(self):  
       self.x = random.randint(50,670)          
       self.y = random.randint(50,670)       
  
  
         

player = player(10,10,(0,0,0))
cherry = cherry(100,200,(255,0,0))
strawberry =  strawberry(175,300,(255,0,255))
rock = rock(100,300,(0,255,0))


while running:
 #Loop

 if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
     player.left()
 elif pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
     player.right()
 elif pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_DOWN]:
     player.down()
 elif pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:  
     player.up()
 if player.rect.colliderect(cherry.rect):
     playerH += 2
     playerW += 2
     cherry.randomP()

     if not(player.x > rock.x and player.x + playerW > rock.x + 50 or player.x < rock.x and player.x + playerW < rock.x + 50) or not(player.y > rock.y and player.y + playerH > rock.y + 50 or player.y < rock.y and player.y + playerH < rock.y + 50):
      while  not(player.x > rock.x and player.x + playerW > rock.x + 50 or player.x < rock.x and player.x + playerW < rock.x + 50) or not(player.y > rock.y and player.y + playerH > rock.y + 50 or player.y < rock.y and player.y + playerH < rock.y + 50):
        rock.randomP()
     else:     
      rock.randomP()
 elif player.rect.colliderect(strawberry.rect):
     playerH += 3
     playerW += 3
     strawberry.randomP()
     if  not(player.x > rock.x and player.x + playerW > rock.x + 50 or player.x < rock.x and player.x + playerW < rock.x + 50) or not(player.y > rock.y and player.y + playerH > rock.y + 50 or player.y < rock.y and player.y + playerH < rock.y + 50):
      while  not(player.x > rock.x and player.x + playerW > rock.x + 50 or player.x < rock.x and player.x + playerW < rock.x + 50) or not(player.y > rock.y and player.y + playerH > rock.y + 50 or player.y < rock.y and player.y + playerH < rock.y + 50):
        rock.randomP()
     else:     
        rock.randomP()

 elif player.rect.colliderect(rock.rect):
     playerH -= playerH / 4
     playerW -= playerW / 4
     if not(player.x > rock.x and player.x + playerW > rock.x + 50 or player.x < rock.x and player.x + playerW < rock.x + 50) or not(player.y > rock.y and player.y + playerH > rock.y + 50 or player.y < rock.y and player.y + playerH < rock.y + 50):
      while  not(player.x > rock.x and player.x + playerW > rock.x + 50 or player.x < rock.x and player.x + playerW < rock.x + 50) or not(player.y > rock.y and player.y + playerH > rock.y + 50 or player.y < rock.y and player.y + playerH < rock.y + 50):
        rock.randomP()
     else:     
      rock.randomP() 
    
 if playerH <= 10:
     running = False   


     





 #Exit the game
 for event in pygame.event.get(): 
   if event.type==pygame.QUIT: 
       running=False



 screen.fill((240,230,140)) 
 rock.update(screen)
 cherry.update(screen)    
 strawberry.update(screen)
 player.update(screen)     
 pygame.display.update()
   
