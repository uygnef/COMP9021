import copy
import sys

dic=[]
with open('wordsEN.txt') as file:
    for word in file:
      word.strip('') 
      dic.append(word)
#print(dic[1])

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



def in_dic(word):
  result=[]
  for word in dic:
    temp_word=list(word)
    for i in range(len(inp)):
      if inp[i] in temp_word:
          temp_word.remove(inp[i])
      else:
          break
      result.append(word)

#if in_dic(inp)==None:
 # print('No word is built from some of those letters . ')
#else:
print(in_dic(inp))
      
    
    


    
