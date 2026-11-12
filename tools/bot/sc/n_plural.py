import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
for w in ['3 potions of healing', '2 potions of sleeping', '2 scrolls of identify', '5 potions of speed']:
    W(w)
