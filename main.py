import requests
from datetime import datetime
from random import randint

a = "dfb44d0c-"
b = "50e8-4e42-bac7-"
c = "6427659133a9"
z = a+b+c

usedaTextFile = open("usedawords.txt", "r")
usedbTextFile = open("usedbwords.txt", "r")
usedcTextFile = open("usedcwords.txt", "r")
useddTextFile = open("useddwords.txt", "r")
usedeTextFile = open("usedewords.txt", "r")
usedfTextFile = open("usedfwords.txt", "r")
usedgTextFile = open("usedgwords.txt", "r")
usedhTextFile = open("usedhwords.txt", "r")
usediTextFile = open("usediwords.txt", "r")
usedjTextFile = open("usedjwords.txt", "r")
usedkTextFile = open("usedkwords.txt", "r")
usedlTextFile = open("usedlwords.txt", "r")
usedmTextFile = open("usedmwords.txt", "r")
usednTextFile = open("usednwords.txt", "r")
usedoTextFile = open("usedowords.txt", "r")
usedpTextFile = open("usedpwords.txt", "r")
usedqTextFile = open("usedqwords.txt", "r")
usedrTextFile = open("usedrwords.txt", "r")
usedsTextFile = open("usedswords.txt", "r")
usedtTextFile = open("usedtwords.txt", "r")
useduTextFile = open("useduwords.txt", "r")
usedvTextFile = open("usedvwords.txt", "r")
usedwTextFile = open("usedwwords.txt", "r")
usedxTextFile = open("usedxwords.txt", "r")
usedzTextFile = open("usedzwords.txt", "r")

usedaLines = usedaTextFile.read().split()
usedbLines = usedbTextFile.read().split()
usedcLines = usedcTextFile.read().split()
useddLines = useddTextFile.read().split()
usedeLines = usedeTextFile.read().split()
usedfLines = usedfTextFile.read().split()
usedgLines = usedgTextFile.read().split()
usedhLines = usedhTextFile.read().split()
usediLines = usediTextFile.read().split()
usedjLines = usedjTextFile.read().split()
usedkLines = usedkTextFile.read().split()
usedlLines = usedlTextFile.read().split()
usedmLines = usedmTextFile.read().split()
usednLines = usednTextFile.read().split()
usedoLines = usedoTextFile.read().split()
usedpLines = usedpTextFile.read().split()
usedqLines = usedqTextFile.read().split()
usedrLines = usedrTextFile.read().split()
usedsLines = usedsTextFile.read().split()
usedtLines = usedtTextFile.read().split()
useduLines = useduTextFile.read().split()
usedvLines = usedvTextFile.read().split()
usedwLines = usedwTextFile.read().split()
usedxLines = usedxTextFile.read().split()
usedzLines = usedzTextFile.read().split()

# Source for text file
# https://github.com/dwyl/english-words/blob/master/words_alpha.txt
# For some reason the y words were mixed the i words in the original txt file
aTextFile = open("awords.txt", "r")
bTextFile = open("bwords.txt", "r")
cTextFile = open("cwords.txt", "r")
dTextFile = open("dwords.txt", "r")
eTextFile = open("ewords.txt", "r")
fTextFile = open("fwords.txt", "r")
gTextFile = open("gwords.txt", "r")
hTextFile = open("hwords.txt", "r")
iTextFile = open("iwords.txt", "r")
jTextFile = open("jwords.txt", "r")
kTextFile = open("kwords.txt", "r")
lTextFile = open("lwords.txt", "r")
mTextFile = open("mwords.txt", "r")
nTextFile = open("nwords.txt", "r")
oTextFile = open("owords.txt", "r")
pTextFile = open("pwords.txt", "r")
qTextFile = open("qwords.txt", "r")
rTextFile = open("rwords.txt", "r")
sTextFile = open("swords.txt", "r")
tTextFile = open("twords.txt", "r")
uTextFile = open("uwords.txt", "r")
vTextFile = open("vwords.txt", "r")
wTextFile = open("wwords.txt", "r")
xTextFile = open("xwords.txt", "r")
zTextFile = open("zwords.txt", "r")

