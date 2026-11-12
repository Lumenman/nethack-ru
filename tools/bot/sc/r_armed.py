import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
for m in ['hostile холмовой орк', 'hostile горный орк', 'hostile урок-хай', 'hostile орк-капитан', 'hostile гном-лорд']:
    K('\x07'); K(m + CR); M()
for r in range(10):
    for d in 'hjklyubn':
        K('F'); K(d); M()
