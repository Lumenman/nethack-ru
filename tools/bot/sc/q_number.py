import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
for w in ['2 potions of healing', '3 cursed potions of sleeping', '5 potions of speed',
          '11 potions of see invisible', '21 potions of fruit juice', '22 blessed potions of water',
          '2 cursed poisoned arrows', '5 poisoned arrows', '21 arrows', '3 daggers', '6 daggers',
          '2 scrolls of identify', '7 scrolls of light', '2 rubies', '5 rocks', '3 cream pies',
          '4 eggs', '2 tins', '3 candles', '12 gold pieces', '3 apples', '5 food rations']:
    W(w)
K('\x09'); K('\x09'); K('\r'); M()
K('i', 'inventory'); M()
L = W('3 daggers')
K('t'); K(L); K('l', 'throw'); M()
