ext('quit'); S('quit q')
for _ in range(30):
    if not b.alive(): break
    s = b.screen()
    msgs.append(s.split('\n')[0])
    if '[yn' in s and ('выйти' in s.lower() or 'Действительно' in s):
        K('y', 'confirm quit', quiet=1.0)
    elif '[ynq]' in s or '[yn]' in s:
        K('n', quiet=0.8)
    else:
        S('screen'); K(CR, quiet=0.8)
