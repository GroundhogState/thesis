import os
import regex as re
import copy


# # Capitalizes bib keys in .bib file
# bibfile = 'bibliography.bib'
# bibwork = open(bibfile,'r',encoding='Latin1')
# newbib = open('newbib.bib','w',encoding = 'Latin1')
# # Let's find the articles
# pattern = "@"

# at_lines = []
# for [idx,line] in enumerate(bibwork):
# 	instances = re.search("@",line)
# 	if instances:
# 		# edit the line
# 		newline = '%s'%line
# 		bracket = re.search("{",line)
# 		bloc=bracket.start()
# 		oldchar = line[bloc+1]
# 		newline = line[:bloc+1]+oldchar.upper()+line[bloc+2:]
# 	else:
# 		newline = line
# 	# print(newline)
# 	newbib.write(newline)

# # for line_key in at_lines:
# 	# bracket =  re.search("{",bibwork[line_key])
# 	# print(bracket.start())


# print('Found %u article headers:'%len(at_lines))
# print(at_lines)
# print(' = Done =')

# # Capitalizes bib keys in main text

# get all the tex files
texfiles = os.listdir(os.getcwd())
texfiles =[f for f in texfiles if f[-3:]=='tex']
print(texfiles)
for [idx,target_file] in enumerate(texfiles):
# target_file = '12_apparatus.tex'
	work_text = open(target_file,'r')
	# for line in target_file:
	lines = work_text.readlines()
	newlines = []
	for line in  lines:
	# test_text = "In some work \cite{ab11}, things worked. In others, they did not \cite{d12,ca15,q}, but they tried \cite{d12}"
		temp_text = line
		citations = re.findall("cite{[^}]+}",temp_text)
		if len(citations)>0:
			print('In the line:')
			print(' '+temp_text)
			print('Citations found:')
			print(citations)
			print('Updated citations to:')
			new_cites = []
			key_changes = {}
			for citation in citations:
				keys = re.split("[{,]",citation[:-1])
				# first entry will be 'cite' so ignore it
				new_cite = "cite{"
				for key in keys[1:]:
					new_key = key[0].upper() + key[1:]
					new_cite = new_cite + new_key + ","
					key_changes[key] = new_key
				# trim the last comma
				new_cite = new_cite[:-1] + "}"
				new_cites.append(new_cite)

			for key in key_changes:
				print(' '+key + " -> " +key_changes[key])

			# temp_text = copy.copy(test_text)
			for key in key_changes:
				instances=re.findall(key,temp_text)
				num_uses = len(instances)
				# print(key + ' used ' +'%u'%num_uses + ' times')
				(temp_text,_) = re.subn(key,key_changes[key],temp_text,count=num_uses)
			print('Updated text to:')
			print(' ' + temp_text)
		newlines.append(temp_text)

	work_text.close()
	with open(target_file,'w') as tf:
		tf.writelines(newlines)
	tf.close()
	print('DONE file %u/%u'%(idx,len(texfiles)))