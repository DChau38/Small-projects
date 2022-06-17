# @ Goal: Assemble a mid lane champion picker thing with sieve options written below
# type = ad, ap, hybrid
# playable = early, mid, late, normal (refers to when useful not biggest spike or ideal scenario: case in point, galio and viegar = normal. Viktor is late cuz no cage like veigar. But Ahri is early cuz she stops being useful late game cuz single target cc and damage basically)

# @ Title: PickYourChampion:Mid
# @ Legal: PickYourChampion:Mid was created under Riot Games' "Legal Jibber Jabber" policy using assets owned by Riot Games.  Riot Games does not endorse or sponsor this project.

# class Champion: defines the champion constructor
class Champion:
    def __init__(self, name, type, playable):
        self.name = name
        self.type = type
        self.playable = playable
    def printType(self):
        print(self.type)
    def printPlayable(self):
        print(self.playable) 
# Definer: makes a list of champions with predefined properties: all is called ob, name is first property
def ChampsAssembler(): 
    listOfChampions = []
    ob = Champion("Ahri", "ap","early")
    listOfChampions.append(ob)
    ob = Champion("Akali", "ap","normal")
    listOfChampions.append(ob)
    ob = Champion("Anivia", "ap","normal")
    listOfChampions.append(ob)
    ob = Champion("Annie", "ap","normal")
    listOfChampions.append(ob)
    ob = Champion("AoShin", "ap","normal")
    listOfChampions.append(ob)
    ob = Champion("Azir", "ap","normal")
    listOfChampions.append(ob)
    ob = Champion("Brand", "ap","normal")
    listOfChampions.append(ob)
    ob = Champion("Cassiopeia", "ap","mid")
    listOfChampions.append(ob)
    ob = Champion("ChoGath", "ap","normal")
    listOfChampions.append(ob)
    ob = Champion("Corki", "hybrid","mid")
    listOfChampions.append(ob)
    ob = Champion("Ekko", "ap","mid")
    listOfChampions.append(ob)
    ob = Champion("Galio", "ap","mid")
    listOfChampions.append(ob)
    ob = Champion("Gangplank", "ad","mid")
    listOfChampions.append(ob)
    ob = Champion("Gragas", "ap","mid")
    listOfChampions.append(ob)
    ob = Champion("Heimerdinger", "ap","normal")
    listOfChampions.append(ob)
    ob = Champion("Irelia", "ad","mid")
    listOfChampions.append(ob)
    ob = Champion("Jayce", "ad","mid")
    listOfChampions.append(ob)
    ob = Champion("Karma", "ap","normal")
    listOfChampions.append(ob)
    ob = Champion("Karthus", "ap","normal")
    listOfChampions.append(ob)
    ob = Champion("Kassadin", "ap","mid")
    listOfChampions.append(ob)
    ob = Champion("Katarina", "hybrid","mid")
    listOfChampions.append(ob)
    ob = Champion("Kayle", "hybrid","mid")
    listOfChampions.append(ob)
    ob = Champion("LeBlanc", "ap","mid")
    listOfChampions.append(ob)
    ob = Champion("Lissandra", "ap","normal")
    listOfChampions.append(ob)
    ob = Champion("Lux", "ap","normal")
    listOfChampions.append(ob)
    ob = Champion("APMalphite", "ap","normal")
    listOfChampions.append(ob)
    ob = Champion("Malzahar", "ap","mid")
    listOfChampions.append(ob)
    ob = Champion("Neeko", "ap","mid")
    listOfChampions.append(ob)
    ob = Champion("Oriana", "ap","normal")
    listOfChampions.append(ob)
    ob = Champion("Pantheon", "ad","early")
    listOfChampions.append(ob)
    ob = Champion("Qiyana", "ad","mid")
    listOfChampions.append(ob)
    ob = Champion("Rumble", "ap","mid")
    listOfChampions.append(ob)
    ob = Champion("Ryze", "ap","meme")
    listOfChampions.append(ob)
    ob = Champion("Seraphine", "ap","normal")
    listOfChampions.append(ob)
    ob = Champion("Singed", "ap","normal")
    listOfChampions.append(ob)
    ob = Champion("SPLITSion", "ad","mid")
    listOfChampions.append(ob)
    ob = Champion("Sona", "ap","normal")
    listOfChampions.append(ob)
    ob = Champion("Soraka", "ap","normal")
    listOfChampions.append(ob)
    ob = Champion("Swain", "ap","mid")
    listOfChampions.append(ob)
    ob = Champion("Sylas", "ap","normal")
    listOfChampions.append(ob)
    ob = Champion("Syndra", "ap","normal")
    listOfChampions.append(ob)
    ob = Champion("Tayilah", "ap","normal")
    listOfChampions.append(ob)
    ob = Champion("Talon", "ad","mid")
    listOfChampions.append(ob)
    ob = Champion("Tristana", "ad","normal")
    listOfChampions.append(ob)
    ob = Champion("Tryndamere", "ad","normal")
    listOfChampions.append(ob)
    ob = Champion("TF", "ap","normal")
    listOfChampions.append(ob)
    ob = Champion("Veigar", "ap","normal")
    ob = Champion("VelKoz", "ap","normal")
    listOfChampions.append(ob)
    ob = Champion("Viktor", "ap","late")
    listOfChampions.append(ob)
    ob = Champion("Vladimir", "ap","late")
    listOfChampions.append(ob)
    ob = Champion("Xerath", "ap","normal")
    listOfChampions.append(ob)
    ob = Champion("Yasuo", "ad","normal")
    listOfChampions.append(ob)
    ob = Champion("Yone", "ad","normal")
    listOfChampions.append(ob)
    ob = Champion("Zed", "ad","normal")
    listOfChampions.append(ob)
    ob = Champion("Ziggs", "ap","mid")
    listOfChampions.append(ob)
    ob = Champion("Zilean", "ap","normal")
    listOfChampions.append(ob)
    ob = Champion("Zoe", "ap","normal")
    listOfChampions.append(ob)
    ob = Champion("Zyra", "ap","normal") 
    return listOfChampions
