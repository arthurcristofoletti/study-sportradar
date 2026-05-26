#study case for preparing to the code interview
#this would be the code that will starts the rpg game
from src.solution import player
class combat_kata():
    def __init__(self):
        player1 = player("Player 1")
        player2 = player("Player 2")
        print(f"{player1.name} vs {player2.name}")
        while player1.is_alive and player2.is_alive:
            player1.take_damage(100)
            print(f"{player1.name} takes 100 damage, health is now {player1.health}")
            if not player1.is_alive:
                print(f"{player1.name} has been defeated!")
                break
            player2.take_damage(150)
            print(f"{player2.name} takes 150 damage, health is now {player2.health}")
            if not player2.is_alive:
                print(f"{player2.name} has been defeated!")
                break
if __name__ == "__main__":      
    print("Hello world!")
    combat_kata()