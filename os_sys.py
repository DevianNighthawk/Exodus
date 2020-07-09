

import os
import re

def find_file_extension(extension,file_list):
	search_expression="*."+extension.lower()
	matches=[]
	for file in file_list:
		x=re.search(search_expression,file)
		if x:
			matches.append(file)
	return matches




directory_contents=os.listdir()
print(directory_contents)
