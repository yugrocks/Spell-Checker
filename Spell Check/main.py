import spellCheck

#initialize dictionary from a database of words with every word having an equal preference
dic={}

dbase=open(r'words.txt')

for _ in dbase:
    dic[_.strip()]=[1]
spellCheck.initialize(dic)


#print the most probable correction
print(spellCheck.correction("pythok")) # single substitution case

print(spellCheck.correction("pythn")) #single deletion case

print(spellCheck.correction("pythno")) #single transpose case

print(spellCheck.correction("pythone")) #single insertion case
