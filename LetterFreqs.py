def FindKey(ciphertext, keylen):

    letter_frequencies = [
        0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070,
        0.002, 0.008, 0.040, 0.024, 0.067, 0.075, 0.019, 0.001, 0.060,
        0.063, 0.091, 0.028, 0.010, 0.023, 0.001, 0.020, 0.001,
    ]

    key = ""

    for k in range(keylen):

        counts = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        ]

        freqs = []

        fit = []

        #count occurences for the set corresponding to keyletter
        for i in range(len(ciphertext)):
            if(i%keylen == k):
                letter = ord(ciphertext[i])-65 
                counts[letter] = counts[letter]+1

        #generate distribution for this count
        total = float(sum(counts))
        for i in range(26):
            freqs.append(counts[i]/total)

        #compare distributions produced by various keys using dot product
        for i in range(26):
            product = 0
            for j in range(26):
                product += (letter_frequencies[(j-i)%26]*freqs[j])
            fit.append(product)

        guess = fit.index(max(fit))%26
        key += chr(guess + 65)

    print(key)
    return key


ciphertext =  "\
FEWCNWQBMSNSTEJYWOTMXDGVXYCVCYYODSGDQEUOFOTNBAUDQEDKLKDYWEQP\
JLKPNSROWTFOOEPNRNICXMGDQIPQHOWEBEVRNMCCJPWXLHNSWEKRJVGXNIVR\
NRVRNTKWNNQBCHGSWCNSWAVSXNVYNXRVJIPWHSGVOTQKVAPGQOTSBEUKWDUV\
NERCDNFOATJOKLCXTEVYOTJOEETIORGOMOODQAVSYRQFRDGKWDVRNNSENSVS\
XNUDQEOKWNGBRNYRRCJSYRQFRDGSC"

keylen = 4

FindKey(ciphertext,keylen)



