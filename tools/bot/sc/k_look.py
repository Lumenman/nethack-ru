import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
sw = W('long sword'); wd = W('wand of fire')
# drop sword, step east, look west at it
T('d' + sw, 'drop sword'); K('l', quiet=0.6); M()
T(';', 'farlook'); K('h', quiet=0.3); K('.', quiet=1.0); S('look sword'); M()
for _ in range(3):
    s = b.screen()
    if 'Подробнее' in s or '[yn' in s:
        K('y', 'more info yes', quiet=1.2); M(); esc()
# wand unidentified, then identified
K('h', quiet=0.6); M()
T(',', 'pickup'); esc()
T('d' + wd, 'drop wand'); K('l', quiet=0.6); M()
T(';', 'farlook wand'); K('h', quiet=0.3); K('.', quiet=1.0); S('look wand unid'); M(); esc()
ext('wizidentify'); K('_', quiet=0.5); S('wizid menu'); esc(3)
K('h', quiet=0.5); M(); T(',', 'pickup2', quiet=0.8); esc(); 
T(chr(92), 'discoveries', quiet=1.0); esc(3)
