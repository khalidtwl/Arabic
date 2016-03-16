import re

char_size = len('ي')

# Arabic Unicode Block
form1 = re.compile('([\u0600-\u06FF]\u064E){3}')
form2 = re.compile('[\u0600-\u06FF]\u064E?[\u0600-\u06FF]\u0651[\u0600-\u06FF]\u064E?')
form3 = re.compile('[\u0600-\u06FF]\u064E?\u0627([\u0600-\u06FF]\u064E?){1}([\u0600-\u06FF]\u064E?){1}')

word = input("Enter an Arabic verb: ")

# Confirmation message
if form1.match(word):
    print("Form 1 verb")

# Testing Diacritic
if form2.match(word):
    print("Form 2 verb")

if form3.match(word):
    print("Form 3 verb")
