import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
for i in range(8):
    W('tin')
W('3 tins')
K('\x09'); K('\x09'); K('\r'); M()
K('i', 'inventory'); M()
