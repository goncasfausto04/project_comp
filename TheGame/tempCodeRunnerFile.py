    def update(self,player):

        #determining direction (in radians)
        dx = player.rect.x - self.rect.x
        dy = player.rect.y - self.rect.y
        direction = math.atan2(dy,dx)

        #moving enemy to player
        self.rect.x += self.speed * math.cos(direction)
        self.rect.y += self.speed * math.sin(direction)


        
