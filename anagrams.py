#!/usr/bin/env python3
# Name  : anagrams.py
# Author: R.J.Toscani
# Date  : 26-02-2024
# Description: Python3 program that finds all word-*COMBINATIONS* in a 
# given language that form an anagram of the (combination of) word(s) given 
# as argument(s).
# Each matching combination of words appears in one distinct sequence only.
# With options to specify:
# - language: only one at the time, default language is Dutch;
# - minimum length of words in matching combination;
# - number of words in matching combination;
# - characters to be excluded from match (in order to avoid dots, apostrophs etc.).
#
# Disclaimer: word combinations presented by this program as anagram solutions can't
# be expected to be grammatically correct nor to make sense in general.
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


def make_list(languagefile, language):
    """Convert language file to dictionarylist:"""
    if language == "g":
    # German language list isn't UTF-8 encoded and contains superfluous text, so re-encode:
        with open(languagefile,'r', encoding='ISO-8859-1') as language:
             dictionarylist = [word.replace("\n","") for word in language.readlines()]
        return [ slashtag.sub('', line) for line in dictionarylist if line[0] != "#" ]
    else:
        with open(languagefile,'r') as language:
            dictionarylist = [word.replace("\n","") for word in language.readlines()]
        return dictionarylist


def excl(string, excl_chars):
    """Check if string does not contain any of the excl_chars:"""
    for char in excl_chars:
        if char in string:
            return False
    return True


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
                intpun.sub('', string))))))))
    return ''.join(sorted(string.lower()))


def compare(string, reference):
    """Compare string to reference, either return reference of reference residue:"""
    residue = reference
    for i in normalize(string):
        if i in residue:                      # If string letter is in reference as well:
            residue = residue.replace(i,"",1) # Subtract matching letter from reference
        else:
            return reference  # If any string letter is not in reference: return full reference 
    return residue            # Else return reference residue, to be matched to later strings
        

def combine(signature, word_args, signature_list, result):
    """Generate all signature combinations that match as an anagram for the given word_args:"""
    residue = word_args
    for i in signature:
        residue = residue.replace(i,"",1)
    if residue == "":
        result = result + [signature]
        if word_qty == -1 or len(result) == word_qty:
            read_words(result, 0, "")
        return
    signature_list_new = []
    for s in signature_list:
        if compare(s, residue) != residue:
            signature_list_new.append(s)
    for s in signature_list_new:
        if len(result) == word_qty:  # Stop if word_qty is reached and residue not yet empty
            return
        if len(s) >= len(signature): # To avoid multiple word sequence for one word combination
            combine(s, residue, signature_list_new, result + [signature])


def read_words(signature_list, i, anagramresult):
    """Print all word combinations for the given signature combinations:"""
    for word in anagrams[signature_list[i]]:
        new_anagramresult = anagramresult + word + " "
        if i < len(signature_list) - 1:
            read_words(signature_list, i + 1, new_anagramresult)
        else:
            print(new_anagramresult)


os.system('clear')

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
anagrams.py [-abdfghislqx] WORD(1) [ ... WORD(n)]\n
\t-a	American-English
\t-b	British-English
\t-d	Dutch
\t-f	French
\t-g	German
\t-h	Help (this output)
\t-i	Italian
\t-s	Spanish
\t-l MINLENGTH
\t	Show only results with at least word MINLENGTH
\t-q QTY
\t	Show only results with QTY words 
\t-x CHARS
\t	Exclude words with any of these CHARS 
"""

dictionarylist = make_list(dictionary_nl, "d")  # Dutch is default language
word_args = ""     # Initializations of word_args
word_qty = -1      # -1 means no filtering to word quantity of in anagram matches
minimum_length = 2 # To avoid single letters to appear in result, unless chosen by option -l
excl_chars = "_"   # Default: underscore does not appear so can always be excluded

"""Regular expressions:"""
intpun = re.compile('[\'\" .&-]')
a_acc = re.compile('[áàäâåÁÀÄÂ]')
e_acc = re.compile('[éèëêÉÈËÊ]')
i_acc = re.compile('[ïíìÏÍÌ]')
o_acc = re.compile('[óòöôøÓÒÖÔ]')
u_acc = re.compile('[úùüÚÙÜ]')
n_til = re.compile('[ñÑ]')
c_ced = re.compile('[çÇ]')
slashtag = re.compile('\/[^/]*')

'""Select option(s):""'
try:
    options, non_option_args = getopt.getopt(sys.argv[1:], 'abdfghisl:q:x:')
except:
    print(usage)
    sys.exit()

for opt, arg in options:
    if opt in ('-h'):
        print(usage)
        sys.exit()
    elif opt in ('-a'):
        dictionarylist = make_list(dictionary_am, "a")
    elif opt in ('-b'):
        dictionarylist = make_list(dictionary_br, "b")
    elif opt in ('-d'):
        dictionarylist = make_list(dictionary_nl, "d")
    elif opt in ('-f'):
        dictionarylist = make_list(dictionary_fr, "f")
    elif opt in ('-g'):
        dictionarylist = make_list(dictionary_de, "g")
    elif opt in ('-i'):
        dictionarylist = make_list(dictionary_it, "i")
    elif opt in ('-s'):
        dictionarylist = make_list(dictionary_sp, "s")
    elif opt in ('-l'):
        minimum_length = int(arg)
    elif opt in ('-q'):
        word_qty = int(arg)
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

# Generate anagrams dictionary with all words per unique sorted character signature:
anagrams = {}
for word in dictionarylist:
    if not excl(word, excl_chars):
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
    if compare(signature, word_args) != word_args:
        signaturelist.append(signature)

# Find the anagram combinations of these signatures with the word_args:
for signature in signaturelist:
    combine(signature, word_args, signaturelist, [])
