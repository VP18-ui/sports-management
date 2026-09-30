class Player:
    def __init__(self,name,sport,age,score):
        self.name=name
        self.sport=sport
        self.age=age
        self.score=score
    def display(self):
        print("Name:",self.name)
        print("Sport:",self.sport)
        print("Age:",self.age)
        print("Score:",self.score)       
class SportsManagement:
    def __init__(self):
        self.players=[]
   #Adding player's details  
    def add_player(self):
        print("\n--- Add Player ---")
        name=input("Enter player name:")
        sport=input("Enter sport:")
        age=int(input("Enter age:"))
        score=int(input("Enter score:"))        
        player=Player(name,sport,age,score)
        self.players.append(player)
        print("Player added successfully")
    #displaying details 
    def view_players(self):
        print("\n--- All Players ---")
        if len(self.players)==0:
            print("No players found.")
        else:
            for player in self.players:
                player.display()
    #Searching player
    def search_player(self):
        print("\n--- Search Player ---")
        name = input("Enter player name:")
        for player in self.players:
            if player.name.lower()==name.lower():
                print("\nPlayer Found")
                player.display()
                return
        print("Player not found.")
    # Updatind score
    def update_score(self):
        print("\n--- Update Score ---")
        name = input("Enter player name:")
        for player in self.players:
            if player.name.lower()==name.lower():
                new_score=int(input("Enter new score:"))
                player.score=new_score
                print("Score updated successfully")
                return
        print("Player not found.")
    #display player with highest score
    def highest_scorer(self):
        print("\n--- Highest Scorer ---")
        if len(self.players)==0:
            print("No players found.")
            return
        highest=self.players[0]
        for player in self.players:
            if player.score > highest.score:
                highest=player
        highest.display()        
    #Removing player
    def delete_player(self):
        print("\n---Delete Player---")
        name = input("Enter player name:")
        for player in self.players:
            if player.name.lower()==name.lower():
                self.players.remove(player)
                print("Player deleted successfully")
                return
        print("Player not found.")
#sports management system 
sports=SportsManagement()
#showing menu 
while True:
    print("---VITYARTHI SPORTS MANAGEMENT---")
    print("1.Add Player")
    print("2.View Players")
    print("3.Search Player")
    print("4.Update Score")
    print("5.Highest Scorer")
    print("6.Delete Player")
    print("7.Exit")
    choice=input("\nEnter your choice:")
    if choice=="1":
        sports.add_player()
    elif choice=="2":
        sports.view_players()
    elif choice=="3":
        sports.search_player()
    elif choice=="4":
        sports.update_score()
    elif choice=="5":
        sports.highest_scorer()
    elif choice=="6":
        sports.delete_player()
    elif choice=="7":
        print("\nThank you for using VITYARTHI Scorecard Management")
        break
    else:
        print("\nInvalid choice")



