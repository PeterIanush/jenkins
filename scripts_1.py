from datetime import datetime
import commands

datetime_now = datetime.now()
uptime = commands.getoutput('uptime')
logged_users = commands.getoutput('who')
write_file = open('scripts_1.log', 'w')
write_file.write(str(datetime_now))
write_file.write(uptime)
write_file.write(logged_users)
write_file.close()
print "date and time: %s" % datetime_now
print "system uptime: %s" % uptime 
print "logged-in users: %s" % logged_users

