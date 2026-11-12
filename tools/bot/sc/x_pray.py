import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
def settle():
    for i in range(8):
        s = M()
        top = s.split('\n')[0]
        if 'Заставить' in top:
            K(force); continue
        time.sleep(0.4); K('\x1b', quiet=0.6)
def pray(t):
    ext('pray'); K('y', t); settle(); S(t + ' end')
force = 'n'
pray('pray1')
R = W('cursed ring of teleportation'); K('P'); K(R); M(); K('r'); M()
force = 'y'
pray('pray2')
pray('pray3')
L = W('cursed long sword'); K('w'); K(L); M()
pray('pray4')
pray('pray5')
K('i', 'inv'); M()
