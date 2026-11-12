import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
T('E', 'engrave'); T('-', 'fingers')
K('abc' + CR, quiet=0.8); M()
ext('polyself'); S('poly prompt')
K('маленькая собака' + CR, quiet=1.0); S('poly done'); M()
T('w', 'wield prompt'); T('-', 'empty paws')
T('W', 'wear prompt'); esc()
T('P', 'puton'); esc()
T('\x18', 'attributes as dog', quiet=1.0); esc(3)
T('/', 'whatis menu', quiet=1.0); esc(3)
w = W('wand of огонь')
if w:
    T('a', 'apply prompt'); T(w, 'apply wand')
    if 'сломать' in b.screen().split('\n')[0]:
        T('y', 'break wand yes', quiet=1.0)
