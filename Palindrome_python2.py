#! /usr/bin/env python 
#python 2

"""
	A simple module for testing the isPalindrome(string) code.
"""


import string

def isPalindrome_Jaysen(s):
    s = s.upper()
    s = s.translate(
        string.maketrans("", ""), string.punctuation + string.whitespace)
    return s == s[::-1]

def isPalindrome_Storz(s):
	upcase = s.upper()
	newString = ''.join(e for e in upcase if e.isalnum())
	# I found this example on stackoverflow.com
	# it iterates through each element of the now uppercase string and only keeps letters and numbers
	return newString == newString[::-1]

def isPalindrome_PhillipAdkins(s):
		return s == s[::-1]

# import string    # already imported above

def isPalindrome_Dmitry(s):
    s = s.upper()
    s = ''.join(e for e in s if e.isalnum())

    length = len(s)
    half = (length / 2)

    if (length % 2 == 0):
        return s[:half - 1] == s[:half:-1]
    else:
        return s[:half] + s[half + 1] == s[:half:-1] + s[half + 1]

def runTests():

	"""
		setup some test sentences and run them against isPalindrome(string)
	"""

	sentenceList = [
		"Sore was I ere I saw Eros.",
		"This is not a Palindrome!",
		"A man, a plan, a canal -- Panama",
		"Never a foot too far, even.",
		"Euston saw I was not Sue.",
		"Live on evasions? No, I save no evil.",
		"Red Roses run no risk, sir, on nurses order.",
		"Salisbury moor, sir, is roomy. Rub Silas.",
		'''Marge, let's "went." I await news telegram.''',
		"A new order began, a more Roman age bred Rowena.",
		"I, man, am regal; a German am I.",
		"Tracy, no panic in a pony-cart.",
		"Egad! Loretta has Adams as mad as a hatter. Old age!",
		"Eve, mad Adam, Eve!",
		"Resume so pacific a pose, muser.",
		"Marge let a moody baby doom a telegram.",
		"Tenet C is a basis, a basic tenet.",
		'''Nella's simple hymn: "I attain my help, Miss Allen."''',
		"Straw? No, too stupid a fad. I put soot on warts.",
		"Sir, I demand, I am a maid named Iris.",
		"Lay a wallaby baby ball away, Al.",
		"Tessa's in Italy, Latin is asset.",
		"Noel sees Leon.",
		]

	print()
	print("Start of Proposal by Conrad Storz...")
	for candidate in sentenceList:
		print("    " + str(isPalindrome_Storz(candidate)) + "[" + candidate + "] {is a palindrome} ")

	print()
	print("Start of Proposal by Jaysen...")
	for candidate in sentenceList:
		print("    " + str(isPalindrome_Jaysen(candidate)) + "[" + candidate + "] {is a palindrome} ")

	print()
	print("Start of Proposal by Phillip Adkins...")
	for candidate in sentenceList:
		print("    " + str(isPalindrome_PhillipAdkins(candidate)) + "[" + candidate + "] {is a palindrome} ")

	print()
	print("Start of Proposal by Dmitry Kreslavskiy...")
	for candidate in sentenceList:
		print("    " + str(isPalindrome_Dmitry(candidate)) + "[" + candidate + "] {is a palindrome} ")

#
# boilerplate for running built-in test suite when this module is run at the commandline.
if __name__ == "__main__":
	print("Starting tests....")
	runTests()



