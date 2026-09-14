def pin_extractor(poems): # we defines a function that we will call on later
    secret_codes = [] # an empty list, for usage of storing multiple pins
    for poem in poems: # a loop that loops thru all the poems
        secret_code = '' #empty variable for storing pin for each poem
        lines = poem.split('\n')
        for line_index, line in enumerate(lines): #a loop that check the index value of each word in the poem making them into numbers
            words = line.split() # putting the indevidual number in the variable words 
            if len(words) > line_index: # checking if the index length of the lines are enough otherwise it adds an additional "0"
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code) # adding pin codes after each other
    return secret_codes        # what we want the function to return when its called

poem = """Stars and the moon
shine in the sky
white and bright
until the end of the night"""

poem2 = 'The grass is green\n here and there\n hoping for rain\n before it turns yellow'
poem3 = 'There\n once\n was\n a\n dragon'

print(pin_extractor([poem, poem2, poem3])) # the output
