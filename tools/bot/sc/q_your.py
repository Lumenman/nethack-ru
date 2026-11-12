import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
for wpn in ['spear', 'pick-axe', 'pair of lenses']:
    L = W(wpn)
    K('w'); K(L); M()
    R = W('scroll of enchant weapon')
    K('r'); K(R, 'read ' + wpn); M(); K(''); M()
L = W('egg')
K('\x09'); K('\x09'); K('\r'); M()
K('i', 'inventory'); M()
