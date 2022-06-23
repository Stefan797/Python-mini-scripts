stundenlohn = input('Bitte gebe deinen Stundenlohn ein: ')
tag = 8 * int(stundenlohn) # int bedeutet einen string in eine Zahl umwandeln
monat = tag * 20
year = monat * 12

print('Dein Stundenlohn beträgt ' + str(stundenlohn) + '€') # str bedeutet einen Zahl in eine string umwandeln
print('Du verdienst ' + str(tag) + '€ pro Tag')
print('Du verdienst pro Monat ' + str(monat) + '€')
print('Du hast ein Jahresgehalt von ' + str(year) + '€')

input('Drücke eine beliebige Taste um das Programm zu schließen') # um den text in der console behalten zu können 
