class Search():
    def __init__(self, word, file):
        self.word = word
        self.file = file

    def search(self):
        with open(self.file, 'r') as file:
            word_list = file.read().lower()
            word_found = False
            
            if word_list.find(self.word.lower()) != -1:
                word_found = True

        if word_found:
            print("Word found!")
            return 1
        else:
            print("Word not in list")
            return -1

# test
search = Search("FAMily", "words.txt")
search.search()