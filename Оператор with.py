
class WordsFinder:
    file_names = []
    def __init__(self,*names):
        self.file_names = list(names)


    def remove_punctuation(self, text):
        punctuations = "',.=!?;:-"
        return ''.join(char for char in text if char not in punctuations)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding = 'utf-8') as file:
                read_file = file.read()
                lower_file = read_file.lower()
                split_file = self.remove_punctuation(lower_file).split()
                all_words[file_name] = split_file
        return all_words




    def find(self, word):
        dikt_find = {}
        self.word = word.lower()
        for name, words in self.get_all_words().items():
            if self.word in words:
                dikt_find.update({name: words.index(self.word) +1})
        return dikt_find

    def count(self, word):
        dikt_count = {}
        self.word = word.lower()
        for name, words in self.get_all_words().items():
            if self.word in words:
                dikt_count.update({name: words.count(self.word)})
        return dikt_count

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

