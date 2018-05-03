ab = {'Swaroop': 'swaroopch@ byteofpython.info',
      'Larry': 'larry@ wall.org',
      'M atsum oto': 'm atz@ ruby-lang.org',
      'Spam m er': 'spam m er@ hotm ail.com '
      }
print("Swaroop's address is % s" % ab['Swaroop'])
# Adding a key/value pair
ab['G uido'] = 'guido@ python.org'
# D eleting a key/value pair
del ab['Spam m er']
print( '\nThere are % d contacts in the address-book\n' % len(ab))
for name, address in ab.items():
	print('Contact % s at % s' % (name, address))
if 'G uido' in ab:  # OR ab.has_key('Guido')
	print ("\nG uido's address is % s" % ab['G uido'])
