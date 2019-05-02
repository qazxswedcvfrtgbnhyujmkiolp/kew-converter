# Need some way to get configuration data around

import io
import os

def get_prop(prop):
	try: 
		confFile = open("../conf/" + prop, 'r')
		val = confFile.read()
		confFile.close()
		return(val)
	except:
		return(0)
		
def set_prop(prop, val):
	confFile = build_config_file(prop)
	confFile.write(val)
	confFile.close()

def check_prop_exists(prop):
	try:
		if (os.file.exists("../conf/" + prop)):
			return True
		else: return False
	except:
		return False

def build_config_file(name):
	if (not os.directory.exists("../conf")): os.system("mkdir ../conf")
	os.system("touch ../conf/" + name)
	return open("../conf/" + name, 'w')
