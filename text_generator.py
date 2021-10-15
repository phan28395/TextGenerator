import random

class WordToken:

    list_result_words = []

    def word_tokenize(self, file_corpus):
        """This function will return a list with all the words in txt file"""

        for line in file_corpus:
            line.strip()
            for word in line.split():
                self.list_result_words.append(word)
        return self.list_result_words

    def bigrams_tokenize(self, file_corpus):
        """This function will return a list with bigrams in format [[head, tail], [head, tail], ...]"""

        list_biagrams = []
        for i in range(len(self.word_tokenize(file_corpus))):
            if i != len(self.word_tokenize(file_corpus)) - 1:
                list_biagrams.append([self.word_tokenize(file_corpus)[i], self.word_tokenize(file_corpus)[i + 1]])
        return list_biagrams

    def markov_chain_maker(self, file_corpus):
        """This function will return a dictionary with head and the occurrence frequency of its tails"""

        dict_markov_chain = {}
        for word_pair in self.bigrams_tokenize(file_corpus):
            dict_markov_chain.setdefault(word_pair[0], {})
            dict_markov_chain[word_pair[0]].setdefault(word_pair[1], 0)
            dict_markov_chain[word_pair[0]][word_pair[1]] += 1
        return dict_markov_chain

    def random_sentence_generate_list_part(self, word_random, file_corpus):
        """This function is a part of random_sentence_generate function, it will return a list words"""
        list_word = []
        dict_markov = self.markov_chain_maker(file_corpus)
        for key in dict_markov[word_random].keys():
            list_word.append(key)
        return list_word

    def random_sentence_generate_weight_part(self, word_random, file_corpus):
        """This function is a part of random_sentence_generate function, it will return a list of weight of words"""
        list_weight = []
        dict_markov = self.markov_chain_maker(file_corpus)
        for value in dict_markov[word_random].values():
            list_weight.append(value)
        for i in range(len(list_weight)):
            list_weight[i] = (list_weight[i] / (sum(list_weight))) * 100
        return list_weight

    def random_sentence_generate(self, word_random, file_corpus):
        """This function will take a random word as parameter and generate a list with 10 sentences
        base on occurrence frequency of each words. First sentence will take a random word as start word in the
        text file. The other one will take the last word from the previous sentence as start word"""

        list_sentences_generated = []
        list_word_random = [word_random]
        for i in range(10):
            list_sentences_generated.append(random.choices(self.random_sentence_generate_list_part(list_word_random[i],
                                                                                                   file_corpus),
                                                           weights=self.random_sentence_generate_weight_part(list_word_random[i],
                                                            file_corpus), k=10))
            list_word_random.append(list_sentences_generated[i][-1])
        for sentence in list_sentences_generated:
            print(' '.join(sentence))




def main():  # Enter file name, and enter the index of biagram pair

    file_name = input()
    file_corpus = open(file_name, 'r', encoding='utf-8')
    obj = WordToken()
    list_biagrams_main = obj.bigrams_tokenize(file_corpus)  # Do this will help the program run faster
    print('Number of bigrams:', len(list_biagrams_main))
    # while True:  # Stage 1
    #
    #     global index
    #     index = input()
    #     if index == 'exit':
    #         exit()
    #     try:
    #         print(obj.word_tokenize(file_corpus)[int(index)])
    #     except ValueError:
    #         print('Type Error. Please input an integer.')
    #     except IndexError:
    #         print('Index Error. Please input an integer that is in the range of the corpus.')
    while True:
        global index
        index = input()
        if index == 'exit':
            file_corpus.close()
            exit()

        try:
            print('Head:', list_biagrams_main[int(index)][0], end='  ')
            print('Tail:', list_biagrams_main[int(index)][1])
        except ValueError:
            print('Type Error. Please input an integer.')
        except IndexError:
            print('Index Error. Please input an integer that is in the range of the corpus.')


def main_stage3():  # Enter file name, and enter the head that you want to see the frequency of its tails
    obj = WordToken()
    file_name = input()
    file_corpus = open(file_name, 'r', encoding='utf-8')

    dict_frequency = obj.markov_chain_maker(file_corpus)
    while True:
        head_name = input()
        if head_name == 'exit':
            file_corpus.close()
            exit()
        try:
            print('Head:', head_name)
            for key, value in dict_frequency[head_name].items():
                print('Tail:', key, end='   ')
                print('Count:', value)
        except KeyError:
            print('Key Error. The requested word is not in the model. Please input another word.')

def main_stage4():
    obj = WordToken()
    file_name = input()
    file_corpus = open(file_name, 'r', encoding='utf-8')
    list_all_words = obj.word_tokenize(file_corpus)
    chosen_word_random = list_all_words[random.randint(0, len(list_all_words))]

    obj.random_sentence_generate(chosen_word_random, file_corpus)


if __name__ == '__main__':
    main_stage4()
