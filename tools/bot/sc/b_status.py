import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())

def status():
    lines = b.screen().split('\n')
    return lines[-2] + ' || ' + lines[-1]

msgs.append('STATUS0: ' + status())
for w in ['зелье замешательства', 'зелье галлюцинации', 'кольцо левитации', 'ring of левитация',
          'зелье слепоты', 'зелье оглушения']:
    msgs.append('LETTER ' + w + ' = ' + str(W(w)))
inv = b.screen()
K('i', 'inventory', quiet=1.0); esc()
# quaff all potions we got, one per letter guess from log
for letter in 'efghijk':
    K('q', quiet=0.6)
    s = b.screen()
    if 'выпить' in s.split('\n')[0] or 'пить' in s.split('\n')[0]:
        T(letter, 'quaff ' + letter)
        msgs.append('STATUS: ' + status())
    else:
        esc()
for letter in 'efghijk':
    K('P', quiet=0.6)
    top = b.screen().split('\n')[0]
    if 'надеть' in top:
        T(letter, 'put on ' + letter)
        top = b.screen().split('\n')[0]
        if 'руку' in top or 'Какую' in top:
            T('l', 'left hand')
        msgs.append('STATUS: ' + status())
        break
    esc()
S('status after effects')
msgs.append('STATUS: ' + status())
# terrain / weapon status options
ext('optionsfull'); S('options full'); esc(3)
K('O', 'options menu', quiet=1.0)
for i in range(6):
    K('>', 'options page %d' % (i + 2), quiet=0.8)
esc(3)
