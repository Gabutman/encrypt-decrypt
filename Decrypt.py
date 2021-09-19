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
for i in dm0(open(input("filename1:"),"r").read()):
	t+=s[s.find(str(chr(int(i)-m)))-k%md]
open("filename2:","w").write(t)
