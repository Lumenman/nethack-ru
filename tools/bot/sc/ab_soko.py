import os, random
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
# Sokoban: boulder pushing, squeezing, holes; unique messages go to the log.
# NHSOKO picks the level letter in the ^V menu (default: first Sokoban level).
K('\x16'); K('?' + CR, quiet=0.8); S('levels'); K('>', 'levels2', quiet=0.8)
s = b.screen()
letter = os.environ.get('NHSOKO')
if not letter:
    for line in s.split('\n'):
        m = re.match(r'\s*([a-zA-Z]) - .*(Сокобан|soko)', line)
        if m:
            letter = m.group(1)
            break
msgs.append('SOKO LETTER %s' % letter)
K(letter or '\x1b', 'soko', quiet=1.0); M()
K(':', 'look'); M()
random.seed(int(os.environ.get('NHSEED', '1')))
seen = set()
for n in range(int(os.environ.get('NHSTEPS', '300'))):
    if not b.alive():
        break
    if 'Die?' in b.screen():
        K('n', quiet=0.3); M()
    d = random.choice('hjklhjklyubn')
    K(d, quiet=0.15)
    s = b.screen()
    top = s.split('\n')[0].strip()
    if top and top not in seen:
        seen.add(top)
        S('step %d %s' % (n, d))
    if '[yn' in s:  # wizard mode: refuse to die, agree to the rest
        K('n' if 'Die?' in s else 'y', quiet=0.3)
    M()
K(':', 'look end'); M()
K('\x0f', 'overview'); M()
