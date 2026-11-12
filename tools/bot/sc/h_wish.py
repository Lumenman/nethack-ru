import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
for w in ['long sword', 'blessed +2 long sword', '2 daggers', 'wand of fire', 'wand of digging',
          'potion of water', '3 potions of healing', 'scroll of enchant armor', 'ring of levitation',
          'spellbook of force bolt', 'amulet of strangulation', 'magic whistle', 'oil lamp',
          'cream pie', 'lump of royal jelly', 'elven mithril-coat', 'speed boots', 'Hawaiian shirt',
          'комок маточного молочка', 'зелье воды', 'благословенный волшебный свисток', 'амулет удушения']:
    W(w)
