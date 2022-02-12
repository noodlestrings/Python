def capitialize(lower_case_word):
	get_text = input("Type something ")
	words = get_text.split(' ')
	new_text = []
	for word in words:
		new_text.append(word.replace(word[0],'#'))
		result = ' '.join(new_text)
	return(result)

capitialize("john")