# userInputAll : asks user for input and returns the sieve
def userInputAll():
    flag = 0
    userInput = input("Do you want to sieve them by type of damage (type damage) or when they come online (type playable)")
    if userInput == "damage":
        flag = 1
        userInputDamageType = input("What type of damage? Options include : ad, ap, hybrid")
    elif userInput == "playable":
        flag = 2
        userInputPlayableType = input("When do you want to come online? Options include, early, mid, late, normal")
    else:
        print("... Did you actually type what's written there")
    if flag == 1:
        return userInputDamageType
    if flag == 2:
        return userInputPlayableType
# usingSieve: takes the given sieve and returns the champion list that fits the requirements
def usingSieve(sieve):
    listOfSievedChampionsTEMP = []
    print("\nThe following champions fit your requirements:\n")
    print("//////////////////////////////////////")
    if sieve == "ad":
        for champ in listOfChampions:
            if champ.type == "ad":
                listOfSievedChampionsTEMP.append(champ)
    if sieve == "ap":
        for champ in listOfChampions:
            if champ.type == "ap":
                listOfSievedChampionsTEMP.append(champ)
    if sieve == "hybrid":
        for champ in listOfChampions:
            if champ.type == "hybrid":
                listOfSievedChampionsTEMP.append(champ)
    if sieve == "early":
        for champ in listOfChampions:
            if champ.playable == "early":
                listOfSievedChampionsTEMP.append(champ)
    if sieve == "mid":
        for champ in listOfChampions:
            if champ.playable == "mid":
                listOfSievedChampionsTEMP.append(champ)
    if sieve == "late":
        for champ in listOfChampions:
            if champ.playable == "late":
                listOfSievedChampionsTEMP.append(champ)
    if sieve == "normal":
        for champ in listOfChampions:
            if champ.playable == "normal":
                listOfSievedChampionsTEMP.append(champ)
    return listOfSievedChampionsTEMP
# Everything down here is essentially the main function: This part is running for the first time
listOfChampions = ChampsAssembler()
sieve = userInputAll()
listOfSievedChampions = usingSieve(sieve)
for champ in listOfSievedChampions:
    print(champ.name)
# running multiple requirements / multiple times
yesNo = "empty"
while yesNo != "no":
    yesNo = input("Do you have any more requirements")
    listOfChampions = listOfSievedChampions
    sieve = userInputAll()
    listOfSievedChampions = usingSieve(sieve)
    for champ in listOfSievedChampions:
        print(champ.name)
