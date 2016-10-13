#import the users input so that it can be normalied
import string

#this contains all of the words that can be removed from the sting that has been imported such as 'like' or 'please'
unimportant_words = []

def user_input_normalisation(user_input)
"""
The following function will remove all of the unwanted punctuation from the users input. 
It will then split the string into individual words that will be put through a function that will
remove all of the unwanted words to leave behind a command for the program to follow.
The unwanted words can be found in the unimportant_words []

>>>user_input_normalisation(["    Please Go! SOUTH")
	['go', 'south']

>>>user_input_normalisation(["PLEASE TAKE THE GuN please..?")
	['take', 'gun']	

>>>user_input_normalisation(["can i drop my ammo here! please! !in this room")
	['drop', 'ammo']

>>>user_input_normalisation(["!!!!!!!CAN I HAVE HELP PLEASE!!!!!!")
	['help']
"""
remove_punctuation = remove_input_punctuation(user_input).strip().lower()
words = remove_punctuation.split()
return remove_unimportant_words(words, unimportant_words)

def remove_unimportant_words(words, unimportant_words)
"""this function will remove all of the umimportant words for the string and replace them with ""

It will return all of the remaining words in a new string that will be used as an input in other functions.
e.g.
>>>remove_unimportant_words(["go north to the kitchen"], ["to, "the", "kitchen"])
	['go north']

>>>remove_unimportant_words(["please drop the first aid kit"], ["please", "to", "the"])
	['drop first aid kit']

>>>remove_unimportant_words(["can i go west to Room 4"], ["can", "i", "to", "Room", "4"])
	['go west']

>>>remove_unimportant_words(["please kill the man for me"], ["please", "the", "for", "me"])
	['kill man']
"""
kept_words = [];
for word in words:
	if word not in unimportant_words:
		kept_words.append(word)
	return kept_words


def remove_input_punctuation(text)



no_punctuation_provided = ""
for char in text
