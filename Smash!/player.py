class Player:
    def __init__(self , playerAlive , playerBase , playerEyes):
        self.alive = playerAlive
        self.playerBase = playerBase
        self.playerEyes = playerEyes

    def playerDraw(self , win , x , y ):
        if self.alive:
            win.blit( self.playerBase , (x , y))  

        try:
            win.blit( self.playerEyes , (x , y)) 
        except:
            pass
