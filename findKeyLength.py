def findKeyLength(ciphertext):

    posskeylens = [];

    for i in range (1,len(ciphertext)/2):
        posskeylens.append(0);
        for j in range (0,len(ciphertext)):
            if(j+i < len(ciphertext)):
                if(ciphertext[j+i] == ciphertext[j]):
                   posskeylens[i-1] = posskeylens[i-1]+1;

    print(posskeylens)
    return posskeylens.index(max(posskeylens)+1)

ciphertext = "\
DOEESFDAWTSRJSXSHRZFHJGBIEAGIEOIGKWYANVWKVPHAAGYKNZLVVJBTUYP\
QROWRBREKSQUAMBUOYRELKSYENPZWPDHXOOFXRXOWACAISFGECNDOEHYFSZB\
ZOKGIFLRHVIPPHBKVRWDPSGFQNDMDBJHBKPEAALLOAZHXDCBGEWXFBIMRHCV\
JTHXJVAWEAYRWSMJOACEESBXXIKVKVPHWMZYCRXQDYQMTYSNJDTTZNYKMGDX\
JOMKCJWTLGBFWIWZSFQDWWBYUYHMRBJOMHFBLOLWHBENOWGGENLGIGDAYJWP\
WNLWQHNIMASF"

print(findKeyLength(ciphertext))
