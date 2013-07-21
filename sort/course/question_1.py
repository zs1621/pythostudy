import sys 
import globalsed
if not "/home/zh/git/python/sort/" in sys.path:
	sys.path.append("/home/zh/git/python/sort/")
import merge_sort

def open_txt():
	try:
		infile = file('interArray.txt', 'r')
		for x in infile.readlines():
			passlist.append(x)
		infile.close()
	except:
		return 0
globalsed.init()
passlist = []
open_txt()
#print len(passlist)
#passlist = [3,6,2,4,8]
merge_sort.sort(passlist, 0, len(passlist))
print("chang", globalsed.inter)


