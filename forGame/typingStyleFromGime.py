

# read gime

with open("getaroQmkCustom.gime", mode="r", encoding='utf-8')as f:
    data = f.read()

# create gimeDict

gImeDict={}

for line in data.split("\r\n"):
    try:
        key,value=line.split("\t")
        gImeDict[key]=value
    except:
        print("can't split. line : {}".format(line))
    

for key in gImeDict.keys():
    print("key:{}\t\tvalue:{}".format(key,gImeDict[i]))

