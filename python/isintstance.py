L1 = ['asdf', 'Wkd', 'saHJ', 18]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
for n in L2:
	print(n)