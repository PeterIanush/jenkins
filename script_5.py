import commands

print commands.getoutput('ps -eo pmem,cmd | sort -k 1 -nr | head -5')
