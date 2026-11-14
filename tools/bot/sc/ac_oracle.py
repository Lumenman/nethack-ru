import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
# Oracle: level sounds, fountains/statues look, minor and major consultation
K('\x16'); K('?' + CR, 'levels', quiet=0.8)
s = b.screen()
letter = None
for line in s.split('\n'):
    m = re.match(r'\s*([a-zA-Z]) - .*oracle', line)
    if m:
        letter = m.group(1)
msgs.append('ORACLE LETTER %s' % letter)
K(letter or '\x1b', 'oracle', quiet=1.0); M()
P = W('blessed potion of monster detection'); K('q'); K(P); M(); K('\x1b'); M()
W('5000 gold pieces')
opp = {'h': 'l', 'l': 'h', 'j': 'k', 'k': 'j', 'y': 'n', 'n': 'y', 'u': 'b', 'b': 'u'}


def to_oracle(d):
    K('\x14')
    for i in range(60):
        top = K('m').split('\n')[0]
        if 'Oracle' in top or 'Оракул' in top or 'оракул' in top:
            msgs.append('ORC ' + top)
            break
    else:
        K('\x1b'); return False
    K(d); K('.'); M()
    return True


def answer(seq):
    """walk through the consultation prompts with the given y/n answers"""
    for _ in range(40):
        s = b.screen()
        top = s.split('\n')[0]
        msgs.append(top)
        if '[yn' in s or '[ynq' in s:
            S('prompt'); K(seq.pop(0) if seq else 'n', quiet=0.8)
        elif 'Дальше' in s or '--More--' in s or '(конец)' in s or is_pause(s):
            S('text'); K(CR, quiet=0.6)
        else:
            break


for d in 'hjkl':
    if to_oracle(d):
        K(';'); K(opp[d]); K('.', 'farlook'); M()
        ext('chat'); K(opp[d], 'chat1', quiet=0.8); answer(['y'])
        ext('chat'); K(opp[d], 'chat2', quiet=0.8); answer(['n', 'y'])
        break
for i in range(30):
    K('s', quiet=0.2); M()
K(':', 'look'); M()
