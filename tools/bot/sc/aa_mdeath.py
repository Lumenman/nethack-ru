import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
# death and the end-of-game screens: reason of death, tombstone, final ^X.
# NHMON=<monster> picks the killer (default minotaur); NHMON=geno reads a
# scroll of genocide against the hero's own race instead.
MON = os.environ.get('NHMON', 'минотавр')
if MON == 'trice':  # pick up a cockatrice corpse bare-handed
    W('труп василиска'); K(',', 'pickup', quiet=1.0)
elif MON == 'geno':
    L = W('uncursed scroll of genocide'); K('r'); K(L, quiet=1.0); M(); S('prompt'); K('человек' + CR, 'geno', quiet=1.0)
else:
    for _ in range(3):
        K('\x07'); K('hostile ' + MON + CR, 'gen'); M()
for n in range(40):
    if not b.alive():
        break
    if MON not in ('geno', 'trice'):
        K('ms', quiet=0.5)
    for _ in range(80):
        if not b.alive():
            break
        s = b.screen()
        top = s.split('\n')[0]
        msgs.append(top)
        if 'Die?' in s or 'Умереть?' in s:
            K('y', 'die yes', quiet=1.0)
        elif '[ynq]' in s or '[yn]' in s or '[ynaq]' in s:
            S('question'); K('y', quiet=1.0)
        elif 'Дальше' in s or '--More--' in s:
            S('more'); K(CR, quiet=0.6)
        elif is_pause(s):
            S('pause'); K(CR, quiet=0.8)
        elif '(конец)' in s or '(end)' in s:
            S('menu'); K(CR, quiet=0.8)
        elif 'Ур.:' in s.split('\n')[-1] or 'Ур.:' in s.split('\n')[-2]:
            break
        else:
            S('other screen'); K(CR, quiet=0.8)
S('end')
