# TODO
from cs50 import get_string

# ask user for input
text = get_string("Text: ")

# count letters, words and sentences in input. No numbers allowed
letters = 0
words = 1
sentences = 0

for i in text:
    if i.isalpha():  # check if text is alpha first
        letters += 1
    # find spaces to count number of words
    elif i == " ":
        words += 1
    elif i == "." or i == "!" or i == "?":
        sentences += 1

# use Coleman-Liau formula 0.0588 * L - 0.296 * S - 15.8 (L = avg letters. S =  avg sentences)
index = round(
    0.0588 * (letters / words * 100) - 0.296 * (sentences / words * 100) - 15.8
)

# output Grade
if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print("Grade ", index)
