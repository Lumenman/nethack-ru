for w in ['волшебный свисток', 'масляная лампа']:
    K('\x17', quiet=0.8); S('after ^W')
    K(w, quiet=0.8); S('typed ' + w)
    K(CR, quiet=1.5); S('entered')
    M()
