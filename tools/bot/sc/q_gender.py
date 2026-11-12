import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
for w in ['cursed rusty pick-axe', 'blessed +2 spear', 'uncursed greased leather armor',
          '5 poisoned arrows', 'cursed burnt fireproof quarterstaff', 'pair of lenses',
          'blessed elven boots', 'cursed potion of water', 'uncursed rustproof +1 dagger',
          'very rotted leather gloves', 'blessed figurine of a gnome', 'cursed spellbook of sleep']:
    W(w)
L = W('blessed +0 long sword')
K('w'); K(L, 'wield'); M()
L = W('uncursed scroll of enchant weapon')
K('r'); K(L, 'read'); M()
K('i', 'inventory'); M()
