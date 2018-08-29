# q.1 read n lines of a file
p=open('file1.txt','r')
file=p.read()
print(file)
p.close()
print()


# q.2 count the frequency of words in a file

r=open("file1.txt",'r')
data=r.read()
w=data.split()
dict={}
for i in w:
    dict[i]=w.count(i)
print(dict)
print()


# q.3 copy the contents of a file to another file

a=open("file1.txt",'r')
t=open("file2.txt",'w')
for i in a:
    t.write(i)
a.close()
t.close()
print()


# q.4 combine each line from first file with the corresponding line in second file

e=open("file1.txt",'r')
k=open("file3.txt",'r')
for i1,i2 in zip(e,k):
    s=open("combi.txt",'a')
    s.write(i1+i2)
    s.close()
k.close()
e.close()
print()


# q.5 read a file and sort it to another file

h=open('file1.txt')
te=open('sort.txt','w+')
srt=h.readlines()
srt.sort()
te.write(str(srt))
te.seek(0)
output=te.read()
print(output)
print()
