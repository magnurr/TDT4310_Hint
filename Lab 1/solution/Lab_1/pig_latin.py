import re

# A cheaty, and compact way of encoding pig latin  :sweat_smile: It is complete in one dialect that does not use yay.
# Find every word that starts with any sequence of non-vowels followed by any set of alphanumericals.
# Making the assumption that words to not contain numbers.


def word_to_pig_latin(word):
    pattern = re.compile(r'\A([^aeiou]*)(\w*)')
    # Switch the placement of the consonant group and the following characthers and add ay
    return pattern.sub(r'\2\1ay', word)


def sentence_to_pig_latin(text):
    # This is a slightly more complex pattern
    # But if you look for any consontant grouping, consisting of 0-inf length
    # followed by any group of alphanumericals of length 1-inf
    # followed by then any non alphanumerical i.e symbols or whitespaces
    # You can ensure a pretty ok encoder for piglatin, that handles symbols, and can be written in pure regex.

    pattern = re.compile(r'([b-df-hj-np-tv-z]*)([\w]+)([ ^\w]?)')
    return pattern.sub(r'\2\1ay\3', text.lower())


print(sentence_to_pig_latin(
    "I want to thank todays sponsor Raid Shadow Legends"))

# c)
"""
There are in general to issues you need to solve to be able to decode pig latin.
The first issues is about how you can be certain that you decoded to an english word. Since we can move clusters of consonants under encoding, and the end of the word can cotain consonats there is no way of accuractly seperating them when trying to decode
The naive apporach might be to move char from the end of the decoded word to the front and check against an english dictonary, this should in theory work fairly well.
However there is another issue. What about words that encode to the same to the same word in pig latin. Some of you have pointed this out with examples like ash and has that encode to ashay. For this we need to apply some context. Context can be many things, but the most usual way to go about it would be Bigrams, where you look at the preceding word as well as the current word to determine which of the possible decodes you should chose.
This can be further enhanced with the use of POS-tags (quite topical in my mind ^^ )

Someone also pointed out that we could use ML, but that is out of scope for now, but a really interesting apporach to something that by many is treated like quite the "novel" problem :^)

in short :chart_trending_upwards: , this is a way cooler than some argot just made for children. """
