from setuptools import setup, find_packages

__version__ = 0.1

setup(
	name="textify",
	version=__version__,
	author="Quin Marilyn",
	author_email="quin.marilyn05@gmail.com",
	description="Library to get text from many popular document types.",
	long_description="# textify\n\nPython library to convert many common document types to plane text.",
	long_description_content_type="text/markdown",
	url="http://github.com/accessware/textify",
	packages=find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		"Development Status :: 3 - Alpha",
	],
	python_requires=">=3",
)
