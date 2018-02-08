def isPalindrome(word):
	i = 0
	new_word = ""
	for character in word:
		if character != ' ':
			new_word = new_word +  character.lower()
	len_word = len(new_word)
	while i < len_word/2:
		if new_word[i] != new_word[len_word - i - 1]:
			return False
		i = i + 1
	return True