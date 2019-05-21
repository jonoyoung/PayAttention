import shutil
import os

# Whether we should exit the program boolean.
exitProgram = False

# Colours class for terminal colours.
class colours:
	HEADER = '\033[95m'
	ERROR = '\033[91m'
	INFO = '\033[94m'
	WARNING = '\033[93m'
	GREEN = '\033[92m'
	STANDARD = '\033[0m'

# On first run of this program create a backup of the /etc/hosts file in case it gets corrupted.
backupFilename = "/etc/hosts.backup"
if not os.path.exists(backupFilename):
	shutil.copyfile('/etc/hosts', backupFilename)

# Print statements and pre-prepared strings.
headerText = colours.HEADER + "\n[PayAttention]" + colours.STANDARD
errorText = colours.ERROR + "[Error] " + colours.STANDARD
infoText = colours.INFO + "[Info] " + colours.STANDARD
menuText = "[1: Add Sites]  [2: Remove Sites]  [3: Add a Site]  [4: Remove a Site]  [5: List Blocked Sites]  [0: Exit Program]"
print(headerText)

# Add all sites in the 'sites.txt' file.
def addSites():
	try:
		sites = open('sites.txt', 'r')
		sitesContents = sites.readlines()
		sites.close()

		hostsFile = open("/etc/hosts", "a")
		for line in sitesContents:
			hostsFile.write("0.0.0.0 " + line + "\n")

		hostsFile.close()
	except IOError:
		print(errorText + "You need to run this program as super user. Retry with 'sudo python PayAttention.py'.")

# Remove all sites added by this program.
def removeSites():
	try:
		with open(backupFilename, "r") as backupFile:
			lines = backupFile.readlines()
		with open("/etc/hosts", "w") as hostsFile:
			hostsFile.writelines(lines)

	finally:
		backupFile.close()
		hostsFile.close()


# Add a specific site.
def addSite():
	print("\n" + colours.ERROR + "[IMPORTANT]" + colours.STANDARD + " Please make sure that you include the domain name extension. E.g: youtube.com")
	userInput = input("[3: Add a Site] Please enter the name of the site you would like to block: ")
	
	try:
		with open("/etc/hosts", "a") as hostsFile:
			hostsFile.write("0.0.0.0 " + userInput + "\n")
			hostsFile.write("0.0.0.0 www." + userInput + "\n")
	finally:
		hostsFile.close()

# Remove a specific site.
def removeSite():
	found = False
	print("\n" + colours.ERROR + "[IMPORTANT]" + colours.STANDARD + " Please enter the domain name and extension. E.g: facebook.com")
	userInput = input("[4: Remove a Site] Please enter the name of the site you would like to unblock: ")

	try:
		with open("/etc/hosts", "r") as readHosts:
			lines = readHosts.readlines()
		with open("/etc/hosts", "w") as writeHosts:
			for line in lines:
				if not userInput in line:
					writeHosts.write(line)
				elif userInput in line:
					found = True
	finally:
		readHosts.close()
		writeHosts.close()

	if (not found):
		print("Could not find that domain, please try again.")

# List all sites currently blocked.
def listBlockedSites():
	try:
		with open("/etc/hosts", "r") as readHosts:
			for line in readHosts.readlines():
				if "0.0.0.0" in line:
					print(line.strip("\n"))
	finally:
		readHosts.close()

# Get the users input and use the appropriate function.
while (not exitProgram):
	print("\n\n" + menuText)
	userInput = int(input("[Input] Please enter the number corresponding to the option you would like: "))

	if (userInput == 1):
		addSites()
	elif (userInput == 2):
		removeSites()
	elif (userInput == 3):
		addSite()
	elif (userInput == 4):
		removeSite()
	elif (userInput == 5):
		listBlockedSites()
	else:
		exitProgram = True
		print(colours.ERROR + "[Exit] " + colours.STANDARD + "Thank you for using this program.")