
class Player:
    def play(self):
        print("The player is playing cricket.")
class Batsman(Player):
    def play(self):
        print("The batsman is batting.")
class Bowler(Player):
    def play(self):
        print("The bowler is bow.")
Batsman=Batsman()
Bowler=Bowler()
Batsman.play()
Bowler.play()