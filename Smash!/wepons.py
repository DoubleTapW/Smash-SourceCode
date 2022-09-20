from pygame import transform

class Wepons:
    def __init__(self , weponImg ):
        self.weponImg = weponImg

    def drawWepon(self , win , playerX , playerY ):
        win.blit( self.weponImg , ((playerX + 32 ) , (playerY + 18))) 
