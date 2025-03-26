
def search(dictionary, characters, main_char, word_list=None,index=0, words=None):
    if words is None:
        # Using a set to avoid duplicate words
        # Set lookups are faster with O(1) as Python uses a hash table internally
        # Improved from list, as there are 89059 comparisions in worst case
        words = set()

    if word_list is None:
        word_list = [] # Using list instead of string concatenation

    word = ''.join(word_list) # Converting word list to string for better dictionary checking

    # Word conditions in the Spelling Bee 
    # - word needs to be greater than 3 
    # - contain the featured char
    # - be a valid English word

    if len(word) > 3 and main_char in word and word in dictionary:
        words.add(word)

    # Recursively try each character that hasn't been used
    for i in range(index, len(characters)):
        word_list.append(characters[i])
        # Pass a sliced list excluding the used character
        search(dictionary, characters[:i] + characters[i+1:], main_char, word_list, 0, words)
        word_list.pop()

    return words # Returning as set to avoid duplicates
    

# test
dictionary = set(open("words.txt", 'r').read().lower().splitlines())
result = search(dictionary, ['o','n','i','l','x','f', 'e'], 'e')
print(result)