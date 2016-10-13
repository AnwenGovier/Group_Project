#import the users input so that it can be normalied
import string

#this contains all of the words that can be removed from the sting that has been imported such as 'like' or 'please'
unimportant_words = ['a', 'about', 'all', 'an', 'any', 'at', 'bad', 'bag', 'better', 'big', 'can',
					 'cannot', 'every', 'for', 'fall', 'from', 'good', 'have', 'her', 'here', 'his'
					 'hostage', 'how', 'hello', 'i', 'in', 'into', 'is', 'it', 'large', 'little', 
					 'me', 'main', 'my', 'the', 'on', 'of', 'off', 'please', 'room', 'small', 'some',
					 'that', 'the', 'then', 'this', 'those', 'through', 'to', 'until', 'us', 'we', 'want', 
					 'when', 'wish', '0', '1', '2', '3', '4', '5', '6',  '7', '8', '9']


def user_input_normalisation(user_input):
	"""
	The following function will remove all of the unwanted punctuation from the users input. 
	It will then split the string into individual words that will be put through a function that will
	remove all of the unwanted words to leave behind a command for the program to follow.
	The unwanted words can be found in the unimportant_words 
	
	>>> user_input_normalisation("    Please Go! south")
	['go', 'south']
	>>> user_input_normalisation("PLEASE TAKE THE GuN please..?")
	['take', 'gun']
	>>> user_input_normalisation("can i drop my ammo here! please! !in this room")
	['drop', 'ammo']
	>>> user_input_normalisation("!!!!!!!CAN I HAVE HELP PLEASE!!!!!!")
	['help']
	"""
	remove_punctuation = remove_input_punctuation(user_input).lower().strip()
	words = remove_punctuation.split()
	return remove_unimportant_words(words, unimportant_words)

def remove_unimportant_words(words, unimportant_words):
	"""this function will remove all of the umimportant words for the string and replace them with ""
	It will return all of the remaining words in a new string that will be used as an input in other functions.
	e.g.

	>>> remove_unimportant_words(["go", "north", "to", "the", "kitchen"], ["to", "the", "kitchen"])
	['go', 'north']
	>>> remove_unimportant_words(["please", "drop", "the", "first", "aid", "kit"], unimportant_words)
	['drop', 'first', 'aid', 'kit']
	>>> remove_unimportant_words(["can", "i", "go", "west", "to", "room", "4"], unimportant_words)
	['go', 'west']
	>>> remove_unimportant_words(["please", "kill", "the", "man", "for", "me"], unimportant_words)
	['kill', 'man']
	"""
	kept_words = [];
	for word in words:
			if word not in unimportant_words:
				kept_words.append(word)
	return kept_words

def remove_input_punctuation(text):
	"""	this function will remove all the punctuation in the string.
	All of the spaces should be kept in place as they are not punctuation. 
	The function should go through each character and replace punctuation with a blank space.
	It should return a new string to the user that will contain only characters and white space
	>>> remove_input_punctuation("take, gun!!!")
	'take gun'
	>>> remove_input_punctuation("go-- s!ou?th!")
	'go south'
	>>> remove_input_punctuation("!!!h!e?l!p!!")
	'help'
	>>> remove_input_punctuation("Please!!!   !take--- the ??ammo")
	'Please   take the ammo'
	"""
	no_punctuation = ""
	for char in text:
		if not (char in string.punctuation):
			no_punctuation= no_punctuation + char
	return no_punctuation
