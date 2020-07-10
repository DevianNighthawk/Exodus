import os
import re


def file_exists(filepath):
	ret=os.path.isfile(filepath)
	return ret




filepath='forgotten.txt'
print(file_exists(filepath))
