from setuptools import setup, find_packages
import codecs
import os


here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "package.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.6'
DESCRIPTION = 'An Unofficial Asynchronous Python version of Mdisk API wrapper'

# Setting up
setup(
    name="mdisky",
    version=VERSION,
    author="Kevin Nadar",
    license="MIT",
    author_email="jesikamaraj@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests',],
    url="https://github.com/kevinnadar22/mdisky",
    keywords=['python', 'mdisk', 'mdisk wrapper', 'mdisk convert', 'earn money '],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)