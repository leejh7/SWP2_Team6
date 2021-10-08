import pickle

dbfilename = 'assignment3_20191670.dat'


def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()

    return scdb


def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))

        if inputstr == "": 
            continue

        parse = inputstr.split(" ")

        if parse[0] == 'add':
            try:
                if (parse[2].isdigit() and parse[3].isdigit()):
                    record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
                    scdb += [record]
                else:
                    print('Please enter an integer.')
            except IndexError:
                print('Enter a age or score to add')

        elif parse[0] == 'del':
            try:
                for p in reversed(scdb): # 이준호 학우님의 아이디어 반영
                    if p['Name'] == str(parse[1]):
                        scdb.remove(p)
            except IndexError:
                print('Add a name to delete.')
            except ValueError:
                print('Please enter a string.')

        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)

        elif parse[0] == 'find':
            try:
                for p in scdb:
                    if p['Name'] == str(parse[1]):
                        print(p)
            except IndexError:
                print('Add a name to find.')
            except ValueError:
                print('Please enter a string.')

        elif parse[0] == 'inc':
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        p['Score'] = str(int(p['Score']) + int(parse[2]))
            except IndexError:
                print('Add a name or amount to insert.')
            except ValueError:
                print('Please enter an integer.')
                
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
