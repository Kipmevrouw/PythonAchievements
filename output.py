Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> # Verander <JOUW NAAM HIER> in je eigen naam
>>> print('MIjn naam is Becky')
MIjn naam is Becky
>>> naam = 'Becky'
>>> print(naam)
Becky
>>> print(naam.upper())
BECKY
>>> print(naam[0:2])
Be
>>> print(naam[::-1])
ykceB
>>> # Verander dit in je eigen leeftijd
>>> leeftijd = 16
>>> print('Hallo ' + naam + 'ben je al + str(leeftijd) + ' jaar?')
      
SyntaxError: invalid syntax
>>> print('Hallo ' + naam + 'ben je al + str(leeftijd) + ' jaar?')
      
SyntaxError: invalid syntax
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo Becky ben je al 16 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
17
>>> leeftijd-=1
>>> leeftijd
16
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')

	
Over 2 jaar wordt je 18
>>> elif leeftijd > 18:
	
SyntaxError: invalid syntax
>>> if leeftijd < 18:
    hoelang_tot18jaar = 18 - leeftijd
    print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
elif leeftijd > 18:
    hoelang_al18jaar = leeftijd - 18
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
else:
    print('Je bent precies ' + str(leeftijd) + ' jaar')

    
Over 2 jaar wordt je 18
>>> # Willekeurige getallen genereren
from random import randint
randint(0,1000)
willekeurig_getal = randint(0,1000)
willekeurig_getal
print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
SyntaxError: multiple statements found while compiling a single statement
>>> randint(0,1000)
willekeurig_getal = randint(0,1000)
willekeurig_getal
print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))

SyntaxError: multiple statements found while compiling a single statement
>>> # willekeurige getallen genereren
>>> from random import randint
>>> randint(0.1000)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    randint(0.1000)
TypeError: randint() missing 1 required positional argument: 'b'
>>> randint(0,1000)
64
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
367
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 367
>>> # Datum en tijd
>>> from datetime import datetime

>>> datum = datetime.now()

>>> print(datum)

2020-09-16 14:23:56.194994
>>> datum.strftime('%A %d %B %Y')

'Wednesday 16 September 2020'
>>> # Nu in een andere taal

>>> import locale

>>> locale.setlocale(locale.LC_TIME, 'nl_NL')

'nl_NL'
>>> datum.strftime('%A %d %B %Y')

'woensdag 16 september 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')

'it_IT'
>>> datum.strftime('%A %d %B %Y')

'mercoledì 16 settembre 2020'
>>> 