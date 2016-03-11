from bs4 import BeautifulSoup
from urllib import request

def onlyAscii(s): 
    return str("".join(i for i in s if ord(i)>=32 and ord(i)<=127)).strip()
    
def onlyNumbers(s): 
    return str("".join(i for i in s if ((ord(i)>=48 and ord(i)<=57) or ord(i)==46))).strip()

class player:
    def __init__(self,name,kills,deaths,assists):
        self.name = name
        self.kills = kills
        self.deaths = deaths
        self.assists = assists

#i dont use this method anymore, but i have it here so i can import it if i need to for whatever reason
def buildLine(line,num=str(1),gamechart="",map="de_cbble",dbxlink="http://ihop.com",matchid="307483",date="12/31/1969",rotlink="http://reddit.com",lmn="de_dust2",lml="http://reddit.com",nmn="de_inferno",nml="http://reddit.com"):
    line = line.replace("$num",num)
    line = line.replace("$date",date)
    line = line.replace("$map",map)
    line = line.replace("$mtlink","https://cevo.com/event/csgo-10man/match/"+matchid);
    line = line.replace("$dbx",dbxlink)
    line = line.replace("$rotlink",rotlink)
    line = line.replace("$lastmapname",lmn)
    line = line.replace("$lastmaplink",lml)
    line = line.replace("$nextmapname",nmn)
    line = line.replace("$nextmaplink",nml)
    line = line.replace("$gamechart",gamechart)
    return line
 
def returnPost(matchid,num=str(1),gamechart="",map="de_cbble",dbxlink="http://ihop.com",date="12/31/1969",rotlink="https://www.reddit.com/r/skw10mans/comments/48zfjy/rotation_1_games_514/",lmn="de_dust2",lml="http://reddit.com",nmn="de_inferno",nml="http://reddit.com"):

    players1 = []
    players2 = []
    pbf = "base.txt" #post base file
    product = ""
    
    url = request.urlopen("http://cevo.com/event/csgo-10man/match/"+matchid)
    soup = BeautifulSoup(url.read(),"html.parser")
    
    #find all player data
    t  = soup.findAll("tr", {"data-roster":"away", "class":"t"})
    ct = soup.findAll("tr", {"data-roster":"away", "class":"ct"})
    
    #get date and time from html
    datesoup = soup.find_all("span",{"class":"scheduled-time"})
    for item in datesoup:
        date = item.text
    
    mapsoup = soup.find_all("div",{"class":"score-seperator"})
    for item in mapsoup:
        map = item.text
    
    #build team1
    for line in t:
        name    = onlyAscii(line.findAll("td")[0].text.replace("\n",""))
        kills   = onlyNumbers(line.findAll("td")[2].text)
        deaths  = onlyNumbers(line.findAll("td")[3].text)
        assists = onlyNumbers(line.findAll("td")[4].text)
        
        players1.append(player(name,kills,deaths,assists))
    
        #build team2
    for line in ct:
        name    = onlyAscii(line.findAll("td")[0].text.replace("\n",""))
        kills   = onlyNumbers(line.findAll("td")[2].text)
        deaths  = onlyNumbers(line.findAll("td")[3].text)
        assists = onlyNumbers(line.findAll("td")[4].text)
        
        players2.append(player(name,kills,deaths,assists))
    
        #open the base file
    pbf = open(pbf)
    gamechart = ""
    #build the gamechart based on this per-line template
    chart = "p0n | p0k/p0d/p0a | p1n | p1k/p1d/p1a"
    for i in range(5):
        chartline =     chart.replace("p0n",players1[i].name).replace("p1n",players2[i].name)
        chartline = chartline.replace("p0k",players1[i].kills).replace("p1k",players2[i].kills)
        chartline = chartline.replace("p0d",players1[i].deaths).replace("p1d",players2[i].deaths)
        chartline = chartline.replace("p0a",players1[i].assists).replace("p1a",players2[i].assists)
        gamechart = gamechart+chartline+"\n"
    
    for line in pbf:
        line = line.replace("$num",num)
        line = line.replace("$date",date)
        line = line.replace("$map",map)
        line = line.replace("$mtlink","https://cevo.com/event/csgo-10man/match/"+matchid);
        line = line.replace("$dbx",dbxlink)
        line = line.replace("$rotlink",rotlink)
        line = line.replace("$lastmapname",lmn)
        line = line.replace("$lastmaplink",lml)
        line = line.replace("$nextmapname",nmn)
        line = line.replace("$nextmaplink",nml)
        line = line.replace("$gamechart",gamechart)
        product = product+buildLine(line,gamechart=gamechart)
        
    return product

if __name__ == "__main__":
    print(returnPost("307483"))
    input("Run without error")

#a lot of code was stolen from onii-chan's web page/leaderboard system (loganford.net/skw10mans), half because i couldnt understand it, half because it was easier to rip than rewrite. 