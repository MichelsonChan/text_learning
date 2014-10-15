# ======= #
# TEXT.py #
# ======= #

# ====== #
# import #
# ====== #
import os
import string

# ==================== #
# functions definition #
# ==================== #

def PREPROCESS( inputTextFileNameStr ) :
	# ============================================ #
	# Part I : punctuation removal & vectorization #
	# ============================================ #
	outputTextFileNameStr = inputTextFileNameStr + ".np"
        # ----------------------- #
        # check file availability #
        # ----------------------- #
        if not os.path.isfile(  inputTextFileNameStr ) :
                print "Error @ TEXT.PREPROCESS() :"
                print inputTextFileNameStr  + " is not found !"
                print "Error exit."
                return
        if     os.path.isfile( outputTextFileNameStr ) :
                print "Error @ TEXT.PREPROCESS() :"
                print outputTextFileNameStr + " already exists !"
                print "Do you want to overwrite it ? [ y / n ]"
                userReply = raw_input()
                if userReply == 'n' :
                        return
                else :
                        os.remove( outputTextFileNameStr )
	# -------------------- #
        # read input text file #
        # -------------------- #
        fileObject = open(  inputTextFileNameStr , 'r' )
        inputStr   = fileObject.read()
        fileObject.close()
        # ------------------- #
        # punctuation removal #
        # ------------------- #
        strTransLogic = ''.join( chr(c) if chr(c).isupper() or chr(c).islower() else '\n' for c in range(256) )
        outputStr     = inputStr.translate( strTransLogic )
        outputStr     = outputStr.lower()
	# ---------------------------- #
	# export punctuation free file #
	# ---------------------------- #
	fileObject = open( outputTextFileNameStr , 'w' )
	fileObject.write( outputStr )
	fileObject.close()
	# ======================================================== #
	# Part II : sort the vectorized punctuation-free text file #
	# ======================================================== #
	inputTextFileNameStr  = outputTextFileNameStr
	outputTextFileNameStr =  inputTextFileNameStr + '.sort'
        # ----------------------- #
        # check file availability #
        # ----------------------- #
        if not os.path.isfile(  inputTextFileNameStr ) :
                print "Error @ TEXT.PREPROCESS() :"
                print inputTextFileNameStr  + " is not found !"
                print "Error exit."
                return
        if     os.path.isfile( outputTextFileNameStr ) :
                print "Error @ TEXT.PREPROCESS() :"
                print outputTextFileNameStr + " already exists !"
                print "Do you want to overwrite it ? [ y / n ]"
                userReply = raw_input()
                if userReply == 'n' :
                        return
                else :
                        os.remove( outputTextFileNameStr )
	# ----------------- #
	# alphabetical sort #
	# ----------------- #
	fileObject       = open( inputTextFileNameStr  , 'r' )
	lines            = fileObject.readlines()
	lines.sort()
	fileObject.close()
	# ============================= #
	# Part III: empty lines removal #
	# ============================= #
	lines_noEmptyLine = []
	for line in lines :
		if not line.strip() :
			continue
		else :
			lines_noEmptyLine.append( line )
	sortedFileObject = open( outputTextFileNameStr , 'w' )
	sortedFileObject.writelines( lines_noEmptyLine )
	sortedFileObject.close()
	# ====== #
	# finish #
	# ====== #
	return outputTextFileNameStr


def WORD2NUM( inputTextFileNameStr ) :
	# ==================================== #
	# this function convert the English    #
	# words in a vectorized text file      #
	# into numbers with a purpose for      #
	# easy and convenient dicionary search #
	# e.g. apple  becomes 1.16.16.12.5     #
	# e.g. banana becomes 3.1.14.1.14.1    #
	# lastly this function will generate a #
	# file named fileNameStr.w2n as output #
	# ==================================== #
	outputTextFileNameStr = inputTextFileNameStr + ".w2n"
	# ======================= #
	# check file availability #
	# ======================= #
	if not os.path.isfile( inputTextFileNameStr ) :
		print "Error @ DSP.WORD2NUM() :"
		print inputTextFileNameStr  + " is not found !"
		print "Error exit."
		return
	if     os.path.isfile( outputTextFileNameStr ) :
		print "Error @ DSP.WORD2NUM() :"
		print outputTextFileNameStr + " already exists !"
        	print "Do you want to overwrite it ? [ y / n ]"
        	userReply = raw_input()
        	if userReply == 'n' :
        		return
        	else :
        		os.remove( outputTextFileNameStr )
	# ==================== #
	# read input text file #
	# ==================== #
	fileObject = open(  inputTextFileNameStr , 'r' )
	inputStr   = fileObject.read().lower()
	fileObject.close()
	# ============== #
	# transformation #
	# ============== #
	inputStr = inputStr.replace( 'a'   , '.0'  )
	inputStr = inputStr.replace( 'b'   , '.1'  )
	inputStr = inputStr.replace( 'c'   , '.2'  )
	inputStr = inputStr.replace( 'd'   , '.3'  )
	inputStr = inputStr.replace( 'e'   , '.4'  )
	inputStr = inputStr.replace( 'f'   , '.5'  )
	inputStr = inputStr.replace( 'g'   , '.6'  )
	inputStr = inputStr.replace( 'h'   , '.7'  )
	inputStr = inputStr.replace( 'i'   , '.8'  )
	inputStr = inputStr.replace( 'j'   , '.9'  )
	inputStr = inputStr.replace( 'k'   , '.10' )
	inputStr = inputStr.replace( 'l'   , '.11' )
	inputStr = inputStr.replace( 'm'   , '.12' )
	inputStr = inputStr.replace( 'n'   , '.13' )
	inputStr = inputStr.replace( 'o'   , '.14' )
	inputStr = inputStr.replace( 'p'   , '.15' )
	inputStr = inputStr.replace( 'q'   , '.16' )
	inputStr = inputStr.replace( 'r'   , '.17' )
	inputStr = inputStr.replace( 's'   , '.18' )
        inputStr = inputStr.replace( 't'   , '.19' )
        inputStr = inputStr.replace( 'u'   , '.20' )
        inputStr = inputStr.replace( 'v'   , '.21' )
        inputStr = inputStr.replace( 'w'   , '.22' )
        inputStr = inputStr.replace( 'x'   , '.23' )
        inputStr = inputStr.replace( 'y'   , '.24' )
        inputStr = inputStr.replace( 'z'   , '.25' )
	inputStr = inputStr.replace( '\n.' , '\n'  )
	# ====================================== #
	# handle the first '.' in the first line #
	# ====================================== #
	inputStr = inputStr.replace( '.'   , '', 1 )
	# ====================== #
	# write output text file #
	# ====================== #
	fileObject = open( outputTextFileNameStr , 'w' )
	fileObject.write( inputStr )
	fileObject.close()
	# ====== #
	# finish #
	# ====== #
	return outputTextFileNameStr

