# your code goes here!

class Anagram:
    '''modelling an anagram'''
    def __init__(self, word):
        '''initialize attributes'''
        self.word = word

    def match(self, possible_anagrams):
        '''matching anagrams'''
        # matching_anagram = []
        # for anag in possible_anagrams:
        #     if sorted([char for char in anag]) == sorted([chara for chara in self.word]):
        #         #matching_anagram.append[anag]
        #         matching_anagram.append(anag)
        #         print(anag)
        #     else:
        #         print([])
        # #return matching_anagram
        match = [anag for anag in possible_anagrams if sorted([char for char in anag]) == sorted([chara for chara in self.word])]
        return match
    #print(matching_anagram)


my_word = Anagram("listen")

my_word.match(['enlists', 'google', 'inlets', 'banana'])