aLines = aTextFile.read().split()
bLines = bTextFile.read().split()
cLines = cTextFile.read().split()
dLines = dTextFile.read().split()
eLines = eTextFile.read().split()
fLines = fTextFile.read().split()
gLines = gTextFile.read().split()
hLines = hTextFile.read().split()
iLines = iTextFile.read().split()
jLines = jTextFile.read().split()
kLines = kTextFile.read().split()
lLines = lTextFile.read().split()
mLines = mTextFile.read().split()
nLines = nTextFile.read().split()
oLines = oTextFile.read().split()
pLines = pTextFile.read().split()
qLines = qTextFile.read().split()
rLines = rTextFile.read().split()
sLines = sTextFile.read().split()
tLines = tTextFile.read().split()
uLines = uTextFile.read().split()
vLines = vTextFile.read().split()
wLines = wTextFile.read().split()
xLines = xTextFile.read().split()
zLines = zTextFile.read().split()

itemMin = 6

for item in aLines[:]:
    if len(item) < itemMin:
        aLines.remove(item)

for item in bLines[:]:
    if len(item) < itemMin:
        bLines.remove(item)

for item in cLines[:]:
    if len(item) < itemMin:
        cLines.remove(item)

for item in dLines[:]:
    if len(item) < itemMin:
        dLines.remove(item)

for item in eLines[:]:
    if len(item) < itemMin:
        eLines.remove(item)

for item in fLines[:]:
    if len(item) < itemMin:
        fLines.remove(item)

for item in gLines[:]:
    if len(item) < itemMin:
        gLines.remove(item)

for item in hLines[:]:
    if len(item) < itemMin:
        hLines.remove(item)

for item in iLines[:]:
    if len(item) < itemMin:
        iLines.remove(item)

for item in jLines[:]:
    if len(item) < itemMin:
        jLines.remove(item)

for item in kLines[:]:
    if len(item) < itemMin:
        kLines.remove(item)

for item in lLines[:]:
    if len(item) < itemMin:
        lLines.remove(item)

for item in mLines[:]:
    if len(item) < itemMin:
        mLines.remove(item)

for item in nLines[:]:
    if len(item) < itemMin:
        nLines.remove(item)

for item in oLines[:]:
    if len(item) < itemMin:
        oLines.remove(item)

for item in pLines[:]:
    if len(item) < itemMin:
        pLines.remove(item)

for item in qLines[:]:
    if len(item) < itemMin:
        qLines.remove(item)

for item in rLines[:]:
    if len(item) < itemMin:
        rLines.remove(item)

for item in sLines[:]:
    if len(item) < itemMin:
        sLines.remove(item)

for item in tLines[:]:
    if len(item) < itemMin:
        tLines.remove(item)

for item in uLines[:]:
    if len(item) < itemMin:
        uLines.remove(item)

for item in vLines[:]:
    if len(item) < itemMin:
        vLines.remove(item)

for item in wLines[:]:
    if len(item) < itemMin:
        wLines.remove(item)

for item in xLines[:]:
    if len(item) < itemMin:
        xLines.remove(item)

for item in zLines[:]:
    if len(item) < itemMin:
        zLines.remove(item)

definition = "No definition"
newWord = ""
alphaNum = randint(0,24)

td = open("todayDate.txt","r+")
theDate = td.read()

if theDate == datetime.today().strftime('%Y-%m-%d'):
    tdef = open("todayDefinitions.txt","r")
    definition = tdef.read().split("\n")
    definition = definition[:-1]

    tword = open("todayWord.txt","r+")
    newWord = tword.read()

