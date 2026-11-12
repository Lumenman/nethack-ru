import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())

wand = W('wand of огонь')
S('got wand')
done = False
for n in range(12):
    if not b.alive():
        break
    K('z', quiet=0.6)
    top = b.screen().split('\n')[0]
    if 'взмахнуть' not in top and 'zap' not in top and '?' not in top:
        S('zap prompt odd'); esc(); continue
    K(wand, quiet=0.6)
    K('.', quiet=1.0)
    S('zap self %d' % n)
    # walk through messages; answer death questions
    for _ in range(60):
        if not b.alive():
            done = True
            break
        s = b.screen()
        top = s.split('\n')[0]
        msgs.append(top)
        if 'Die?' in s:
            K('y', 'die yes', quiet=1.0)
        elif '[ynq]' in s or '[yn]' in s or '[ynaq]' in s:
            S('question'); K('y' if 'Покажи' in s or 'показ' in s.lower() else 'n', quiet=1.0)
        elif 'Дальше' in s or '--More--' in s:
            K(CR, quiet=0.6)
        elif is_pause(s):
            S('pause'); K(CR, quiet=0.8)
        elif 'Ур.:' in s.split('\n')[-1]:
            break
        else:
            S('other screen'); K(CR, quiet=0.8)
    if done:
        break
S('end')
