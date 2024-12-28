ifile=open("nee.txt","r")
ofile=open("nee2.txt","w")

list=[]
for line in ifile:
    words=line.split()
    list.append(words)

ofile.write("name "+"roll no"+"\n")
for i in list:
    ofile.write(i[0]+i[1].rjust(10," ")+"\n")
ifile.close()
ofile.close()