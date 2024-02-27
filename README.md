# Name: anagrams.py
anagrams.py - a program that finds all word-*COMBINATIONS* in a given language that form an anagram of the (combination of) word(s) given as argument(s).

# Description:
anagrams.py is a Python3 program that finds all word-*COMBINATIONS* in a 
given language that form an anagram of the (combination of) word(s) given as argument(s).
Each matching combination of words appears in one distinct sequence only.

anagrams.py offers options to set:
- language: only one at the time, default language is Dutch;
- minimum length of words in matching combination;
- maximum number of words in matching combination;
- a word that must be part of the matching combination;
- characters to be excluded from match (in order to avoid dots, apostrophs etc.).

The results are sent to standard output and can be piped to e.g. 'less' or other utilities and applications.

Perequisite is presence on the system of a word list in flat text format of at least one language.
In its present form, the program code references following language word lists: 

	/usr/share/dict/dutch
	/usr/share/dict/american-english
	/usr/share/dict/british-english
	/usr/share/hunspell/de_DE_frami.dic
	/usr/share/dict/french
	/usr/share/dict/spanish
	/usr/share/dict/italian

If no language option is given, Dutch is the default language.

If wished and as per system configuration, above paths and langauge default may be changed or removed and references to other word lists may be added, by modifying the program code accordingly.

# How to use anagrams.py

## Usage:

	anagrams.py [-abdfghislqx] WORD(1) [ ... WORD(n)]

## Options:
	-a            American-English
	-b            British-English
	-d            Dutch
	-f            French
	-g            German
	-h            Help (this output)
	-i            Italian
	-s            Spanish
	-l MINLENGTH  Show only results with words of at least MINLENGTH
	-q MAXQTY     Show only results with maximally MAXQTY words 
	-I WORD       Show only results containing WORD
	-x CHARS      Exclude words with any of these CHARS 

Options can be combined but only one (1) language can be set at the time.

One of more [WORD] arguments must be given, to which the program will present all matching combinations of words, given the option settings.

For example, the command:

	./anagrams.py -a -l6 github actions

gives following result:

	Chiba's touting 
	GitHub action's 
	GitHub actions 
	GitHub cation's 
	GitHub cations 
	action GitHub's 
	cation GitHub's 
	aught's bitcoin 
	aughts bitcoin 
	bight's auction 
	bight's caution 
	bights auction 
	bights caution 
	bough's Titanic 
	bough's titanic 
	boughs Titanic 
	boughs titanic 
	chino's Bugatti 
	chinos Bugatti 
	coitus bathing 
	touch's baiting 

# Author:
Written by Rob Toscani (rob_toscani@yahoo.com).
