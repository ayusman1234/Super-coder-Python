#paired
mylist = [9, 3, 6, 1, 5, 0, 8, 2, 4, 7]
list_b = [6, 4, 6, 1, 2, 2]
result = []
for i in list_b:
    result.append((i, mylist.index(i)))
print(result)

print([(i,mylist.index(i))for i in list_b])
#problem1
sentences = ["a new world record was set", 
             "in the holy city of ayodhya", 
             "on the eve of diwali on tuesday", 
             "with over three lakh diya or earthen lamps", 
             "lit up simultaneously on the banks of the sarayu river"]

stopwords = ['for', 'a', 'of', 'the', 'and', 'to', 'in', 'on', 'with','was']

results = []    
for sentence in sentences:
    sentence_tokens = []
    for word in sentence.split(' '):
        if word not in stopwords:
            sentence_tokens.append(word)
    results.append(sentence_tokens)

print(results)
