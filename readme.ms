.SH 1
Name: anagrams.py
.pdfhref O 1 "Name: anagrams.py"
.pdfhref M "name-anagrams.py"
.LP
anagrams.py - a program that finds all word-\f[I]COMBINATIONS\f[R] in a
given language that form an anagram of the (combination of) word(s)
given as argument(s).
.SH 1
Description:
.pdfhref O 1 "Description:"
.pdfhref M "description"
.LP
anagrams.py is a Python3 program that finds all
word-\f[I]COMBINATIONS\f[R] in a given language that form an anagram of
the (combination of) word(s) - whether or not existing(!) - given as
argument(s).
.PP
anagrams.py offers options to chose: - language: only one at the time,
default language is Dutch; - minimum length of words in matching
combination; - maximum number of words in matching combination; -
characters to be excluded from match (in order to avoid dots, apostrophs
etc.); - a (quoted sequence of) word(s) that must be part of the
matching combination (length nor characters restricted); - to permute
word order of matching word combinations (default only 1 word order).
.PP
The results are sent to standard output and can be piped to e.g.\ `less'
or other utilities and applications.
.PP
Perequisite is presence on the system of a word list in flat text format
of at least one language.
In its present form, the program code references following language word
lists:
.IP
.nf
\f[C]
/usr/share/dict/dutch
/usr/share/dict/american-english
/usr/share/dict/british-english
/usr/share/hunspell/de_DE_frami.dic
/usr/share/dict/french
/usr/share/dict/spanish
/usr/share/dict/italian
\f[]
.fi
.LP
If no language option is given, Dutch is the default language.
.PP
If wished and as per system configuration, above paths and langauge
default may be changed or removed and references to other word lists may
be added, by modifying the program code accordingly.
.SH 1
How to use anagrams.py
.pdfhref O 1 "How to use anagrams.py"
.pdfhref M "how-to-use-anagrams.py"
.SH 2
Usage:
.pdfhref O 2 "Usage:"
.pdfhref M "usage"
.IP
.nf
\f[C]
anagrams.py [-abdfghislqxIP] WORD(1) [ ... WORD(n)]
\f[]
.fi
.SH 2
Options:
.pdfhref O 2 "Options:"
.pdfhref M "options"
.IP
.nf
\f[C]
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
\f[]
.fi
.LP
Options can be combined but only one (1) language can be set at the
time.
.PP
One of more [WORD] arguments must be given, to which the program will
present all matching combinations of words, given the option settings.
.PP
For example, the command:
.IP
.nf
\f[C]
./anagrams.py -a -l5 word combination
\f[]
.fi
.LP
gives following result:
.IP
.nf
\f[C]
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
\f[]
.fi
.SH 1
Author:
.pdfhref O 1 "Author:"
.pdfhref M "author"
.LP
Written by Rob Toscani (rob_toscani\[at]yahoo.com).
