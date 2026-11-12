import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
K('\x16'); K('?' + CR); K('>'); K('w', 'minetown'); M()
P = W('blessed potion of monster detection'); K('q'); K(P); M(); K('\x1b'); M()
W('2000 gold pieces')
def to_shk(d):
    K('\x14')
    for i in range(60):
        top = K('m').split('\n')[0]
        if 'shopkeeper' in top:
            msgs.append('SHK ' + top)
            break
    else:
        K('\x1b'); return False
    K(d); K('.'); M()
    return True
inshop = False
for d in 'hjklyubn':
    if not to_shk(d):
        break
    s = K(':', 'look ' + d); M()
    if 'зоркмид' in s or 'бесплатно' in s or 'на продажу' in s:
        inshop = True; break
msgs.append('INSHOP %s' % inshop)
opp = {'h':'l','l':'h','j':'k','k':'j','y':'n','n':'y','u':'b','b':'u'}
if inshop:
    K(','); S('pick'); M()
    if 'подобрать' in b.screen().lower():
        K('.'); K(CR); M()
    K('i', 'inv'); M()
    ext('chat'); K(opp[d], 'chat'); M()
    K('p', 'pay'); M()
    if 'платить' in b.screen():
        K('.'); K(CR); M()
    K('y'); M(); M()
    for w in ['scroll of light', 'dagger', 'blessed potion of healing']:
        D = W(w)
        K('d'); K(D, 'sell ' + w); M(); K('y'); M()
    K('$', 'gold'); M()
    K(opp[d]); M(); K(opp[d]); M()
