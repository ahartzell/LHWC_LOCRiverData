
str = '7.8 (+-3.9)'

if '(+-' in str:
    print('We found it!')
    
print(str.split('('))

splitResult = str.split('(')

print(splitResult)