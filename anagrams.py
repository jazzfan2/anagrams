#!/usr/bin/env python3
# Name  : anagrams.py
# Author: R.J.Toscani
# Date  : 26-02-2024
# Description: Python3 program that finds all word-*COMBINATIONS* in a 
# given language that form an anagram of the (combination of) word(s) - whether
# or not existing(!) - given as argument(s). With options in order to set:
# - language: only one at the time, default language is Dutch;
# - minimum length of words in matching combination;
# - maximum number of words in matching combination;
# - a (quoted sequence of) word(s) that must be part of the matching combination;
# - characters to be excluded from match (in order to avoid dots, apostrophs etc.).
#
# Each matching combination of words appears in one distinct word sequence.
#
# Disclaimer: word combinations presented by this program as anagram solutions can't
# be expected to be grammatically correct nor to make sense in general.
#
# Use pypy3 for enhanced speed.
#
######################################################################################
#
# Copyright (C) 2024 Rob Toscani <rob_toscani@yahoo.com>
#
# anagrams.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# anagrams.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
######################################################################################

import getopt
import sys
import re
import os
import time


def to_list(file, language):
    """Convert language file to dictionarylist:"""
    if language == "g": # German language file
                        # Not UTF-8 encoded and contains superfluous text, so re-encode:
        with open(file,'r', encoding='ISO-8859-1') as language:
             dictionarylist = [word.replace("\n","") for word in language.readlines()]
        return [ slashtag.sub('', line) for line in dictionarylist if line[0] != "#" ]
    else:
        with open(file,'r') as language:
            dictionarylist = [word.replace("\n","") for word in language.readlines()]
        return dictionarylist


def normalize(string):
    """ By means of regular expressions, normalize all characters to lower case,
        remove accent marks and other non-alphanumeric characters,
        and convert string to a unique sorted character signature:"""
    string = a_acc.sub('a', \
                e_acc.sub('e', \
                i_acc.sub('i', \
                o_acc.sub('o', \
                u_acc.sub('u', \
                n_til.sub('n', \
                c_ced.sub('c', \
                intpunct.sub('', string))))))))
    return ''.join(sorted(string.lower()))


def contains(string, characters):
    """Check if string contains any of characters:"""
    for char in characters:
        if char in string:
            return True                       # one of more of characters is in string
    return False                              # none of characters is in string


def is_subset(string1, string2):
    """Check if all characters in string1 are a subset of the characters in string2:"""
    for i in string1:
        if i in string2:                      # If character in string1 is in string2 too:
            string2 = string2.replace(i,"",1) # Remove matching letter from string2
        else:
            return False                      # string1 characters are not subset
    return True                               # string1 characters are subset
        

def combine(signature, word_args, signaturelist, result):
    """Generate all signature combinations that match as an anagram for the given word_args:"""
    residue = word_args
    for i in signature:
        residue = residue.replace(i,"",1)
    if residue == "":
        result = result + [signature]
        if maximum_qty < 0 or len(result) <= maximum_qty:
            get_words(result, 0, "")     # Get all words belonging to these sign. combinations
        return
    if len(residue) < minimum_length or len(result) == maximum_qty-1:
        return                           # No solutions will be found in these two cases
    signaturelist_reduced = []
    for s in signaturelist:
        if s != residue and \
           len(result) == maximum_qty-2: # If 's' is not equal to residue if maximally 1 more
            continue                     # recursion is left to empty residue, 's' is rejected
        if is_subset(s, residue):        # All letters in s must be in residue as well
            signaturelist_reduced.append(s)
    for s in signaturelist_reduced:
        if order[s] > order[signature]:  # To achieve 1 distinct sequence per sign. combination
            combine(s, residue, signaturelist_reduced, result + [signature])


def get_words(signaturelist, i, anagramresult):
    """Print all word combinations for the given signature combinations:"""
    for word in anagrams[signaturelist[i]]:
        anagramresult_new = anagramresult + word + " "
        if i < len(signaturelist) - 1:
            get_words(signaturelist, i + 1, anagramresult_new)
        else:
            print(anagramresult_new + spaces1.sub('', spaces2.sub(' ', incl_words)))


# os.system('clear')

language = dictionary_nl = "/usr/share/dict/dutch"
dictionary_am = "/usr/share/dict/american-english"
dictionary_br = "/usr/share/dict/british-english"
dictionary_de = "/usr/share/hunspell/de_DE_frami.dic"
dictionary_fr = "/usr/share/dict/french"
dictionary_sp = "/usr/share/dict/spanish"
dictionary_it = "/usr/share/dict/italian"

