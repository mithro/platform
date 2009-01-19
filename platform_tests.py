
class PlatformDistroTests():

	def distrocodename(file):
		file = os.path.basename(file)
		return file.split('-', 3)

	def patchopen(target, replacement):
		def opentestfile(filename):
			assert filename == target
			return real_open(replacement)
		__builtins__["open"] = opentestfile

	def TestWithUbuntuLSBFile():
		"""Test that the platform module detects the correct distro given all
		   the /etc/lsb-release files we have.
		"""

		real_open = __builtins__["open"]
		try:
			for testfilename in os.listdir("tests/*-lsb-release"):
				patchopen("/etc/lsb-release", testfilename)
				testdistro, testcodename, target = self.distrocodename()

				assert platform.distro() == testdistro 
				assert platform.codename() == testdistro 
		finally:
			__builtins__["open"] = real_open

	def TestWithIssue():
		"""Test that the platform module detects the correct distro given an
		   unmodified issues file. This is a last resort detection method.
		"""

		real_open = __builtins__["open"]
		real_exists = os.path.exists
		
		def exists(filename):
			return filename == "/etc/issue"
		os.path.exists = exists

		try:
			for testfilename in os.listdir("tests/*-issue"):
				patchopen("/etc/issue", testfilename)
				testdistro, testcodename, target = self.distrocodename()
				
				assert platform.distro() == testdistro 
				assert platform.codename() == testdistro 
		finally:
			__builtins__["open"] = real_open
			os.path.exists = real_exists

