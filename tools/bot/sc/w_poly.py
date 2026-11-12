import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
def poly(name):
    ext('polyself'); S('pq ' + name)
    K(name + CR, 'poly ' + name); M()
for f in ['огненный элементаль', 'красный дракон', 'нимфа', 'вампир', 'гном-король', 'кокатрикс', 'летучая мышь', 'железный голем']:
    poly(f)
    K('\x07'); K('hostile шакал' + CR); M()
    for d in 'hjklyubn':
        K('F'); K(d); M()
    K('\x18', 'attr ' + f); K(' '); K(' '); M(); K('\x1b')
