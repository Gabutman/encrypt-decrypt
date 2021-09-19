def list_text(t):
	n = ""
	for i in range(t):
		n+=str(chr(i))
	return n
def dm(t):
	d=0
	for i in t:
		d+=ord(i)
	return d
def dm0(t):
	return [ord(i) for i in t]
t,d,s,m,k,md="","",list_text(1114112),dm(input("input the value:")),dm(input("input key:")),int(input("input mod:"))
if m < 1:
        m = 1
if k < 1:
        k = 1
if md < 1:
        md = 3
for i in dm0(open(input("filename1:"),"r").read()):
	t+=s[s.find(str(chr(int(i)-m)))-k%md]
f = open("filename2:","w")
f.write(t)
f.close()
