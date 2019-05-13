class Player:
    def __init__(self, gold_coins = 0, health_points = 10, lives = 5):
        self.gold_coins = gold_coins
        self.health_points = health_points
        self.lives = lives
    
    def __str__(self):
        return "Player has {} lives left.".format(self.lives)
#Your class should have an instance method called level_up that increases lives by one.
    def level_up(self):
        self.lives += 1
        return "Player has {} lives.".format(self.lives)
#Your class should have an instance method called collect_treasure that increases gold_coins by one. If gold_coins is a multiple of ten (eg, 10, 20, 30, and so on) then the collect_treasure method should run the level_up method.
    def collect_treasure(self):
        self.gold_coins +=1
        if self.gold_coins % 10 == 0:
            self.level_up()
        return "Player has {} gold coins.".format(self.gold_coins)
#Your class should have an instance method called do_battle that accepts one damage argument and subtracts it from the player's health_points. If health_points falls below one, subtract one from lives and reset health_points to ten. If you have run out of lives, this method should run another method called restart (see below).
    def do_battle(self, damage):
        self.health_points -= damage
        if self.health_points < 1:
            self.lives -= 1 
            self.health_points = 10
            if self.lives <= 0:
                self.restart()
        return "Player has {} lives and {} health points.".format(self.lives, self.health_points)
#The restart instance method should set all attributes back to their starting values (5, 0, and 10).
    def restart(self):
        self.gold_coins = 0
        self.health_points = 10
        self.lives = 5

player1 = Player()
player2 = Player(5, 30, 2)

print(player1.do_battle(9))
print(player2.do_battle(19))