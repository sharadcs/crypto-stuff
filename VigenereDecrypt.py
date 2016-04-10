def VigenereDecrypt(ciphertext, key):

    plaintext = ""

    keylen = len(key)

    numkey = [] 
    for i in range(keylen):
        numkey.append(ord(key[i])-65)

    for i in range(len(ciphertext)):
        plaintext += chr((ord(ciphertext[i]) - 65 - numkey[i%keylen])%26 + 65)

    print(plaintext)
    return plaintext

ciphertext = "\
DOEESFDAWTSRJSXSHRZFHJGBIEAGIEOIGKWYANVWKVPHAAGYKNZLVVJBTUYP\
QROWRBREKSQUAMBUOYRELKSYENPZWPDHXOOFXRXOWACAISFGECNDOEHYFSZB\
ZOKGIFLRHVIPPHBKVRWDPSGFQNDMDBJHBKPEAALLOAZHXDCBGEWXFBIMRHCV\
JTHXJVAWEAYRWSMJOACEESBXXIKVKVPHWMZYCRXQDYQMTYSNJDTTZNYKMGDX\
JOMKCJWTLGBFWIWZSFQDWWBYUYHMRBJOMHFBLOLWHBENOWGGENLGIGDAYJWP\
WNLWQHNIMASF"
key = "WATSON"
plaintext = VigenereDecrypt(ciphertext,key)

