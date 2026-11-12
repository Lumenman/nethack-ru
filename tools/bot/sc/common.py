import re


def wait_top(pred, timeout=4.0):
    t0 = time.time()
    while time.time() - t0 < timeout:
        top = b.screen().split('\n')[0]
        if pred(top):
            return top
        time.sleep(0.1)
    return b.screen().split('\n')[0]


def W(text):
    """Wish; return inventory letter or None."""
    K('\x17')
    wait_top(lambda t: 'желаете' in t)
    K(text + CR, quiet=0.6)
    top = wait_top(lambda t: re.match(r'\s*[a-zA-Z$] - ', t) or 'желаете' in t
                   or 'Ничего' in t or 'Дальше' in t or 'More' in t)
    msgs.append('WISH[' + text + '] -> ' + top)
    if 'желаете' in top and 'Ничего' not in top:
        K('\x1b', quiet=0.6)
        M()
        return None
    m = re.match(r'\s*([a-zA-Z]) - ', top)
    M()
    if not m:
        s = b.screen()
        if 'желаете' in s.split('\n')[0]:
            K('\x1b', quiet=0.6)
            M()
    return m.group(1) if m else None


def T(keys, title, quiet=0.6):
    """Send keys, log, then dismiss --More-- collecting messages."""
    K(keys, quiet=quiet)
    S(title)
    M()
    return b.screen()


def esc(n=2):
    for _ in range(n):
        K('\x1b', quiet=0.3)
    M()
