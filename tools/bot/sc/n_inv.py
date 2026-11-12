import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
for w in ['Mjollnir', 'Cleaver', 'Magicbane', 'Grayswandir', 'potion of healing', 'long sword']:
    W(w)
K('i', 'inv', quiet=1.2); K(' ', 'inv2', quiet=1.0); esc()
K(chr(92), 'disco', quiet=1.0); K(' ', 'disco2', quiet=1.0); esc(3)
W('Экскалибур')
