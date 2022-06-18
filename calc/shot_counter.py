
import os


datadir = 'E:\\Data\\Tuneout\\to_main_data'

num_forc = 0

for subdir in os.scandir(datadir):
	if subdir.is_dir():
		print('In folder: ',subdir.name)
		contents = os.scandir(os.path.join(datadir,subdir))
		# objnames = list([o.name for o in contents])
		files = list([f for f in contents if f.is_file()])
		print('  There are %u files '%(len(files)))
		numtxt = [f for f in files if f.name[-3:]=='txt']
		print('  Of which %u are .txt '%(len(numtxt)))
		forc_files = [f for f in files if 'forc' in f.name]
		print('  and %u are _forc '%(len(forc_files)))
		num_forc += len(forc_files)


# dirs = os.listdir(datadir)

# for this_dir in dirs:
# 	working_dir = os.path.join(datadir,this_dir)
	
# 	allfiles = os.listdir

print('Done. Found %u _forc files'%(num_forc))
