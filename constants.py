IGNORE_LINES = ['syntax = "proto3";', 'package main;']
VERSION_FILE = "version.txt"
PACKAGE = "models"
DEFAULT_BRANCH = "master"
OUTPUT_FOLDER = "output/"
DIST_FOLDER = "dist/"
PACKAGE_NAME = "model-services"
PACKAGE_META = """
setup(
    name='models-{%CHANNEL%}-{%BRANCH%}',
    version='{%VERSION%}',
    packages=['""" + str(PACKAGE) + """'],
    url='github.com/divyam-rai',
    license='ISC',
    author='Divyam Rai',
    author_email='mgmtdgr@gmail.com',
    description=''
)
"""