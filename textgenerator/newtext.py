salutation = input('Please enter the salutation (For Neutral Press Enter) : ')
if salutation == '':
    salutation = 'Neutral'
name = input('Please enter the name: ')
content = input('Write your text: ')
mein_name = 'Stefan Hübner'

mappingSalutation = {
    'Frau': 'Sehr geehrte Frau ' + name + ',',
    'Herr': 'Sehr geehrter Herr' + name + ',',
    'Neutral': 'Hallo ' + name + ',',
}

print(mappingSalutation[salutation])

# if salutation == 'Frau':
#     print('Sehr geehrte Frau ' + name + ',')
# elif salutation == 'Herr':
#     print('Sehr geehrter Herr' + name + ',')
# else:
#     print('Hallo ' + name + ',')

print('')
print(content)
print('')
print('Mit freundlichen Grüßen')
print(mein_name)






