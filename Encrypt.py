def list_text(t):
	n = ""
	for i in range(t):
		n+=str(chr(i))
	return n
def dm(t):
	return [ord(x) for x in t]
def dm0(t):
	d=0
	for i in t:
		d+=ord(i)
	return d
t,s,f,m,k,md="",list_text(1114112),open(input("filename:"),"w"),dm0(str(input("input value:"))),dm0(str(input("input key:"))),int(input("input mod:"))
for i in str(open("input.txt","r").read()):
	t+=s[s.find(i)+k%md]
for i in dm(t):
	f.write(chr(i+m))
f.close()
