import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
K('\x16', quiet=0.8); K('?' + CR, quiet=1.2); K('>', quiet=0.6); K('>', quiet=0.6); S('page3')
s = b.screen()
import re
pick = None
for line in s.split('\n'):
    m = re.match(r'\s*([a-zA-Z]) - .*tut-1', line)
    if m: pick = m.group(1)
msgs.append('PICK ' + str(pick))
if pick:
    K(pick, quiet=0.5); K(CR, quiet=2.5); M()
    K(':', 'look here', quiet=1.0); M()
