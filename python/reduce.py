from functools import reduce
def xy(x,y):
	return x*10 + y
def charts(s):
	charts = {'1':1,'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0, '.':'.'}
	return charts[s]
def toint(s):
	return reduce(xy,map(charts,s))1
#a = input('请输入一串数字')
#print('转换成数字:', isinstance(toint(a),int))
#lambda和reduce结合转换
def prod(L):
	return reduce(lambda x,y:x*y, L)
L = [1, 3, 5, 7, 9]
#print('L内部积', prod(L))
def floatxy(x,y):
	pass
def str2float(s):
	n = s.index('.')
	s1 = map(int,s[:n])
	s2 = list(map(int,s[n+1:]))
	return reduce(xy,s1)+(reduce(xy,s2)/10**len(s2))
b = input('请输入一串浮点型数字:')
print(str2float(b))