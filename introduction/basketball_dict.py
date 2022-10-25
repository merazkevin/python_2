# Assignment
# Paul is a fantasy basketball league manager, but also a programmer! 
# He is trying to organize fantasy teams of players (that can be from 
# any of the real teams) for his league website. There is already a web
# service that collects the line-up data from friends in batches.

# So far, he has been able to get a single list of dictionaries at a time
# from the API, and would like to put each team into a list of Player object 
# instances, so that he can use methods related to players.

# The lists look something like this:



class Player:
    all_team=[]
    def __init__(self,data):
        self.name = data['name']
        self.age = data['age']
        self.position = data['position']
        self.team = data['team']
        Player.all_team.append(data)

    @classmethod
    def get_team(cls):
        for key in Player.all_team:
            print(f"{key['name']}, {key['position']}".upper())
        return key

kevin =Player(data={
	"name": "Kevin Durant", 
	"age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
})
# print(kevin.name)

jason =Player(data={
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
})
# print(jason.name)

kyrie =Player(data={
    "name": "Kyrie Irving", 
    "age":32,
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
})
# print(kyrie.name)

# print(Player.all_players[0]['name'])
Player.get_team()