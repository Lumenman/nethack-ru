"""List / rewrite mon_nam() and y_monnam() arguments of pline-like calls
by the word in the format string right before their %s (CP1251 sources).
    python -X utf8 tools/monsites.py list src/*.c
        -> counts of preceding words with a sample file:line
    python -X utf8 tools/monsites.py apply "по=BP_DAT,в=BP_ACC" src/*.c
        -> mon_nam(x) -> mon_nam_case(x, BP_DAT) after "по %s", ...
Only literal format strings are seen; review the diff afterwards."""
import re, sys, collections

FUN = re.compile(r'\b(pline|You|Your|You_hear|You_see|You_feel|pline_The|There|Sprintf|Strcpy|verbalize|Norep|custompline|pline_mon|You_cant|impossible)\s*\(')


def split_args(s):
    """split a C argument list at top-level commas; returns list of (text, start)"""
    out, depth, cur, start, i, q = [], 0, '', 0, 0, None
    while i < len(s):
        c = s[i]
        if q:
            cur += c
            if c == '\\':
                cur += s[i + 1]; i += 1
            elif c == q:
                q = None
        elif c in '"\'':
            q = c; cur += c
        elif c in '([{':
            depth += 1; cur += c
        elif c in ')]}':
            if depth == 0:
                out.append((cur, start)); return out, i
            depth -= 1; cur += c
        elif c == ',' and depth == 0:
            out.append((cur, start)); cur = ''; start = i + 1
        else:
            cur += c
        i += 1
    return out, i


def calls(text):
    for m in FUN.finditer(text):
        args, end = split_args(text[m.end():])
        yield m, args, m.end()


def fmt_of(args):
    """index of the first argument that is a string literal concatenation"""
    for k, (a, _) in enumerate(args):
        if re.match(r'\s*"', a):
            lit = ''.join(re.findall(r'"((?:[^"\\]|\\.)*)"', a))
            return k, lit
    return None, None


def sites(text):
    for m, args, base in calls(text):
        k, lit = fmt_of(args)
        if k is None:
            continue
        specs = [mm for mm in re.finditer(r'%[-+ #0-9.*]*l?[sdcuxlf]', lit)]
        for n, sm in enumerate(specs):
            ai = k + 1 + n
            if ai >= len(args):
                break
            a, st = args[ai]
            am = re.match(r'(\s*)(mon_nam|Monnam|y_monnam|Y_monnam)\((.*)\)\s*$', a, re.S)
            if not am or sm.group() != '%s':
                continue
            before = lit[:sm.start()]
            word = re.findall(r'(\S+)\s*$', before)
            yield word[0].lower() if word else '^', base + st + len(am.group(1)), am


def main():
    mode = sys.argv[1]
    if mode == 'list':
        cnt, ex = collections.Counter(), {}
        for f in sys.argv[2:]:
            t = open(f, 'rb').read().decode('cp1251')
            for w, pos, am in sites(t):
                cnt[w] += 1
                ex.setdefault(w, '%s:%d' % (f.split('/')[-1], t.count('\n', 0, pos) + 1))
        for w, c in cnt.most_common():
            print(c, w, ex[w])
    else:
        mp = dict(x.split('=') for x in sys.argv[2].split(','))
        total = 0
        for f in sys.argv[3:]:
            t = open(f, 'rb').read().decode('cp1251')
            edits = [(pos, am, mp[w]) for w, pos, am in sites(t) if w in mp and am.group(2) in ('mon_nam', 'y_monnam')]
            for pos, am, case in sorted(edits, key=lambda e: -e[0]):
                old = am.group(0).lstrip()
                new = '%s_case(%s, %s)' % (am.group(2), am.group(3), case)
                assert t[pos:pos + len(old)] == old, (f, pos)
                t = t[:pos] + new + t[pos + len(old):]
                total += 1
            open(f, 'wb').write(t.encode('cp1251'))
        print(total, 'rewritten')


main()
