#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup  # pylint: disable=import-error
from setuptools import find_packages

setup(name="bpsupport",
		version="0.0.1",
		description="A simple program for support bp",
		packages=find_packages(),
		install_requires=[
			"PyYaml >= 6.0",
            "requests >= 2.21.0",
            "beautifulsoup4 >= 4.12.2"
		],
		entry_points={
				'console_scripts': [
						'out_to_csv = bpsupport.cmd.out_to_csv:main',
				],
		},
		classifiers=[
				"Development Status :: 3 - Alpha",
				"Intended Audience :: Developers",
				"Operating System :: POSIX",
				"Programming Language :: Python :: 3.10.6",
		],
		)

# vim: tabstop=4 shiftwidth=4
