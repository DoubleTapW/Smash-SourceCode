class Enemy:
    def __init__( self , x , y , enemyVel , Ienemy ): 
        self.x = x
        self.y = y
        self.enemyVel = enemyVel
        self.Ienemy = Ienemy

    def movement(self , playerPosX , playerPosY):

        self.playerPosX = playerPosX
        self.playerPosY = playerPosY

        if self.x > self.playerPosX:
            self.x -= self.enemyVel
        
        if self.y > self.playerPosY:
            self.y -= self.enemyVel

        if self.x < self.playerPosX:
            self.x += self.enemyVel
        
        if self.y < self.playerPosY:
            self.y += self.enemyVel

    def draw_enemy(self , win ):
        win.blit( self.Ienemy , ( self.x , self.y ) )
 