import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
for w in ['potion of healing', 'potion of sleeping', 'potion of speed', 'potion of gain level',
          'ring of levitation', 'ring of conflict', 'ring of regeneration',
          'wand of fire', 'wand of digging', 'wand of light',
          'spellbook of force bolt', 'spellbook of sleep', 'spellbook of identify']:
    W(w)
K('i', 'inventory')
