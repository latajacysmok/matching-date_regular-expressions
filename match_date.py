import pyperclip, re
import time
import datetime

dateRegex = re.compile(r'''(
    (\d{1,4}) #3/14/2015 03-14-2015 2015/3/14  03.01.2018
    (\s|-|\.|[/]|\\)?
    (\d{1,2})
    (\s|-|\.|/)?
    (\d{1,4})
)''', re.VERBOSE)

def changeFormatDate():
    for i in matches:
        try:
            polishDate = datetime.datetime.strptime(i, '%d.%m.%Y')
            usaDate = datetime.datetime.strftime(polishDate, '%Y/%m/%d')
            print(usaDate)
            return
        except:
            pass
    print("I did not find the matching date[dd.mm.yyyy].")
    return

text = str(pyperclip.paste())
matches = []

for groups in dateRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to the clipboard: ')
    print('\n'.join(matches))
    changeFormatDate()

else:
    print('I did not find the matching date.')