import commands

du = commands.getoutput('df -hT /')
size = du.split(' ')[-2].replace("%", "")

print int(size)
if int(size) >=90:
	print 'alarm' #TODO:"make code to send email for admin"
