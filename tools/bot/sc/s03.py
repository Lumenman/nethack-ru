for w in ['wand of огонь', 'копание', 'огонь', 'зелье воды', 'potion of вода', 'кремовый пирог', 'амулет удушения']:
    K('\x17'); K(w + CR, quiet=0.8)
    s = b.screen()
    msgs.append('WISH[' + w + '] -> ' + s.split('\n')[0])
    if 'Чего вы желаете' in s:
        K('\x1b', quiet=0.8); M()
        msgs.append('   after esc: ' + b.screen().split('\n')[0])
    else:
        M()
K('i', 'inv', quiet=1.0); K('\x1b')
