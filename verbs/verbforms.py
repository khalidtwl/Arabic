# Sample roots for debugging: درس باع
# Abstract away the char sizes of Arabic characters
import sys

# Printing to a file
# orig_stdout = sys.stdout
# f = file('out.txt', 'w')
# sys.stdout = f

char_size = len('ي')

def past_tense(root):
    f = root[0]
    a = root[1]
    l = root[2]
    lst = []
    lst.append(f + 'َ' + a + 'َ' + l + 'َ')
    lst.append(f + 'َ' + a + 'َّ' + l + 'َ')
    lst.append(f + 'َ' + 'ا' + a + 'َ' + l + 'َ')
    lst.append('أ' + f + 'ْ' + a + 'َ' + l + 'َ')
    lst.append('تَ' + f + 'َ' + a + 'َّ' + l + 'َ')
    lst.append('تَ' + f + 'َ' + 'ا' + a + 'َ' + l + 'َ')
    lst.append('اِنْ' + f + 'َ' + a + 'َ' + l + 'َ')
    lst.append('اِ' + f + 'ْ' + 'تَ' + a + 'َ' + l + 'َ')
    lst.append('اِ' + f + 'ْ' + a + 'َ' + l + 'َّ')
    lst.append('اِسْتَ' + f + 'ْ' + a + 'َ' + l + 'َ')
    return lst

def present_tense(root):
    f = root[0]
    if f == 'و':
        f == ''
    a = root[1]
    if a == 'ا':
        a = 'ي'
    l = root[2]
    lst = []
    lst.append('يَ'+f+'ْ'+a+'َُِ'+l+'ُ')
    lst.append('يُ'+f+'َ'+a+'ِّ'+l+'ُ')
    lst.append('يُ'+f+'َ'+'ا'+a+'ِ'+l+'ُ')
    lst.append('يُ'+f+'ْ'+a+'ِ'+l+'ُ')
    lst.append('يَتَ'+f+'َ'+a+'َّ'+l+'ُ')
    lst.append('يَتَ'+f+'َ'+'ا'+a+'َ'+l+'ُ')
    lst.append('يَنْ'+f+'َ'+a+'ِ'+l+'ُ')
    lst.append('يَ'+f+'ْ'+'تَ'+a+'ِ'+l+'ُ')
    lst.append('يَ'+f+'ْ'+a+'َ'+l+'ُّ')
    lst.append('يَسْتَ'+f+'ْ'+a+'ِ'+l+'ُ')
    return lst

def verb_chart(root):
    print('%12s %12s \n' % ('ماضي', 'مضارع'))
    for i in range(10):
        print('%12s   %12s' % (past_tense(root, i+1), present_tense(root, i+1)))

# Checks if root is 3 letters long
# while not len(root) == 3:
#     root = input("That was " + str(len(root)) + " character(s) long. Please type in a 3-letter root:")

# Stores conjugations as lists
# past = past_tense(root)
# present = present_tense(root)

# Pretty prints
# for i in range(10):
#     print(past[i], present[i])

# Reverting to shell
# sys.stdout = orig_stdout
# f.close()
