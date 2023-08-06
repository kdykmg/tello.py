import pygame

class keyborad:
    def __init__(self):
        pygame.init()
        win=pygame.display.set_mode((400,400))
        
    
    def getKey(self,keyname):
        ans=False
        for event in pygame.event.get():pass
        keyInput=pygame.key.get_pressed()
        mykey=getattr(pygame,'K_{}'.format(keyname))
        print('K_{}'.format(keyname))
        if keyInput[mykey]:
            ans = True
        pygame.display.update() 
        return ans
  
  
    def getKeyInput(self):
        a,b,c,d=0,0,0,0
        e="a"
        speed=50
        
        if self.getKey("a"):
            a=-speed
        elif self.getKey("d"):
            a=speed 
            
        if self.getKey("w"):
            b=speed
        elif self.getKey("s"):
            b=-speed    
            
        if self.getKey("8"):
            c=speed
        elif self.getKey("5"):
            c=-speed
            
        if self.getKey("4"):
            d=-speed
        elif self.getKey("6"):
            d=speed 
        
        if self.getKey("z"):
            e="takeoff"
        elif self.getKey("x"):
            e="land"          
        return [a,b,c,d,e]