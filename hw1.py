lines = []
while True:
	s = input()
	if s:
		lines.append(s.upper())
	else:
		break
for line in lines:
	print(line)