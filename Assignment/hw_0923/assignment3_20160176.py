import pickle

dbfilename = 'assignment3.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
        for i in scdb:
            i['Age'] = int(i['Age'])
            i['Score'] = int(i['Score'])
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
                    print('name, age, score를 모두 입력하세요.')
                    continue
                if not (parse[2].isdigit() and parse[3].isdigit()):
                    print('age와 score는 숫자로 입력하세요.')
                    continue
                record = {'Name': parse[1], 'Age': int(parse[2]), 'Score': int(parse[3])}
                scdb += [record]
                elif parse[0] == 'del':
                count = 0
                if len(parse) < 2:
                    print('이름을 입력해주세요')
                    continue
                for p in scdb:
                    if p['Name'] == parse[1]:
                        count += 1
                        scdb.remove(p)
                        break
                if count == 0:
                    print('해당 이름이 존재하지 않습니다.')
            elif parse[0] == 'show':
                sortKey = 'Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)
            elif parse[0] == 'quit':
                break
            elif parse[0] == 'find':
                if len(parse) < 2:
                    print('이름을 입력해주세요')
                    continue
                tmp_scdb = []
                for i in scdb:
                    if i['Name'] == parse[1]:
                        tmp_scdb.append(i)
                        showScoreDB(tmp_scdb, 'Name')
                        break
            elif parse[0] == 'inc':
                if len(parse) < 3:
                    print('name과 amount를 모두 입력하세요.')
                    continue
                if not parse[2].isdigit():
                    print('amount는 숫자로 입력하세요.')
                    continue
                for i in scdb:
                    if i['Name'] == parse[1]:
                        i['Score'] += int(parse[2])
            else:
                print("Invalid command: " + parse[0])
        except Exception as e:
            print(e)


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + str(p[attr]), end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
