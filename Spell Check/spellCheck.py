import re

def initialize(dct):
    global dic
    dic=dct

def editDist1(word):
    #All edits at a distance of one including insertions and deletions and replaces and transposes
    alphabets='abcdefghijklmnopqrstuvwxyz'
    split=[]
    deletes=[]
    transposes=[]
    insertions=[]
    replaces=[]
    for _ in range(len(word)+1):
        split.append((word[:_],word[_:]))

    for i,j in split:
        deletes.append(i+j[1:])
    for i,j in split:
        if len(j)>1:
          transposes.append(i+j[1]+j[0]+j[2:])
    for i,j in split:
        for _ in alphabets:
          insertions.append(i+_+j)
    for i,j in split:
        if j:
          for _ in alphabets:
            replaces.append(i+_+j[1:])

    return set(deletes+transposes+replaces+insertions)

def editDist2(word):
    return (i for j in editDist1(word) for i in editDist1(j))

def matches(listOfWords):
    st=set()
    for _ in listOfWords:
       if _ in dic:
           st.add(_)

    return st

def possibleWords(word):
    return (matches([word]) or matches(editDist1(word)) or matches(editDist2(word)) or [word])

def criteria(word):
    if word in dic:
      return len(dic[word])


def correction(word):
    return max(possibleWords(word),key=criteria)










    
