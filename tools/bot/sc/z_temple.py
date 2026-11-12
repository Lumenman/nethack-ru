import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
K('\x16'); K('?' + CR); K('>'); K('w', 'minetown'); M()
P = W('blessed potion of monster detection'); K('q'); K(P); M(); K('\x1b'); M()
W('3000 gold pieces')
opp = {'h':'l','l':'h','j':'k','k':'j','y':'n','n':'y','u':'b','b':'u'}
found = None
for d in 'hjklyubn':
    K('\x14')
    for i in range(60):
        top = K('m').split('\n')[0]
        if '[priest' in top or 'жрец' in top or 'жрица' in top:
            msgs.append('PRIEST ' + top); break
    else:
        K('\x1b'); break
    K(d); K('.'); M()
    ext('chat'); s = K(opp[d], 'chat ' + d); M()
    top = b.screen().split('\n')[0]
    msgs.append('CHAT ' + top)
    if 'пожертв' in top or 'Сколько' in top:
        K('400' + CR, 'donate'); M(); found = d; break
    K('\x1b'); M()
K('\x14'); K('_'); K('.', 'to altar'); M()
K(':', 'look altar'); M()
C = W('труп шакала')
ext('offer'); S('offerq'); K('y'); M(); K(C); M(); M()
ext('pray'); K('y'); 
for i in range(6):
    s = M()
    if 'Заставить' in s.split('\n')[0]:
        K('y')
    time.sleep(0.5)
K('\x18', 'attr'); K(' '); K(' '); M()
