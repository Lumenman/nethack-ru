import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
L = W('3 potions of extra healing')
K('q'); K(L, 'quaff'); M()
L = W('potion of healing')
K('q'); K(L, 'quaff2'); M()
