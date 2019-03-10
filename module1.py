class Game():
    def __init__(self, rooms, player, set_attempts, desired_room):
        self.data_action = []
        self.rooms = rooms
        self.player = player
        self.desired_room = desired_room
        self.set_attempts = set_attempts
        self.real_attempts = 0

    def start(self):
        print("Hello, "+str(self.player)+"! Where the key of cellar?:")
        print(self.rooms)
        print("You have "+str(self.set_attempts)+" attempts")
        while self.real_attempts < self.set_attempts:
            action = input("Сhoose an action: move or search (or quit)")
            if action == "move":
                room = input("Choose a room: ")
                if room in self.rooms or room == self.desired_room:
                    print("You moved in"+str(room))
                    self.data_action.append("moved in_"+str(room))
                else:
                    print("error")
            elif action == "search" and self.data_action:
                room = (self.data_action[-1])[9:]
                if room in self.rooms:
                    self.data_action.append("search in "+str(room))
                    self.real_attempts += 1
                    print("key not found, you have "+
                          str(self.set_attempts-self.real_attempts)+
                          " more attempts")
                elif room == self.desired_room:
                    print("You found the key. Game over. You won.")
                    break
                else:
                    print("You must move first.")
            elif action == "quit":
                break
            else:
                print("error")
        else:
            print("You lose. Game over.")

class Player():
    def __init__(self, player_name):
        self.player_name = player_name

    @property
    def name(self):
        return self.player_name
