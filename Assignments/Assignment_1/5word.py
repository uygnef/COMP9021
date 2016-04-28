dic=[]
with open('wordsEN.txt') as file:
    for word in file:
      word.strip('') 
      dic.append(word)
print(dic[1])