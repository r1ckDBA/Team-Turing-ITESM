def reverseWord(word):
	list_separated = []
	tmp_word = ""
	for character in word:
		if character != " ":
			tmp_word = tmp_word + character
		else:
			list_separated.append(tmp_word)
			tmp_word = ""
	list_separated.append( tmp_word )

	reversed_word = ""
	for element in list_separated[::-1]:
	    reversed_word = reversed_word + element + " "

	return reversed_word