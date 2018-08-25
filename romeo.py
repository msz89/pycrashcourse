import os


fn = os.path.join("labs", "play.txt")
print(fn)
f = open(fn,"r")

split_words = f.read().split(" ")
# print(split_words)

ULIST = list()

for word in split_words:
	if word not in ULIST:
		ULIST.append(word)

print(ULIST)
print(len(ULIST))