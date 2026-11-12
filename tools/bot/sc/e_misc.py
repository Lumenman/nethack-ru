import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())

# engrave in dust, step away, farlook the spot
T('E', 'engrave'); T('-', 'fingers')
K('Здесь был Тест' + CR, quiet=0.8); M()
for d in 'lhjk':
    K(d, quiet=0.6); M()
    if b.screen().split('\n')[0].strip() == '':
        break
S('moved')
T(';', 'farlook'); K('hjklyubn'[0], quiet=0.3)
for d in 'hlkj':
    pass
S('cursor')
# try the four neighbours until the description mentions the engraving
for back in ['h', 'l', 'j', 'k']:
    K(';', quiet=0.4); K(back, quiet=0.3); K('.', quiet=0.8)
    S('farlook ' + back); M()
# '/' menu
T('/', 'whatis menu', quiet=1.0); esc(3)
T('/m', 'list monsters', quiet=1.0); esc(3)
T('/o', 'list objects', quiet=1.0); esc(3)
T('/t', 'list traps', quiet=1.0); esc(3)
T('/e', 'list engravings', quiet=1.0); esc(3)
# break a wand -> explosion
w = W('wand of огонь')
if w:
    T('a', 'apply prompt'); T(w, 'apply wand')
    top = b.screen().split('\n')[0]
    if 'сломать' in top:
        T('y', 'break wand yes', quiet=1.0)
# polymorph into a dog and look at body parts
ext('polyself'); S('poly prompt')
K('собака' + CR, quiet=1.0); S('poly done'); M()
T('w', 'wield prompt'); T('-', 'empty paws')
T('\x18', 'attributes as dog', quiet=1.0); esc(3)
