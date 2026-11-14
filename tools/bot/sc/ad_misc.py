import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
# small checks: counted items on the floor, a monster wielding a pick-axe
L = W('2 food rations'); K('d'); K(L); M(); K(':', 'look 2 rations'); M()
L = W('pick-axe'); K('d'); K(L); M()
K('\x07'); K('hostile дварф' + CR, 'gen'); M()
K('h'); M(); K('l'); M()
for i in range(12):
    if 'Die?' in b.screen():
        K('n'); M()
    K('ms', quiet=0.3); M()
K(':', 'look end'); M()
