from src.solution import player
def test_player_initialization():    
    p = player("Alice")
    assert p.name == "Alice"
    assert p.level == 1
    assert p.health == p.INITIAL_HEALTH
    assert p.is_alive == True
def test_invalid_name():
    try:
        p = player(123)
    except ValueError as e:
        assert str(e) == "Name must be a string"
def test_take_damage():
    p = player("Bob")
    p.take_damage(200)
    assert p.health == 800
    assert p.is_alive == True
    p.take_damage(800)
    assert p.health == 0
    assert p.is_alive == False
def test_heal():    
    p = player("Charlie")
    p.take_damage(500)
    p.heal(300)
    assert p.health == 800
    assert p.is_alive == True   
    p.heal(300)
    assert p.health == p.INITIAL_HEALTH
    assert p.is_alive == True
def test_heal_dead_player():
    p = player("Dave")
    p.take_damage(1000)
    p.heal(500)
    assert p.health == 0
    assert p.is_alive == False     
def test_damage_dead_player():
    p=player("Arthur")
    p.take_damage(1000)
    p.take_damage(100)
    