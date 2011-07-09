import os
import random
import sys

#Created using an idea from Nick Parlante's Google Python Class
#http://code.google.com/edu/languages/google-python-class/
#mimic.py problem

#builds dictionary(hash) of words from files in provided directory (dirname)
def buildWordDict(dirname):
	wordDict = {}
	for file in os.listdir(dirname):
		if file.split('.')[1] == 'txt':
			
			#parse lines in file
			openFile = open(os.path.join(dirname, file), 'r')
			text = openFile.read()
			openFile.close()
			words = text.split()
			prevWord = ''
			for curWord in words:
				if not prevWord in wordDict:
					wordDict[prevWord] = [curWord]
				else:
					wordDict[prevWord].append(curWord)
				prevWord = curWord
	return wordDict
	
#builds song from dict, using startword, and generates numWords in length
def buildText(wordDict, startWord, numWords):
	punctuation = [',','.','?','!',';',':']
	text = ''
	
	#use  empty if startWord not in dict
	if startWord not in wordDict:
		word = ''
	else:
		word = startWord
	
	#loop through numberOfWords etc
	for i in range(numWords):
		text  += word + ' '
		nextWord = wordDict.get(word)
		
		if not nextWord:
			nextWord = wordDict['']
		word = random.choice(nextWord)
		
		#check to add newline after punctuation
		if word[-1] in punctuation:
			if i != (numWords-1) :
				word+='\n'
	
	#loop through words until you end with punctation
	#should help last sentence end more coherently
	while word[-1] not in punctuation:
		text += word + ' '
		
		nextWord = wordDict.get(word)
		
		if not nextWord:
			nextWord = wordDict['']
		word = random.choice(nextWord)
		
	text += word
	return text

#TODO: writes file appends # if name is taken	
def writeFile(text, filename):
	outFile = open(filename, 'a')
	outFile.write(text)
	outFile.close()		

	
#supply the values to get the program started
def main():
	songLength = 250
	wordDict = buildWordDict('lyrics')
	#use random word from dict as start word
	text = buildText(wordDict, random.choice(wordDict.keys()), songLength)
	writeFile(text, 'yoursong.txt')
					
if __name__ == "__main__":
	main()