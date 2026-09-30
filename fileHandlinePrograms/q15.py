f=open("program.py","r")
g=open("newprogram.py","w")
for line in f:
    if "#" in line:
        line=line.split("#")[0]+"\n"
    g.write(line)
f.close()
g.close()