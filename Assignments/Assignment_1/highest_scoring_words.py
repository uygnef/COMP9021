import copy
import sys

dic=[]
with open('wordsEN.txt') as file:
    for word in file:
      word=word.strip()
      dic.append(word)


inp=input('Enter between 3 and 10 lowercase letters:')
inp=inp.replace(' ','')

if inp.isalpha() and inp.islower() and 2<len(inp)<11:
    pass
else:
    print('Incorrect input, giving up . . .')
    sys.exit()

value={'a':2, 'b':5, 'c':4, 'd':4, 'e':1, 'f':6, \
       'g':5, 'h':5, 'i':1, 'j':7, 'k':6, 'l':3, \
       'm':5, 'n':2, 'o':3, 'p':5, 'q':7, 'r':2, \
       's':1, 't':2, 'u':4, 'v':6, 'w':6, 'x':7, \
       'y':5, 'z':7}


def in_dic():
  result=[]
  for word in dic:
    if len(inp)>=len(word):
      temp_inp=list(inp)  
      for i in range(len(word)):
        if word[i] in temp_inp:
            temp_inp.remove(word[i])
            if i==len(word)-1:
              result.append(word)
        else:
            break
  return result

result=in_dic()
if result==[]:
  print('No word is built from some of those letters . ')
  sys.exit()
score=0
list_result=[]
end_number=[]
for a in result:
  score=0
  for i in a:
    score=value[i]+score
  list_result.append(score)
  max_number=max(list_result)
print('The highest score is {}.'.format(max_number))


print('The highests coring words are, in alphabetical order:')
for m in range(len(list_result)):
  if list_result[m]==max_number:
     print('    ',result[m])
    
    

      
    
    


    
