import random

class Backround_Cosmatics():
    def __init__( self , bg , screenW , screenH , Iflower , Istone , Igrass1 , Igrass2 ):
        self.bg = bg
        self.Random_bg = random.randint(1, 3)
        self.grass_type = random.randint(1 , 2) 
        self.x = random.randint(0, screenW)
        self.y = random.randint(0, screenH)   

        if self.Random_bg == 1:
            self.image = Iflower
        elif self.Random_bg == 2:
            self.image = Istone
        elif self.grass_type == 1:
            self.image = Igrass1
        else:
            self.image = Igrass2

    def DrawCosmatics(self, win):
        win.blit(self.image, (self.x, self.y))
        self.bg += 1