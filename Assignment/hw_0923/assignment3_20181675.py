import pickle

dbfilename = 'assignment3_20181675.dat'


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
    while(True):
        try:
            inputstr = (input("Score DB > "))
            if inputstr == "":
                continue
            parse = inputstr.split(" ")
            if parse[0] == 'add':
                if len(parse) < 4:
                    raise Exception('add할 name, age, score를 입력하시오.')
                if not (parse[2].isdigit() and parse[3].isdigit()):
                    raise Exception('age와 score는 정수로 입력하시오.')
                record = {'Name': parse[1], 'Age': int(parse[2]),
                          'Score': int(parse[3])}
                scdb += [record]
            elif parse[0] == 'del':
                if len(parse) < 2:
                    raise Exception('del할 name을 입력하시오.')
                for p in reversed(scdb):
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
            elif parse[0] == 'show':
                sortKey = 'Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)
            elif parse[0] == 'find':
                if len(parse) < 2:
                    raise Exception('find할 name을 입력하시오.')
                target_scdb = []
                for p in scdb:
                    if p['Name'] == parse[1]:
                        target_scdb.append(p)
                showScoreDB(target_scdb, 'Age')
            elif parse[0] == 'inc':
                if len(parse) < 3:
                    raise Exception('inc할 name과 amount를 입력하시오.')
                if not parse[2].isdigit():
                    raise Exception('inc할 amount는 정수로 입력하시오.')
                for p in scdb:
                    if p.get('Name') == parse[1]:
                        p['Score'] += int(parse[2])
            elif parse[0] == 'quit':
                break
            else:
                print("Invalid command: " + parse[0])
        except Exception as e:
            print('[Error]', e)


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(f"{attr}={p[attr]}", end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
