def count(sentence):
    letter=list(sentence)
    uppercase=0
    lowercase=0

    for i in letter:
        if(i>="A" and i<="Z"):
            uppercase+=1
        elif(i>="a" and i<="z"):
            lowercase+=1
        else:
            continue

    print("No of lowercase: ",lowercase)
    print("No of uppercase: ",uppercase)


sentence="The quick Brow Fox"
count(sentence)
