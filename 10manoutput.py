from skw10mans import returnPost

validtags = """valid tags: 
- id:(number) - match id found on cevo, e.g. https://cevo.com/event/csgo-10man/match/XXX
- num:(number) - denotes game number, can be a string.
- lmn:(name) - last map name, e.g. de_dust2
- lml:(link) - last map link, e.g. 47zwzy/2nd_official_10_man_resuts/
- nmn:(name) - next map name, e.g. de_cbbl
- nml:(link) - next map link, e.g. 495kfj/official_10_man_4_results/
- file:(0/1) - whether or not to output to file (file will be called output.txt) (default:1)
- pr:(0/1) - whether or not to print to this screen when done. (default:0)
- rot:(link) - link to current map rotation, defaults to 4a6srf/rotation_2/

***Note when using links, the https://www.reddit.com/r/skw10mans/comments/ is always implied when pasting, \nSo only copy the last two segments (eg. 48zfjy/rotation_1_games_514/)"""

def postBuilder():
    rawinp = input("> tags: ")
    if (rawinp == "help" or rawinp=="?"):
        print(validtags)
    else:
        args = rawinp.split(" ")
        dict = {}
        
        reddit = "https://www.reddit.com/r/skw10mans/comments/"
        
        id = "0"
        num = "0"
        nmn = "NEXTMAP"
        nml = "nexmaplink"
        lml = "nextmaplink"
        lmn = "LASTMAP"
        file = 1
        pr = 0
        rot = "4a6srf/rotation_2/"
        
        try:
            for arg in args:
                arg = arg.split(":")
                dict[arg[0]] = arg[1]
        except(IndexError):
            print("Index Error, you might have put an item with a space or a colon in it. Don't do that.\nInstead of 'https://www.reddit.com/r/skw10mans/comments/48zfjy/rotation_1_games_514/' just put '48zfjy/rotation_1_games_514/'")
            pass
        
        #Spaghetti code because i want to restrict to specific tags, 
            #rather than just parsing anything
        if "id" in dict:
            id = dict["id"]
        if "num" in dict:
            num = dict["num"]
        if "nml" in dict:
            nml = dict["nml"]
        if "nmn" in dict:
            nmn = dict["nmn"]
        if "lml" in dict:
            lml = dict["lml"]
        if "lmn" in dict:
            lmn = dict["lmn"]
        if "rot" in dict:
            rot = dict["rot"]
        if "file" in dict:
            if dict["file"] == "0":
                file = 0
            print("output to file!")
        if "pr" in dict:
            if dict["pr"] == "1":
                pr = 1
        
        post = returnPost(id,num=num,nml=reddit+nml,nmn=nmn,lmn=lmn,lml=reddit+lml,rotlink=reddit+rot)
        if file:
            out = open('output.txt', 'w+')
            out.write(post)
            print("Wrote to file 'output.txt.' Use pr:1 if you want to print output here.")
        if pr:
            print(post)
    
    #except(IndexError):
    #    print("Input invalid: likely no input or no separation. \nUse ' ' to separate parameters, and ':' to set values to keys. (E.G. id:1000)")

if __name__ == "__main__":
    print("   Example line: \n   id:3000 num:10 lmn:de_dust2 file:0")
    print(validtags)
    print()
    print("Type 'help' or '?' for valid tags")
    while 1:
        postBuilder()