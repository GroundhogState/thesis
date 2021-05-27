# A short script to regex your way to a nice compiled todo list anywhere in your document.
# Reads all .tex files in tex_directory (default latex/) and collects \todo{}
# Then writes all items to a bullet list mtodo.tex.
# 
# Usage: 
	# To collate list: python ctodo.py [opt:tex_directory]
	# To present in pdf: add \include{tex_directory/mtodo} in main.tex
# Possible improvements:
	# * Doesn't like multiline todo items or a \todo that 
	# contains another envt (like a list or table)
	# * Could bundle items by the file they live in and print in separate lists
	# * Platinum version: Each master todo is a href to the appropriate location tex
	# and safely removes them once the todo list is done!!!

import sys
import os
import re
import datetime

datestring = str(datetime.datetime.now())[:10].replace('-','')

if len(sys.argv) == 1:
	texdir = 'latex'
else:
	texdir = sys.argv[1]
target_dir = os.path.join(os.getcwd(),texdir)
the_files = [f for f in  os.listdir(target_dir) if ".tex" in f and "mtodo" not in f]
with open(os.path.join(texdir,'mtodo.tex'),'w') as texout:
	texout.write("To-do list:\\newline\n")
	for f in the_files:
		todolist = []
		fullfile = os.path.join(os.getcwd(),texdir,f)
		with open(fullfile) as thisfile:
				text = thisfile.read()
				todolist = re.findall(r'\\todo{.*?}',text,flags=re.I)
				if len(todolist)>0:
					strip_items = [item[6:-1] for item in todolist]
					if len(strip_items)>0:
						texout.write('In \\verb|{%s}|:\n'%f)
						texout.write("\\begin{itemize}\n")
						for item in strip_items:
								texout.write("\\item {%s}\n"%item)
						texout.write("\\end{itemize}\n")
	texout.close()
# write to text file for easy check-boxing
with open('todo_%s.md'%datestring,'w') as mdout:
	mdout.write("To-do list:\n")
	for f in the_files:
		todolist = []
		fullfile = os.path.join(os.getcwd(),texdir,f)
		with open(fullfile) as thisfile:
				text = thisfile.read()
				todolist = re.findall(r'\\todo{.*?}',text,flags=re.I)
				if len(todolist)>0:
					strip_items = [item[6:-1] for item in todolist]
					if len(strip_items)>0:
						mdout.write('# %s\n'%f)
						# texout.write("\\begin{itemize}\n")
						for item in strip_items:
								mdout.write("\t[] %s\n"%item)
						# texout.write("\\end{itemize}\n")
	mdout.close()

print('To-do list compiled')
