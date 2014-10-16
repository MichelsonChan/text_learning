# ============ #
# test_text.py #
# ============ #

# ====== #
# import #
# ====== #
import os
import TEXT
import numpy as np

os.system('rm *.vec')
os.system('rm *.sort')
os.system('rm *.np')

# ===================== #
# preprocess dictionary #
# no need to generate   #
# vector for dictionary #
# ===================== #
TEXT.PREPROCESS_DICT( 'dictionary' )
# ========================================= #
# all the file with names stored in         #
# "file" will be preprocessed and           #
# the following files will be generated     #
# .np          => stands for no punctuation #
# .np.sort     => sorted alphabetically     #
# .np.sort.vec => a numeric vector file     #
#                 indicating the frequency  #
#                 of occurance where the    #
#                 index corresponds to the  #
#                 dictionary                #
# ========================================= #
file = []
file.append( 'text.AlbertEinstein' )
file.append( 'text.AlexanderTheGreat' )
file.append( 'text.CPEBach' )
file.append( 'text.tropicalCyclone' )
file.append( 'text.IsaacNewton' )
file.append( 'text.JSBach' )
file.append( 'text.PhilipIIofMacedon' )
file.append( 'text.typhoon' )

# ============================= #
# preprocess + vector formation #
# ============================= #
WORDPROFILE = np.zeros( [ 69681 , len( file ) ] )
for i in range( 0 , len( file ) ) :
	fileName_prepro = TEXT.PREPROCESS( file[i] )
	print file[i] + " is preprocessed !"
	V = TEXT.FORMVECTOR( fileName_prepro , 'dictionary.np' )
	print "a vector file is generatd for " + fileName_prepro
	for k in range( 0 , V.size ) :
		WORDPROFILE[ k , i ] = V[ k ]
print WORDPROFILE

