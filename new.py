file=open("nee.txt",mode="w+")

dict={"thejas":"c41",
      "sushanth":"c37",
      "sushanths":"c36"}
for line in file:
    new=line.split()
    for word in new:
        dict[word]=dict.get(word,0)+1
print(dict)
listz=[]
for key,val in dict.items():
    listz.append((key,val))

for i in listz:
    file.write(str(i[0])+" ---->"+str(i[1])+"\n")

file.close()

for lines in open("nee.txt"):
    nline=lines.split()
    print(nline[0],"---->",nline[1])
print("this is a python repo")



#this is just for practice 
#i dont intend to write any code in this repo