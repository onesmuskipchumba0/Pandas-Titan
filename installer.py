import subprocess
packages=['pandas','rich','pyfiglet','openpyxl']
for package in packages:
	subprocess.check_call(['pip','install',package])
	