import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
for r in range(3):
    for d in 'hjklyubn':
        K('F'); K(d); M()
        if 'атаковать' in b.screen().split('\n')[0]:
            K('y'); M()
P = W('potion of hallucination'); K('q'); K(P); M()
L = W('scroll of taming')
for r in range(2):
    K('r'); K(L); M()
    for d in 'hjklyubn':
        K('F'); K(d); M()
        if 'атаковать' in b.screen().split('\n')[0]:
            K('y'); M()
    L = W('scroll of taming')
