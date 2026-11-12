import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
K('\x16', 'ctrlv')
K('?' + CR, 'menu')
K('>', 'menu2')
K('\x1b'); K('\x1b')
