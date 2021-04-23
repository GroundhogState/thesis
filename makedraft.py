import os
import sys
import datetime
import argparse

# get current datestamp string
# Run pdflatex/bibtex/pdflatex/pdflatex 
# Save in drafts/datestamp/etc
# Include the mtodo
# Update a word count somehow??? Possibly other stats - page num, etc

p = argparse.ArgumentParser()
p.add_argument('-f',nargs = '?',default='main', const = 'main')
p.add_argument('-b',nargs = '?',default=True, const = True)
p.add_argument('-t',nargs = '?',default='draft', const = 'draft')
p.add_argument('-r',nargs = '?',default=False, const = False)
args = p.parse_args()
fname_in = args.f
recompile_bib = args.b
fname_out = args.t
refresh = args.r
datestring = str(datetime.datetime.now())[:10].replace('-','')

os.system('py ctodo.py')

# compilecommand = 'pdflatex {fin} -jobname=drafts/{fin}/{datestr}/{datestr}_{fout}'.format(datestr=datestring,fin=fname_in,fout = fname_out)
jobname = 'drafts/{datestr}/{datestr}_{fin}_{fout}'.format(datestr=datestring,fin=fname_in,fout = fname_out)
compilecommand = 'pdflatex {fin} -jobname={jobname}'.format(fin=fname_in,jobname=jobname)
if refresh:
	print('Deleting old draft!')
	os.system('rm -rf drafts/{fin}/{datestr}'.format(datestr=datestring,fin=fname_in))
print('Compile command: ',compilecommand)
os.system(compilecommand)
if recompile_bib==True:
	print('Recompiling bib from aux file...')
	bibcommand = 'biber {fin}'.format(fin=jobname)
	os.system(bibcommand)
	print('Recompiling PDF...')
	os.system(compilecommand)
	os.system(compilecommand)
os.system('start "" {jobname}.pdf'.format(jobname=jobname))