import sys
file_name = sys.argv[1]
fh = open (file_name, 'r')

print len(fh.readlines())

