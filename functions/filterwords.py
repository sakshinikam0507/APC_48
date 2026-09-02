words=input("Enter words: ").split()
ans=list(filter(lambda word:len(word)>5,words))
print(ans)
