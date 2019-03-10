from module1 import Game, Player

player1 = Player("Sherlock")
game1 = Game(["living room", "main room",
              "closet", "i", "kitchen", "bedroom"], player1.name, 3,
             "closet")
game1.start()
