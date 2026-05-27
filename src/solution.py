class player:
    INITIAL_HEALTH = 1000
    def __init__( self, name:str) -> None:
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not name.strip():
            raise ValueError("Name cannot be empty")
        self.name : str = name
        self.level : int = 1
        self._health : int = self.INITIAL_HEALTH
        self._is_alive : bool = True

    @property
    def health(self) -> int:
        return self._health
    
    @property
    def is_alive(self) -> bool: 
        return self._is_alive
    
    def kill(self) -> None:
         if not self._is_alive:   
              return
         self._health = 0
         self._is_alive = False

    def take_damage(self, damage: int) -> None:
        if not isinstance(damage, (int, float)):
            raise TypeErrorError("Damage must be a number")
        if damage < 0:  
            raise ValueError("Damage cannot be negative")
        if self._is_alive:
            return
        self._health = max(self._health - damage, 0)
        if self._health == 0:
            self.kill()


    def heal(self, amount: int) -> None:
        if not isinstance(amount, (int, float)):
            raise TypeError("Heal amount must be a number")
        if amount < 0:
            raise ValueError("Heal amount cannot be negative")
        if not self._is_alive:
            raise ValueError("Cannot heal a dead player")
        self._health = min(self._health + amount, self.INITIAL_HEALTH)


             
