import pickle

dbfilename = 'assignment_20190406.dat'

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
                if len(parse) != 4:
                    raise Exception("추가할 Name, Age, Score를 모두 입력하세요")
                if not (parse[2].isdigit() and parse[3].isdigit()):
                    raise Exception('age와 score는 정수로 입력하시오.')
                record = {'Name':parse[1], 'Age':int(parse[2]), 'Score':int(parse[3])}
                scdb += [record]

            # del 수정
            elif parse[0] == 'del':
                if len(parse) != 2:
                    raise Exception("삭제할 name을 입력하세요")
                for p in reversed(scdb):
                    if p['Name'] == parse[1]:
                        scdb.remove(p)    

            elif parse[0] == 'show':
                sortKey ='Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)

            # find 추가
            elif parse[0] == 'find':
                if len(parse) != 2:
                    raise Exception("찾고 싶은 Name을 입력하세요")
                find_scdb = []
                sortKey = 'Age'
                for p in scdb:
                    if p['Name'] == parse[1]:
                        find_scdb.append(p)
                showScoreDB(find_scdb, sortKey)

            # inc 추가
            elif parse[0] == 'inc':
                if len(parse) != 3:
                    raise Exception("Name과 amount를 모두 입력하세요")
                sortKey = 'Score'
                for p in scdb:
                    if p['Name'] == parse[1]:
                        p['Score'] += int(parse[2])

            elif parse[0] == 'quit':
                break
            else:
                print("Invalid command: " + parse[0])

        except Exception as e:
            print("에러 발생", e)


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + str(p[attr]), end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
