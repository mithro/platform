
LSB_RELEASE = "/etc/lsb-release"
DISTROS = {
	"Ubuntu"      : "/etc/lsb-release",
	"Debian"      : "/etc/debian_version",
	"RedHat"      : "/etc/redhat-release",
	"SUSE"        : "/etc/SUSE-release",
	"Fedora"      : "/etc/fedora-release",
	"Gentoo"      : "/etc/gentoo-release",
	"Slackware"   : "/etc/slackware-version",
	"Mandriva"    : "/etc/mandriva-release",
	"Mandrake"    : "/etc/mandrake-release",
	"YellowDog"   : "/etc/yellowdog-release",
	"SUN JDS"     : "/etc/sun-release",
	"UnitedLinux" : "/etc/UnitedLinux-release"
}

DISTROS_TOOL = {
	'apt' : ["Ubuntu", "Debian"],
	'rpm' : ["RedHat", "SUSE", "Fedora", "Gentoo", "Mandriva", "Mandrake", "YellowDog"],
	'emerge' : ["Gentoo"],
}

def distro():
	# Lets first as LSB
	if os.path.exists(LSB_RELEASE):
		values = open(LSB_RELEASE).readlines()
		for value in values:
			if value.startswith("DISTRIB_ID"):
				return value.split("=")[-1]
	
	# Check for various Release files
	for name,location in DISTROS.iteritems():
		if os.path.exists(location):
			return name

	# This only works on a system which does not have a modified issue file.
	issueFile = open("/etc/issue","r")
	issue = issueFile.readline()
	qname = issue.split()
	return qname[0]

def packager():
	distro = distro()
	for tool, distros in DISTRO_TOOLS.iteritems():
		if distro in distros:
			# Check that the tool actually exists...
			
			return tool
	return None

