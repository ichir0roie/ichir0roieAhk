'''
flow

a→no
key a
gime a の
hiraToAlpha の no

↓

generate ahk a::no
'''

# load googleIme (keyToGetaro)

gimePath="getaroQmkCustom.gime"

with open(gimePath,mode="r",encoding="utf-8")as f:
    gimeList=f.read().split("\n")

dictGime={}
for item in gimeList:
    if item=="":
        continue
    key,value=item.split("\t")
    if key=="":
        continue
    dictGime[key]=value
# print(dictGime)

# load HiraToAlpha

hiraToAlphaPath="alphaToHira.tsv"

with open(hiraToAlphaPath,mode="r",encoding="utf-8")as f:
    hiraList=f.read().split("\n")

dictHira={}
for item in hiraList:
    if item=="":
        continue
    value,key=item.split("\t")
    if key=="":
        continue
    dictHira[key]=value
# print(dictHira)

printText=""

for key in list(dictGime.keys())[:28]:
    #key=key
    hira=dictGime[key]
    roma=dictHira[hira]

    code=key+"::Send {Text}"+roma+" ; "+hira
    print(code)
    printText+=code+"\n"


with open("test.ahk",mode="w",encoding="utf-8")as f:
    f.write(printText)
