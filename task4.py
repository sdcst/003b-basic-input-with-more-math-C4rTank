#!python3
 
"""
Assignment 5:
Make a Mad Lib

Ask the user to enter a number of words, one for each of the underscored words in the following paragraph.  Once they have finished, display the following story to them with the replacements made in the Mad Lib

Today we picked apple from _PERSON_'s Orchard. 
I had no idea there were so many different varieties of apples. 
I ate _ADJECTIVE_ apples straight off the tree that tasted like _FOOD_. 
Then there was a _ADJECTIVE_ apple that looked like a _NOUN_.  
When our bag was full, we went on a free hay ride to _PLACE_ and back. 
It ended at a hay pile where we got to _VERB_ _ADVERB_. 
I can hardly wait to get home and cook with the apples. 
We are going to make apple _FOOD_ and _THINGS_ pies!
"""

person = input("Enter a Person :")
adj = input("Enter an Adjective :")
noun = input("Endter a Noun :")
plac = input("Enter a Place :")
verb = input("Enter a Verb :")
adver = input("Enter an Adverb :")
food = input("Enter a Food :")
thing = input("Enter a Thing :")

print("Today we picked apple from",person +"'s Orchard.")
print("I had no idea there were so many different varieties of apples.")
print("I ate",adj,"apples straight off the tree that tasted like",food +".")
print("Then there was a",adj,"apple that looked like a",noun +".")
print("When our bag was full, we went on a free hay ride to",plac,"and back.")
print("It ended at a hay pile where we got to",verb,adver +".")
print("I can hardly wait to get home and cook with the apples.")
print("We are going to make apple",food,"and",thing +"s pies!")