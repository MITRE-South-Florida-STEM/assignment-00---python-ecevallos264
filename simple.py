import math
'''
Write 6 print() statements to "draw" the following on the console

ooo/\ooo
oo/  \oo
o/ '' \o
/______\
|| || ||
xxxxxxxx

(hint: use escape sequence)
'''
line1 = 'ooo/\\ooo'
line2 = 'oo/  \\oo'
line3 = 'o/ \'\' \\o'
line4 = '/______\\'
line5 = '|| || ||'
line6 = 'xxxxxxxx'
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)

string = [
    'ooo/\\ooo\n', 'oo/  \\oo\n', 'o/ \'\' \\o\n', '/______\\\n',
    '|| || || \n', 'xxxxxxxx'
]
'''
Can you do it with just one print statement?
(hint: use string concatenation
'''
str = ""
for i in range(len(string)):
    str += string[i]
print(str)
'''
Choose three positive values for a, b, and c such that the final print() statement returns True
'''
a = 3
b = 4
c = 5
print(a**2 + b**2 == c**2)
