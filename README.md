# Name: anagrams.py
anagrams.py - generates all single- and multi-word anagrams for the (combination of) word(s) given as argument(s).

# Description:
anagrams.py is a Python3 program that generates all words and *word-combinations* in a 
given language that form an anagram of the (combination of) word(s) - whether or not existing - given as argument(s).

anagrams.py offers the possibility to set various properties to manipulate and filter the results,
such as:
- the language in which the anagrams are to be generated (default is Dutch);
- the minimum length of words in the generated anagrams;
- the maximum number of words per anagram;
- any characters to be excluded from the anagrams;
- any existing or non-existing (quoted sequence of) word(s) that must be part of the anagram;

In addition, the program can optionally be made to:
- permute the word order of all generated multi-word anagrams (default is only one word order);
- instead of returning the anagrams, provide all the single "subset-words",
that have all their alphanumeric characters in common with the argument word(s).

The results are sent to standard output and can be piped to e.g. 'less' or other utilities and applications.

Prerequisite is presence on the system of a word list in flat text format of at least one language.
In its present form, the program code references following language word lists: 

	/usr/share/dict/dutch
	/usr/share/dict/american-english
	/usr/share/dict/british-english
	/usr/share/hunspell/de_DE_frami.dic
	/usr/share/dict/french
	/usr/share/dict/spanish
	/usr/share/dict/italian

If no language option is given, Dutch is the default language.

If wished and as per system configuration, above paths and language default may be changed or removed and references to other word lists may be added, by modifying the program code accordingly.

# How to use anagrams.py

## Usage:

	anagrams.py [-abdfghislqxIPS] WORD(1) [ ... WORD(n)]

## Options:
	-a            American-English
	-b            British-English
	-d            Dutch
	-f            French
	-g            German
	-h            Help (this output)
	-i            Italian
	-s            Spanish
	-l MINLENGTH  Results with words of at least MINLENGTH only
	-q MAXQTY     Results with maximally MAXQTY words only
	-x CHARS      Exclude words with any of these CHARS
	-I INCLWRDS   Results including INCLWRDS (NOT restricted by options -l, -x) only
	-P            Permute word order per anagram if it contains 2 or more words
	-S            Instead of anagrams, print all character subset words (not with option -I) 

Options can be combined but only one (1) language can be set at the time.

One of more [WORD] arguments must be given,
to which the program will present all matching anagrams given the option settings.

For example, the command:

	./anagrams.py -a -l5 word combination

gives following result:

	Acton Brown idiom 
	Acton brown idiom 
	canto Brown idiom 
	canto brown idiom 
	Brown Macon idiot 
	brown Macon idiot 
	Robin contd miaow 
	robin contd miaow 
	Rodin Twain combo 
	Rodin twain combo 
	baton crown idiom

For a detailed description see the man-page included in this repository.

# Author:
Written by Rob Toscani (rob_toscani@yahoo.com).
