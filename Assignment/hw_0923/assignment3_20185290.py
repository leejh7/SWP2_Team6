import pickle

dbfilename = 'assignment3_20185290.dat'


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
                    raise Exception('NAME, AGE, SCORE를 입력해주세요.')
                if not (parse[2].isdigit() and parse[3].isdigit()):
                    raise Exception('AGE, SCORE 정수로 입력해주세요.')
                record = {'Name': parse[1], 'Age': int(parse[2]),
                          'Score': int(parse[3])}
                scdb += [record]


            elif parse[0] == 'del':
                if len(parse) < 2:
                    raise Exception('삭제할 NAME을 입력하세요.')
                for p in reversed(scdb):
                    if p['Name'] == parse[1]:
                        scdb.remove(p)


            elif parse[0] == 'show':
                sortKey = 'Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)


            elif parse[0] == 'find':
                if len(parse) < 2:
                    raise Exception('찾을 NAME을 입력하세요.')
                findname_scdb = []
                for p in scdb:
                    if p['Name'] == parse[1]:
                        findname_scdb.append(p)
                showScoreDB(findname_scdb, 'Age')


            elif parse[0] == 'inc':
                if len(parse) < 3:
                    raise Exception('NAME과 AMOUNT를 입력하세요.')
                if not parse[2].isdigit():
                    raise Exception('INC할 AMOUNT를 정수로 입력하세요.')
                for p in scdb:
                    if p.get('Name') == parse[1]:
                        p['Score'] += int(parse[2])
            elif parse[0] == 'quit':
                break
            else:
                print("Invalid command: " + parse[0])

        except Exception as e:
            print('error 발생', e)


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr+"="+str(p[attr]), end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