else:
    if alphaNum == 0:
        while definition == 'No definition':
            newWord = aLines[randint(0, len(aLines)-1)]

            while newWord in usedaLines:
                newWord = aLines[randint(0, len(aLines)-1)]

            aurl = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+newWord+'?key='+z

            call = requests.get(aurl)
            jsonList = call.json()

            try:
                definition = jsonList[0]['shortdef']
            except:
                f = open('usedawords.txt', 'a')
                f.write('\n'+newWord)
                f.close()
                definition = 'No definition'

        f = open('usedawords.txt', 'a')
        f.write('\n'+newWord)
        f.close()

    if alphaNum == 1:
        while definition == 'No definition':
            newWord = bLines[randint(0, len(bLines)-1)]

            while newWord in usedbLines:
                newWord = bLines[randint(0, len(bLines)-1)]

            aurl = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+newWord+'?key='+z

            call = requests.get(aurl)
            jsonList = call.json()

            try:
                definition = jsonList[0]['shortdef']
            except:
                f = open('usedbwords.txt', 'a')
                f.write('\n'+newWord)
                f.close()
                definition = 'No definition'

        f = open('usedbwords.txt', 'a')
        f.write('\n'+newWord)
        f.close()

    if alphaNum == 2:
        while definition == 'No definition':
            newWord = cLines[randint(0, len(cLines)-1)]

            while newWord in usedcLines:
                newWord = cLines[randint(0, len(cLines)-1)]

            aurl = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+newWord+'?key='+z

            call = requests.get(aurl)
            jsonList = call.json()

            try:
                definition = jsonList[0]['shortdef']
            except:
                f = open('usedcwords.txt', 'a')
                f.write('\n'+newWord)
                f.close()
                definition = 'No definition'

        f = open('usedcwords.txt', 'a')
        f.write('\n'+newWord)
        f.close()

    if alphaNum == 3:
        while definition == 'No definition':
            newWord = dLines[randint(0, len(dLines)-1)]

            while newWord in useddLines:
                newWord = dLines[randint(0, len(dLines)-1)]

            aurl = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+newWord+'?key='+z

            call = requests.get(aurl)
            jsonList = call.json()

            try:
                definition = jsonList[0]['shortdef']
            except:
                f = open('useddwords.txt', 'a')
                f.write('\n'+newWord)
                f.close()
                definition = 'No definition'

        f = open('useddwords.txt', 'a')
        f.write('\n'+newWord)
        f.close()

    if alphaNum == 4:
        while definition == 'No definition':
            newWord = eLines[randint(0, len(eLines)-1)]

            while newWord in usedeLines:
                newWord = eLines[randint(0, len(eLines)-1)]

            aurl = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+newWord+'?key='+z

            call = requests.get(aurl)
            jsonList = call.json()

            try:
                definition = jsonList[0]['shortdef']
            except:
                f = open('usedewords.txt', 'a')
                f.write('\n'+newWord)
                f.close()
                definition = 'No definition'

        f = open('usedewords.txt', 'a')
        f.write('\n'+newWord)
        f.close()

    if alphaNum == 5:
        while definition == 'No definition':
            newWord = fLines[randint(0, len(fLines)-1)]

            while newWord in usedfLines:
                newWord = fLines[randint(0, len(fLines)-1)]

            aurl = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+newWord+'?key='+z

            call = requests.get(aurl)
            jsonList = call.json()

            try:
                definition = jsonList[0]['shortdef']
            except:
                f = open('usedfwords.txt', 'a')
                f.write('\n'+newWord)
                f.close()
                definition = 'No definition'

        f = open('usedfwords.txt', 'a')
        f.write('\n'+newWord)
        f.close()

    if alphaNum == 6:
        while definition == 'No definition':
            newWord = gLines[randint(0, len(gLines)-1)]

            while newWord in usedgLines:
                newWord = gLines[randint(0, len(gLines)-1)]

            aurl = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+newWord+'?key='+z

            call = requests.get(aurl)
            jsonList = call.json()

            try:
                definition = jsonList[0]['shortdef']
            except:
                f = open('usedgwords.txt', 'a')
                f.write('\n'+newWord)
                f.close()
                definition = 'No definition'

        f = open('usedgwords.txt', 'a')
        f.write('\n'+newWord)
        f.close()

    if alphaNum == 7:
        while definition == 'No definition':
            newWord = hLines[randint(0, len(hLines)-1)]

            while newWord in usedhLines:
                newWord = hLines[randint(0, len(hLines)-1)]

            aurl = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+newWord+'?key='+z

            call = requests.get(aurl)
            jsonList = call.json()

            try:
                definition = jsonList[0]['shortdef']
            except:
                f = open('usedhwords.txt', 'a')
                f.write('\n'+newWord)
                f.close()
                definition = 'No definition'

        f = open('usedhwords.txt', 'a')
        f.write('\n'+newWord)
        f.close()

    if alphaNum == 8:
        while definition == 'No definition':
            newWord = iLines[randint(0, len(iLines)-1)]

            while newWord in usediLines:
                newWord = iLines[randint(0, len(iLines)-1)]

            aurl = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+newWord+'?key='+z

            call = requests.get(aurl)
            jsonList = call.json()

            try:
                definition = jsonList[0]['shortdef']
            except:
                f = open('usediwords.txt', 'a')
                f.write('\n'+newWord)
                f.close()
                definition = 'No definition'

        f = open('usediwords.txt', 'a')
        f.write('\n'+newWord)
        f.close()

    if alphaNum == 9:
        while definition == 'No definition':
            newWord = jLines[randint(0, len(jLines)-1)]

            while newWord in usedjLines:
                newWord = jLines[randint(0, len(jLines)-1)]

            aurl = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+newWord+'?key='+z

            call = requests.get(aurl)
            jsonList = call.json()

            try:
                definition = jsonList[0]['shortdef']
            except:
                f = open('usedjwords.txt', 'a')
                f.write('\n'+newWord)
                f.close()
                definition = 'No definition'

        f = open('usedjwords.txt', 'a')
        f.write('\n'+newWord)
        f.close()

    if alphaNum == 10:
        while definition == 'No definition':
            newWord = kLines[randint(0, len(kLines)-1)]

            while newWord in usedkLines:
                newWord = kLines[randint(0, len(kLines)-1)]

            aurl = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+newWord+'?key='+z

            call = requests.get(aurl)
            jsonList = call.json()

            try:
                definition = jsonList[0]['shortdef']
            except:
                f = open('usedkwords.txt', 'a')
                f.write('\n'+newWord)
                f.close()
                definition = 'No definition'

        f = open('usedkwords.txt', 'a')
        f.write('\n'+newWord)
        f.close()

    if alphaNum == 11:
        while definition == 'No definition':
            newWord = lLines[randint(0, len(lLines)-1)]

            while newWord in usedlLines:
                newWord = lLines[randint(0, len(lLines)-1)]

            aurl = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+newWord+'?key='+z

            call = requests.get(aurl)
            jsonList = call.json()

            try:
                definition = jsonList[0]['shortdef']
            except:
                f = open('usedlwords.txt', 'a')
                f.write('\n'+newWord)
                f.close()
                definition = 'No definition'

        f = open('usedlwords.txt', 'a')
        f.write('\n'+newWord)
        f.close()

    if alphaNum == 12:
        while definition == 'No definition':
            newWord = mLines[randint(0, len(mLines)-1)]

            while newWord in usedmLines:
                newWord = mLines[randint(0, len(mLines)-1)]

            aurl = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+newWord+'?key='+z

            call = requests.get(aurl)
            jsonList = call.json()

            try:
                definition = jsonList[0]['shortdef']
            except:
                f = open('usedmwords.txt', 'a')
                f.write('\n'+newWord)
                f.close()
                definition = 'No definition'

        f = open('usedmwords.txt', 'a')
        f.write('\n'+newWord)
        f.close()

    if alphaNum == 13:
        while definition == 'No definition':
            newWord = nLines[randint(0, len(nLines)-1)]

            while newWord in usednLines:
                newWord = nLines[randint(0, len(nLines)-1)]

            aurl = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+newWord+'?key='+z

            call = requests.get(aurl)
            jsonList = call.json()

            try:
                definition = jsonList[0]['shortdef']
            except:
                f = open('usednwords.txt', 'a')
                f.write('\n'+newWord)
                f.close()
                definition = 'No definition'

        f = open('usednwords.txt', 'a')
        f.write('\n'+newWord)
        f.close()

    if alphaNum == 14:
        while definition == 'No definition':
            newWord = oLines[randint(0, len(oLines)-1)]

            while newWord in usedoLines:
                newWord = oLines[randint(0, len(oLines)-1)]

            aurl = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+newWord+'?key='+z

            call = requests.get(aurl)
            jsonList = call.json()

            try:
                definition = jsonList[0]['shortdef']
            except:
                f = open('usedowords.txt', 'a')
                f.write('\n'+newWord)
                f.close()
                definition = 'No definition'

        f = open('usedowords.txt', 'a')
        f.write('\n'+newWord)
        f.close()

    if alphaNum == 15:
        while definition == 'No definition':
            newWord = pLines[randint(0, len(pLines)-1)]

            while newWord in usedpLines:
                newWord = pLines[randint(0, len(pLines)-1)]

            aurl = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+newWord+'?key='+z

            call = requests.get(aurl)
            jsonList = call.json()

            try:
                definition = jsonList[0]['shortdef']
            except:
                f = open('usedpwords.txt', 'a')
                f.write('\n'+newWord)
                f.close()
                definition = 'No definition'

        f = open('usedpwords.txt', 'a')
        f.write('\n'+newWord)
        f.close()

    if alphaNum == 16:
        while definition == 'No definition':
            newWord = qLines[randint(0, len(qLines)-1)]

            while newWord in usedqLines:
                newWord = qLines[randint(0, len(qLines)-1)]

            aurl = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+newWord+'?key='+z

            call = requests.get(aurl)
            jsonList = call.json()

            try:
                definition = jsonList[0]['shortdef']
            except:
                f = open('usedqwords.txt', 'a')
                f.write('\n'+newWord)
                f.close()
                definition = 'No definition'

        f = open('usedqwords.txt', 'a')
        f.write('\n'+newWord)
        f.close()

    if alphaNum == 17:
        while definition == 'No definition':
            newWord = rLines[randint(0, len(rLines)-1)]

            while newWord in usedrLines:
                newWord = rLines[randint(0, len(rLines)-1)]

            aurl = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+newWord+'?key='+z

            call = requests.get(aurl)
            jsonList = call.json()

            try:
                definition = jsonList[0]['shortdef']
            except:
                f = open('usedrwords.txt', 'a')
                f.write('\n'+newWord)
                f.close()
                definition = 'No definition'

        f = open('usedrwords.txt', 'a')
        f.write('\n'+newWord)
        f.close()

    if alphaNum == 18:
        while definition == 'No definition':
            newWord = sLines[randint(0, len(sLines)-1)]

            while newWord in usedsLines:
                newWord = sLines[randint(0, len(sLines)-1)]

            aurl = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+newWord+'?key='+z

            call = requests.get(aurl)
            jsonList = call.json()

            try:
                definition = jsonList[0]['shortdef']
            except:
                f = open('usedswords.txt', 'a')
                f.write('\n'+newWord)
                f.close()
                definition = 'No definition'

        f = open("usedswords.txt", "a")
        f.write("\n"+newWord)
        f.close()

    if alphaNum == 19:
        while definition == 'No definition':
            newWord = tLines[randint(0, len(tLines)-1)]

            while newWord in usedtLines:
                newWord = tLines[randint(0, len(tLines)-1)]

            aurl = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+newWord+'?key='+z

            call = requests.get(aurl)
            jsonList = call.json()

            try:
                definition = jsonList[0]['shortdef']
            except:
                f = open('usedtwords.txt', 'a')
                f.write('\n'+newWord)
                f.close()
                definition = 'No definition'

        f = open("usedtwords.txt", "a")
        f.write("\n"+newWord)
        f.close()

    if alphaNum == 20:
        while definition == 'No definition':
            newWord = uLines[randint(0, len(uLines)-1)]

            while newWord in useduLines:
                newWord = uLines[randint(0, len(uLines)-1)]

            aurl = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+newWord+'?key='+z

            call = requests.get(aurl)
            jsonList = call.json()

            try:
                definition = jsonList[0]['shortdef']
            except:
                f = open('useduwords.txt', 'a')
                f.write('\n'+newWord)
                f.close()
                definition = 'No definition'

        f = open("useduwords.txt", "a")
        f.write("\n"+newWord)
        f.close()

    if alphaNum == 21:
        while definition == 'No definition':
            newWord = vLines[randint(0, len(vLines)-1)]

            while newWord in usedvLines:
                newWord = vLines[randint(0, len(vLines)-1)]

            aurl = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+newWord+'?key='+z

            call = requests.get(aurl)
            jsonList = call.json()

            try:
                definition = jsonList[0]['shortdef']
            except:
                f = open('usedvwords.txt', 'a')
                f.write('\n'+newWord)
                f.close()
                definition = 'No definition'

        f = open("usedvwords.txt", "a")
        f.write("\n"+newWord)
        f.close()

    if alphaNum == 22:
        while definition == 'No definition':
            newWord = wLines[randint(0, len(wLines)-1)]

            while newWord in usedwLines:
                newWord = wLines[randint(0, len(wLines)-1)]

            aurl = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+newWord+'?key='+z

            call = requests.get(aurl)
            jsonList = call.json()

            try:
                definition = jsonList[0]['shortdef']
            except:
                f = open('usedwwords.txt', 'a')
                f.write('\n'+newWord)
                f.close()
                definition = 'No definition'

        f = open("usedwwords.txt", "a")
        f.write("\n"+newWord)
        f.close()

    if alphaNum == 23:
        while definition == 'No definition':
            newWord = xLines[randint(0, len(xLines)-1)]

            while newWord in usedxLines:
                newWord = xLines[randint(0, len(xLines)-1)]

            aurl = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+newWord+'?key='+z

            call = requests.get(aurl)
            jsonList = call.json()

            try:
                definition = jsonList[0]['shortdef']
            except:
                f = open('usedxwords.txt', 'a')
                f.write('\n'+newWord)
                f.close()
                definition = 'No definition'

        f = open("usedxwords.txt", "a")
        f.write("\n"+newWord)
        f.close()

    if alphaNum == 24:
        while definition == 'No definition':
            newWord = zLines[randint(0, len(zLines)-1)]

            while newWord in usedzLines:
                newWord = zLines[randint(0, len(zLines)-1)]

            aurl = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+newWord+'?key='+z

            call = requests.get(aurl)
            jsonList = call.json()

            try:
                definition = jsonList[0]['shortdef']
            except:
                f = open('usedzwords.txt', 'a')
                f.write('\n'+newWord)
                f.close()
                definition = 'No definition'
        
        f = open("usedzwords.txt", "a")
        f.write("\n"+newWord)
        f.close()

    todayDate = datetime.today().strftime('%Y-%m-%d')
    d = open("todayDate.txt", "w")
    d.write(todayDate)
    d.close()

    n = open("todayWord.txt", "w")
    n.write(newWord)
    n.close()

    with open("todayDefinitions.txt", "w") as txt_file:
        for line in definition:
            txt_file.write("".join(line) + "\n")
        txt_file.truncate()
    
print("Word: " + newWord)
for i in range(len(definition)):
    print("Definition " + str(i+1) + ": " + definition[i])
print("")
input("Click ''Enter'' to end...")