# Text printed if -h option (help) or a non-existing option has been given:
usage = """
Usage:
anagrams.py [-abdfghislqx] WORD(1) [ ... WORD(n)]
\t-a	American-English
\t-b	British-English
\t-d	Dutch
\t-f	French
\t-g	German
\t-h	Help (this output)
\t-i	Italian
\t-s	Spanish
\t-l MINLENGTH
\t	Results with words of at least MINLENGTH only
\t-q MAXQTY
\t	Results with maximally MAXQTY words only
\t-I WORDS
\t	Results including WORDS only (length not restricted by option -l)
\t-x CHARS
\t	Exclude words with any of these CHARS 
"""

dictionarylist = to_list(dictionary_nl, "d")  # Dutch is default language
word_args      = ""  # Initializations of word_args
maximum_qty    = -1  # -1 means that anagram matches are not filtered to word quantity 
minimum_length = 2   # Blocks single letters to appear in result, unless so chosen by option -l
incl_words     = ""
excl_chars     = "_" # Default: underscore does not appear so can always be excluded


"""Regular expressions:"""
a_acc = re.compile('[áàäâåÁÀÄÂ]')
e_acc = re.compile('[éèëêÉÈËÊ]')
i_acc = re.compile('[ïíìÏÍÌ]')
o_acc = re.compile('[óòöôøÓÒÖÔ]')
u_acc = re.compile('[úùüÚÙÜ]')
n_til = re.compile('[ñÑ]')
c_ced = re.compile('[çÇ]')
intpunct = re.compile('[\'\" :.&-]')
slashtag = re.compile('\/[^/]*')
spaces1 = re.compile('^ +')
spaces2 = re.compile(' +')

'""Select option(s):""'
try:
    options, non_option_args = getopt.getopt(sys.argv[1:], 'abdfghisl:q:I:x:')
except:
    print(usage)
    sys.exit()

for opt, arg in options:
    if opt in ('-h'):
        print(usage)
        sys.exit()
    elif opt in ('-a'):
        dictionarylist = to_list(dictionary_am, "a")
    elif opt in ('-b'):
        dictionarylist = to_list(dictionary_br, "b")
    elif opt in ('-d'):
        dictionarylist = to_list(dictionary_nl, "d")
    elif opt in ('-f'):
        dictionarylist = to_list(dictionary_fr, "f")
    elif opt in ('-g'):
        dictionarylist = to_list(dictionary_de, "g")
    elif opt in ('-i'):
        dictionarylist = to_list(dictionary_it, "i")
    elif opt in ('-s'):
        dictionarylist = to_list(dictionary_sp, "s")
    elif opt in ('-l'):
        minimum_length = int(arg)
    elif opt in ('-q'):
        maximum_qty = int(arg)
    elif opt in ('-I'):
        incl_words = arg
    elif opt in ('-x'):
        excl_chars = arg

# Non-option argument(s) must be included: 
if len(non_option_args) == 0:
    print(usage)
    sys.exit()  

# Convert the non-option word arguments to a unique sorted character signature:
word_args = ""
for word in non_option_args:
    word_args = word_args + word
word_args = normalize(word_args)


# Loop through all 'include'-words:
incl_words_list = [ word for word in incl_words.split(' ') ]
for incl_word in incl_words_list:

    # Stop if 'include'-word is not in the language dictionary:
    if incl_word != "" and incl_word not in dictionarylist:
       sys.exit()

    # Convert the 'include'-word to a unique sorted "Include"-signature:
    incl_signa = normalize(incl_word)

    # Subtract 'include'-signature from word_args signature:
    for char in incl_signa:
        if char in word_args:
            word_args = word_args.replace(char, "", 1)
        else:          # Interrupt if 'include'-word characters are not a subset of word_args
            sys.exit()

    # Print 'include'-words here if covering all word_args characters, and terminate program:
    if word_args == "":      # word_args has become empty after subtracting all incl_words
        print(spaces1.sub('', spaces2.sub(' ', incl_words)))
        sys.exit()

    # The 'include'-word is part of result in advance, so remaining maximum_qty becomes 1 less:
        maximum_qty -= 1

# Generate anagrams dictionary with all words per unique sorted character signature:
anagrams = {}
for word in dictionarylist:
    if contains(word, excl_chars):
        continue
    signature = normalize(word)
    if len(signature) < minimum_length:
        continue
    if signature in anagrams:
        anagrams[signature].append(word)
    else:
        anagrams[signature] = [word]

# List of signatures of which all (distinct) letters are in word_args as well:
signaturelist = [] 
for signature in anagrams:
    if is_subset(signature, word_args):
        signaturelist.append(signature)

# Quick searchable dictionary to compare signature index order:
index = 0
order = {}
for signature in signaturelist:
    order[signature] = index
    index += 1

# Find the distinct combinations of these signatures that form anagrams of the word_args:
for signature in signaturelist:
    combine(signature, word_args, signaturelist, [])
