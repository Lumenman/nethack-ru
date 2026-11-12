import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
t = W('банка шпината')
T('e', 'eat prompt'); T('d', 'eat ration', quiet=1.0)
for _ in range(8):
    M(); K('s', quiet=0.3)
S('after eating')
if t:
    T('e', 'eat prompt2'); T(t, 'open tin', quiet=1.0)
    for _ in range(10):
        s = b.screen()
        if '[yn' in s: K('y', quiet=0.8)
        M(); K('s', quiet=0.3)
w = W('wand of огонь')
if w:
    T('a', 'apply prompt'); T(w, 'apply wand')
    if 'сломать' in b.screen().split('\n')[0]:
        T('y', 'break wand yes', quiet=1.0)
