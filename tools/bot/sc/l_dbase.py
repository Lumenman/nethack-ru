import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
def answer_more(tag):
    for _ in range(8):
        s = b.screen(); top = s.split('\n')[0]; msgs.append(top)
        if 'Подробнее' in top or '[yn' in top:
            K('y', tag + ' info yes', quiet=1.5)
        elif 'Дальше' in s or 'More' in s:
            K(CR, quiet=0.6)
        else:
            break
sw = W('long sword')
T('t' + sw, 'throw'); K('l', quiet=1.0); M()
K('/', quiet=0.6); K('/', quiet=0.6); M(); K('o', quiet=0.4); S('cursor on obj'); K('.', quiet=1.2); S('whatis sword')
answer_more('map'); esc(3)
K('/', quiet=0.6); K('?', quiet=0.8); S('specify'); K('длинный меч' + CR, quiet=1.2); S('typed en')
answer_more('typed'); esc(3)
