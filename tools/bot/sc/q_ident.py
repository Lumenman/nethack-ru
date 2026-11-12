import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
for w in ['potion of blindness', 'potion of healing', 'potion of water', 'scroll of enchant weapon',
          'wand of fire', 'wand of make invisible', 'ring of levitation', 'ring of fire resistance',
          'spellbook of force bolt', 'amulet of life saving', 'blessed potion of water', 'cursed potion of water', 'scroll of blank paper', 'spellbook of blank paper', 'spellbook of fireball', 'wand of create monster']:
    W(w)
K('\x09', 'ident'); M()
K('i', 'inventory'); M()
