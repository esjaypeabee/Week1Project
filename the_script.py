# take a bunch of files and sort them into directories based on 
# the first letter of the filename.
# 1: create 26 directories *** DONE ***
# 2: read the file names *** DONE ***
# 3: split off first letter
# 4: sort into appropriate directory

import os
import shutil

UPPERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWERS = 'abcdefghijklmnopqrstuvwxyz'
PATH = '~/Coding/Hackbright/Curriculum/Hackbright-Curriculum/Week_1_Project/'

def create_directories():

	for c in LOWERS:
		os.mkdir(c)


def get_filenames():

	file_list = []
	for f in os.listdir('original_files'):
		file_list = file_list + [f]
	return file_list

def sort_files(file_list):

	source = 'original_files'

	for f in file_list:
		letter = f[0]
		if f[-3:] == 'txt':
			shutil.move('original_files/'+f, letter)



# create_directories()
filenames = get_filenames()
sort_files(filenames)
# print filenames[:10]
