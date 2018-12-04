import os
list_dir = os.listdir('/var/log')

for f_name in list_dir:
	
	if os.path.isfile('/var/log/%s'%f_name) == True:
	 		
		if (os.stat('/var/log/%s'%f_name).st_size) >= 20:
			print(f_name)
 
