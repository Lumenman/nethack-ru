import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
T('E', 'e1'); T('-', 'e2 fingers')
K('abc' + CR, 'e3'); M()
m = W('волшебный маркер')
T('E', 'e4'); T(m, 'e5 marker')
K('xyz' + CR, 'e6'); M()
