#!/usr/bin/env python

import sys

from setuptools import setup

setup(
	name		="platform",
	version		="0.0.1",
	license		="LGPL",
	description	="Library for detecting the extact platform python is running on.",
	long_description="""\
A library for detecting the exact platform. This includes:
 * platform - Linux, FreeBSD, Windows, etc
 * distro - Ubuntu, Debian, gentoo, etc
 * release - Hardy, Gusty, Lenny, etc
""",
	author		="Tim Ansell",
	author_email="mithro@mithis.com",
	url			="http://www.mithis.com/~tim/platforms",
	keywords	="platform detection release distro",

	namespace_packages = ['platform'],
	packages=[ \
		'platform',
	],
	zip_safe=True,
)
