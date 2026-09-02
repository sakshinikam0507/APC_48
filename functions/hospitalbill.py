def getconsult(amt):
    return amt

def getlab(amt):
    return amt

def getmed(amt):
    return amt

def getroom(amt):
    return amt

def final(consult,lab,med,room,cat):
    tot=consult+lab+med+room
    if cat=="senior":
        tot-=tot*0.20
    elif cat=="child":
        tot-=tot*0.10
    return tot

consult=getconsult(float(input("Consultation charges: ")))
lab=getlab(float(input("Laboratory charges: ")))
med=getmed(float(input("Medicine charges: ")))
room=getroom(float(input("Room charges: ")))
cat=input("Patient category: ")

print("Final bill:",final(consult,lab,med,room,cat))
