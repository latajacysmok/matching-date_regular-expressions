import pyperclip, re
import time
import datetime

dateRegex = re.compile(r'''(
    (\d{1,4}) #3/14/2015 03-14-2015 2015/3/14  2015\3\14
    (\s|-|\.|[/]|\\)?
    (\d{1,2})
    (\s|-|\.|/)?
    (\d{1,4})
)''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []

for groups in dateRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Skopiowano do schowka: ')
    print('\n'.join(matches))
    # for i in list(matches):
    #     print("i: ", i)
    #     print(datetime.datetime.strptime("03-14-2015", '%d-%m-%Y'))

else:
    print('Nie znaleziono żadnej daty.')
