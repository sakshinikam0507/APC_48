words=input("Enter words: ").split()

lengths=list(map(lambda x:len(x),words))
longwords=list(filter(lambda x:len(x)>5,words))
sortedwords=sorted(words,key=lambda x:len(x))

print("Lengths:",lengths)
print("More than five characters:",longwords)
print("Sorted words:",sortedwords)
