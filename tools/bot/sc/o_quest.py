import os, re
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
K('\x16', quiet=0.8); K('?' + CR, quiet=1.2); K('>', quiet=0.8)
K('y', quiet=0.5); K(CR, quiet=2.5); S('arrived')
for _ in range(14):
    s = b.screen(); msgs.append(s.split('\n')[0])
    if 'Дальше' in s or 'More' in s:
        S('more'); K(CR, quiet=0.8)
    else:
        break
S('after arrival')
K('s', quiet=1.5); S('after wait')
for _ in range(14):
    s = b.screen(); msgs.append(s.split('\n')[0])
    if 'Дальше' in s or 'More' in s:
        S('more2'); K(CR, quiet=0.8)
    else:
        break
