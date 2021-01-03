#!/usr/bin/env python3
import re

# * Repetition Qualifiers

# (.*) Any character repeated as many times as possible including 0
print(re.search(r'Py.*n', 'Pygmalion'))  # RETURNS WHOLE WORD

# Being Greedy -> the * takes as many as charaters as possible
print(re.search(r'Py.*n', 'Python Programming'))

# MATCHING JUST ANY LETTERS [a-z]
print(re.search(r'Py[a-z]*n', 'Python Programming'))

#
print(re.search(r'Py[a-z]*n', 'Pyn'))

# (+) SEARCH FOR CHAR REPETIOTIONS (OL) WILL MATCH
print(re.search(r'o+l+', 'goldfish'))
# MATCHING MUTIPLE REPETITIONS
print(re.search(r'o+l+', 'woolly'))
# HERE ARE NO REPETITIONS OF OO OR LL
print(re.search(r'o+l+', 'boil'))

# * Optional
# (?) MARKS THE CHAR FEFORE IT AS "OPTIONAL" MEANING ZERO TO ONE OCCURANCES
print(re.search(r'p?each', 'To each their own'))
# HERE (?) WILL MATCH ONCE
print(re.search(r'p?each', 'I like peaches'))


###############* Advanced ####################

# specify the num of characters we search for
print(re.search(r'[A-za-z]{5}', 'a ghost in a shell'))  # search for 5 chars
# returns the firt matching pattern
print(re.search(r'[a-zA-Z]{5}', 'a scary ghost appeared'))
# finding all will also return 'appre'
print(re.findall(r'[A-Za-z]{5}', 'a scary ghost appreared'))
# fi we only want full words use \b
print(re.findall(r'\b[A-Za-z]{5}\b', 'a scary ghost appreared'))

# * Using ranges
# all words from 5 to 10 chars
print(re.findall(r'\w{5,10}', 'I really like strawberries'))
# five an up
print(re.findall(r'\w{5,}', 'I really like strawberries'))
# from 0 up to n with a (s)
print(re.search(r's\w{,20}', 'I really like strawberries'))
# full words only
print(re.findall(r'\b\w{5,10}\b', 'I really like strawberries'))


# * The long_words function returns all words that are at least 7 characters. Fill in the regular expression to complete this function.


def long_words(text):
    pattern = r'\w{7,}'
    result = re.findall(pattern, text)
    return result


print(long_words("I like to drink coffee in the morning."))  # ['morning']
# ['chocolate', 'afternoon']
print(long_words("I also have a taste for hot chocolate in the afternoon."))
print(long_words("I never drink tea late at night."))  # []
