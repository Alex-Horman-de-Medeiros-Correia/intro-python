import re

def append_each_letter_of_the_word_in_a_list(word: str):
    """ return [letter for letter in word] """

    letter_list = list()

    for letter in word:
        letter_list.append(letter)

    return letter_list


def return_index_of_the_uppercase_letter(word: str):
        regex = '[A-Z]+[a-z]+$'
        x =  re.search(regex, word)
        
        if x:
            
            return x.span()[0]
        else:
           
            return len(word) -1
   
""" print(return_index_of_the_uppercase_letter('espadAa')) """


def return_element_from_list_that_is_string(input_list: list):
    for elem in input_list:
         if type(elem) == str:
              print(elem)
              return elem
         
