class player:
    INITIAL_HEALTH = 1000
    def __init__( self, name:str):
        try:
            self.name = name
        except:
                raise ValueError("Name must be a string")
        self.level = 1
        self.health = self.INITIAL_HEALTH
        self.is_alive = True
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False
    def heal(self, amount):
        if self.is_alive:
            self.health += amount
            if self.health > self.INITIAL_HEALTH:
                self.health = self.INITIAL_HEALTH   
