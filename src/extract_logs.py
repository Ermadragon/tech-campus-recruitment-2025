import sys

def LogEntries(sys.argv[1]):
	date = sys.argv[1]
	with open('test_logs.log', 'r') as file:
		lines = file.readlines()
	f = open("output/output_YYYY-MM-DD.txt", "a")
	for line in lines:
		if line[:10] == date:
			print(line, file=f)
    f.close()



