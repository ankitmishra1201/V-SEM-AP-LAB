sentence="khadak singh ne khadak ti hai khadak ti hai kidhkiya"

counts=dict()
words=sentence.split()

for word in words:
    if word in counts:
        counts[word]+=1
    else:
        counts[word]=1


print(counts)
