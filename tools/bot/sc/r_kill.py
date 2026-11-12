import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
for m in ['hostile гном-королева', 'hostile гном-лорд', 'hostile гном-королева', 'котёнок', 'шакал', 'hostile орк-капитан', 'летучая мышь']:
    K('\x07'); K(m + CR, 'gen ' + m); M()
L = W('5 daggers')
for r in range(8):
    for d in 'hjklyubn':
        K('F'); K(d); M()
    K('t'); K('b'); K('hjkl'[r % 4]); M()
K(':', 'look'); M()
