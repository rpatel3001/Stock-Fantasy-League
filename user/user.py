from preferences import *

class User:
    highestUID = 0
    def createLeague(self,leagueName, startBalance,numberOfDays,restrictions):
        # add constructor for create League
        return
        # League(leagueName,startBalance,numberOfDays,restrictions)
    def joinLeague(self, leagueName,startBalance,numberOfDays):
        #add code to join league
        return

    def __init__(self,UID,userPreferences,lastUsedPlayer,playersArray,totalPoints,mostRecentAcheievements,playerAchievements):
        self.uid = UID
        self.userPreferences = Preferences()
        self.layers_array = None
        self.total_points = None
        self.mostRecentAchievements = None
        self.player_Achievements = None
