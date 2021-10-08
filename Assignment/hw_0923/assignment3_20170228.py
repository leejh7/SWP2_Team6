import pickle

dbfilename = 'test3_4.dat'


def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb = pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while (True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
            scdb += [record]
        elif parse[0] == 'del':
            dellist = []
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        dellist.append(p)
                for p in dellist:
                    scdb.remove(p)
            except IndexError:
                print("input 'del name':")
        elif parse[0] == 'show':
            sortKey = 'Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'find':
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        print(p)
            except IndexError:
                print("Input 'find name':")
        elif parse[0] == 'inc':
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        p['Score'] = str(int(p['Score']) + int(parse[2]))
            except IndexError:
                print("Input 'inc name amount':")
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()

scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
