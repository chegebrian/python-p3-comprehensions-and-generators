#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers = [even for even in num_list if even % 2 == 0]

    return even_numbers


def make_exclamation(sentence_list):
    ammended_sentence = [sentence + "!" for sentence in sentence_list]
    return ammended_sentence
