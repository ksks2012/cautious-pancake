#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup  # pylint: disable=import-error
from setuptools import find_packages

setup(name="bpsupport",
		version="0.0.1",
		description="A simple program for support bp",
		packages=find_packages(),
		install_requires=[
			"PyYaml >= 6.0, < 7.0",
			"requests >= 2.21.0, < 3.0.0",
			"beautifulsoup4 >= 4.12.2, < 5.0.0",
			"SQLAlchemy >= 2.0.36, < 2.1.0",
			"alembic >= 1.14.0, < 2.0.0",
			"pandas >= 2.2.3, < 3.0.0",
			"matplotlib >= 3.9.3, < 4.0.0",
			"seaborn >= 0.13.2, < 1.0.0",
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
