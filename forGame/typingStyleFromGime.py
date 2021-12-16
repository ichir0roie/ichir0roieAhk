

# read gime

with open("getaroQmkCustom.gime", mode="r", encoding='utf-8')as f:
    data = f.read()

# create gimeDict

giDict={}

for line in data.split("\n"):
    try:
        key,value=line.split("\t")
        giDict[key]=value
    except:
        print("can't split. line : {}".format(line))

# from japan to roma.

with open("JapanToRoma.tsv",mode="r",encoding='utf-8')as f:
    data=f.read()

jtrDict={}

for line in data.split("\n"):
    try:
        key,value=line.split("\t")
        jtrDict[key]=value
    except:
        print("can't split. line : {}".format(line))


# create key to roma

ktrDict={}

for key in giDict.keys():
    giValue=giDict[key]

    if giValue in jtrDict.keys():
        try:
            jtrValue=jtrDict[giValue]
            ktrDict[key]=jtrValue
        except:
            print("not find item from japan to hira. key:{},value:{}".format(key,giValue))
    else:
        ktrDict[key]=giValue

for c,i in enumerate(ktrDict.keys()):
    print("{} : {}:{}".format(c,i,ktrDict[i]))

# create .AutoHotKey from keyToRoma Dict.

remapLineFormat="{}::Send, {} return"

ahkText=""

ahkText+="SendMode Input\n\n"

for key in ktrDict.keys():
    value= ktrDict[key]

    addText=""
    if len(key)>1:
        addText+="::"
    addText+=remapLineFormat.format(key,value)

    ahkText+=addText+"\n"


with open("gimeToAhk.ahk",mode="w",encoding="utf-8")as f:
    f.write(ahkText)



