import ephem 
from datetime import date

mars = ephem.Mars(date.today())
print(ephem.constellation(mars))

planets = ['venus','mercury', 'earth', 'mars', 'jupiter', 'saturn', 'uranus','pluto']

mrs = planets[7].title()
test_str = str('ephem.' + mrs + '(date.today())')
print(ephem.constellation(eval(test_str)))