"""Generate include/moncase_ru.h: case forms of Russian monster names that
src/do_name.c mon_paradigms[] does not list by hand.  Nouns come from
pymorphy3 when it knows the word, otherwise from ending rules; adjectives
always from ending rules.
    python -X utf8 tools/gen_moncase.py [--review]"""
import re, os, sys
import pymorphy3

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASES = ['nomn', 'gent', 'datv', 'accs', 'ablt', 'loct']
M = pymorphy3.MorphAnalyzer()
VELAR, HUSH = 'гкх', 'жшчщ'
ADJ_ENDS = ('ый', 'ий', 'ой', 'ая', 'яя', 'ое', 'ее')
INDECL = {'леди', 'хай', 'зомби', 'Сато'}
ANIM = {'скелет', 'оракул', 'Мор', 'Голод', 'жучок'}  # monsters, though inanimate words
COMMON = {'убийца'}  # nouns of common gender
NOT_ADJ = {'титанотерий', 'балухитерий', 'Пелий'}  # nouns ending like adjectives
KEEP_TAIL = {'Мордора', 'Йендора', 'Воров', 'Хухетотла'}
# nouns pymorphy gets wrong: gender, animate, 6 singular, 6 plural forms
NOUNS = {
    'элементаль': ('masc', True,
                   'элементаль элементаля элементалю элементаля элементалем элементале',
                   'элементали элементалей элементалям элементалей элементалями элементалях'),
}
# whole names: 6 singular forms
WHOLE = {
    'Тот Амон': 'Тот Амон|Тота Амона|Тоту Амону|Тота Амона|Тотом Амоном|Тоте Амоне',
    'Неферет Зелёная': 'Неферет Зелёная|Неферет Зелёной|Неферет Зелёной|'
                       'Неферет Зелёную|Неферет Зелёной|Неферет Зелёной',
    'Двацветок': 'Двацветок|Двацветка|Двацветку|Двацветка|Двацветком|Двацветке',
    'шаман Карнов': 'шаман Карнов|шамана Карнова|шаману Карнову|шамана Карнова|шаманом Карновым|шамане Карнове',
    'Асикага Такаудзи': '|'.join(['Асикага Такаудзи'] * 6),
}

# adjective endings: type -> gender -> 6 cases ('-': accusative by animacy)
ADJ = {
    'hard': {'m': 'ый ого ому - ым ом', 'f': 'ая ой ой ую ой ой',
             'n': 'ое ого ому ое ым ом', 'p': 'ые ых ым - ыми ых'},
    'hardo': {'m': 'ой ого ому - ым ом', 'f': 'ая ой ой ую ой ой',
              'n': 'ое ого ому ое ым ом', 'p': 'ые ых ым - ыми ых'},
    'velar': {'m': 'ий ого ому - им ом', 'f': 'ая ой ой ую ой ой',
              'n': 'ое ого ому ое им ом', 'p': 'ие их им - ими их'},
    'velaro': {'m': 'ой ого ому - им ом', 'f': 'ая ой ой ую ой ой',
               'n': 'ое ого ому ое им ом', 'p': 'ие их им - ими их'},
    'hush': {'m': 'ий его ему - им ем', 'f': 'ая ей ей ую ей ей',
             'n': 'ее его ему ее им ем', 'p': 'ие их им - ими их'},
    'husho': {'m': 'ой ого ому - им ом', 'f': 'ая ой ой ую ой ой',
              'n': 'ое ого ому ое им ом', 'p': 'ие их им - ими их'},
    'soft': {'m': 'ий его ему - им ем', 'f': 'яя ей ей юю ей ей',
             'n': 'ее его ему ее им ем', 'p': 'ие их им - ими их'},
}
GK = {'masc': 'm', 'femn': 'f', 'neut': 'n'}


def is_adj(w):
    if w in NOT_ADJ:
        return False
    b = w[:-2] if len(w) > 5 and w.endswith('ся') else w
    return len(b) >= 4 and b.endswith(ADJ_ENDS)


def adj_form(w, g, num, ci, anim):
    sja = ''
    if len(w) > 5 and w.endswith('ся'):
        w, sja = w[:-2], 'ся'
    stem, e = w[:-2], w[-2:]
    c = stem[-1]
    if c in VELAR:
        t = 'velaro' if e == 'ой' else 'velar'
    elif c in HUSH:
        t = 'husho' if e == 'ой' or (e in ('ая', 'ое') and c in 'шж') else 'hush'
    elif e in ('ий', 'яя', 'ее'):
        t = 'soft'
    else:
        t = 'hardo' if e == 'ой' else 'hard'
    ends = ADJ[t]['p' if num == 'plur' else g].split()
    end = ends[ci]
    if end == '-':  # accusative of masculine / plural
        end = ends[1 if anim else 0]
    return stem + end + sja


def rule_noun(w, num, ci, anim):
    """declension by ending for words pymorphy does not know"""
    low = w.lower()
    if low[-1] in 'оеиуюэы' or w in INDECL:
        return w
    if low[-1] in 'ая':
        st, soft = w[:-1], low[-1] == 'я'
        k = 'и' if (soft or st[-1] in VELAR + HUSH) else 'ы'
        de = 'и' if soft and st[-1] == 'и' else 'е'  # эринии
        sg = [w, st + k, st + de, st + ('ю' if soft else 'у'),
              st + ('ей' if soft or st[-1] in HUSH else 'ой'), st + de]
        gp = st + ('й' if soft and st[-1] == 'и' else 'ь' if soft else '')  # эриний
        if not soft and len(st) > 2 and st[-1] == 'к' and st[-2] not in 'аеёиоуыэюя':
            gp = st[:-1] + ('е' if st[-2] in HUSH + 'ь' else 'о') + 'к'  # кошек, маток
            gp = gp.replace('ьек', 'ек')
        pl = [st + k, gp, st + ('ям' if soft else 'ам'), None,
              st + ('ями' if soft else 'ами'), st + ('ях' if soft else 'ах')]
        pl[3] = pl[1] if anim else pl[0]
        return (sg if num == 'sing' else pl)[ci]
    if low[-1] in 'ьй':
        st = w[:-1]
        sg = [w, st + 'я', st + 'ю', None, st + 'ем',
              st + ('и' if low.endswith('ий') else 'е')]
        pl = [st + 'и', st + ('ев' if low[-1] == 'й' else 'ей'), st + 'ям', None,
              st + 'ями', st + 'ях']
    else:
        h = low[-1] in HUSH
        sg = [w, w + 'а', w + 'у', None, w + ('ем' if h or low[-1] == 'ц' else 'ом'),
              w + 'е']
        k = 'и' if low[-1] in VELAR + HUSH else 'ы'
        pl = [w + k, w + ('ей' if h else 'ев' if low[-1] == 'ц' else 'ов'), w + 'ам',
              None, w + 'ами', w + 'ах']
    sg[3] = sg[1] if anim else sg[0]
    pl[3] = pl[1] if anim else pl[0]
    return (sg if num == 'sing' else pl)[ci]


def known_noun(w):
    for p in M.parse(w.lower()):
        if ('NOUN' in p.tag and 'nomn' in p.tag and 'sing' in p.tag and p.is_known
                and p.word == w.lower()):
            return p
    return None


def cap(src, w):
    return w[0].upper() + w[1:] if src[:1].isupper() else w


def noun_info(w):
    """(gender, animate) of a single noun"""
    if w.lower() in NOUNS:
        return NOUNS[w.lower()][0], NOUNS[w.lower()][1]
    p = known_noun(w)
    if p:
        return p.tag.gender or 'masc', 'anim' in p.tag or w in ANIM
    return ('femn' if w[-1] in 'ая' else 'masc'), True


def noun_form(w, num, ci, anim):
    lw = w.lower()
    if lw in NOUNS:
        return cap(w, NOUNS[lw][2 if num == 'sing' else 3].split()[ci])
    if w in INDECL or lw in INDECL:
        return w
    p = known_noun(w)
    if p:
        cs = CASES[ci]
        if ci == 3 and (num == 'plur' or p.tag.gender == 'masc'):
            cs = 'gent' if anim else 'nomn'
        q = p.inflect({cs, num})
        if q:
            return cap(w, q.word)
    return rule_noun(w, num, ci, anim)


def head_form(w, num, ci, g, anim):
    parts = w.split('-')
    if (any(x in INDECL or x.lower() in INDECL for x in parts)
            or (len(parts) > 1 and parts[-1][-1] in 'оеиуюэы')):
        return w
    # "гном-королева": parts of different gender -> only the last declines
    g0, g1 = str(noun_info(parts[0])[0]), str(noun_info(parts[-1])[0])
    # "гном-королева": a masculine attribute to a feminine noun stays put;
    # "крыса-оборотень", "пчела-убийца" decline both parts
    mixed = (len(parts) > 1 and not is_adj(parts[-1]) and g0 == 'masc'
             and g1 == 'femn' and parts[-1].lower() not in COMMON)
    return '-'.join(x if mixed and k < len(parts) - 1
                    else adj_form(x, GK.get(g, 'm'), num, ci, anim) if is_adj(x)
                    else noun_form(x, num, ci, anim) for k, x in enumerate(parts))


def phrase(name, num, ci):
    ws = name.split(' ')
    h = next((i for i, w in enumerate(ws) if not is_adj(w.split('-')[0])), None)
    if h is None:  # substantivized adjective: "Тёмный", "ловчий"
        return ' '.join(adj_form(w, 'm', num, ci, True) for w in ws)
    g, anim = noun_info(ws[h].split('-')[0])
    gk = GK.get(g, 'm')
    res = []
    for i, w in enumerate(ws):
        if i < h:
            res.append(adj_form(w, gk, num, ci, anim))
        elif i == h:
            res.append(head_form(w, num, ci, g, anim))
        elif w[0].isupper() and w not in KEEP_TAIL:
            res.append(adj_form(w, gk, num, ci, anim) if is_adj(w)
                       else head_form(w, num, ci, noun_info(w)[0], True))
        else:
            res.append(w)  # genitive tail: "детёныш красного дракона"
    return ' '.join(res)


def rd(path):
    return open(os.path.join(ROOT, path), 'rb').read().decode('cp1251')


def main():
    entries = re.split(r'\n\s*MON\(', rd('include/monsters.h'))[1:]
    names, seen = [], set()
    for e in entries:
        m = re.match(r'\s*NAMS?\(([^)]*)\)', e)
        if not m:
            continue
        uniq = 'G_UNIQ' in e[:1500]
        for n in re.findall(r'"([^"]+)"', m.group(1)):
            if n not in seen:
                seen.add(n)
                names.append((n, uniq))
    have = set(re.findall(r'\{ "([^"]+)",\r?\n\s+\{', rd('src/do_name.c')))
    out = ['/* moncase_ru.h: case forms of monster names, entries of',
           ' * mon_paradigms[] in do_name.c beyond the hand-written ones.',
           ' * Generated by tools/gen_moncase.py (pymorphy3); do not edit.  CP1251. */']
    n_out = 0
    for n, uniq in names:
        if n in have:
            continue
        n_out += 1
        s = WHOLE[n].split('|') if n in WHOLE else [phrase(n, 'sing', i) for i in range(6)]
        s[0] = n
        if uniq:
            p = ['NULL'] * 6
        else:
            p = ['"%s"' % phrase(n, 'plur', i) for i in range(6)]
            p[3] = 'NULL'
        if '--review' in sys.argv:
            print(' | '.join(s), '||', ' | '.join(x.strip('"') for x in p if x != 'NULL'))
        out.append('    { "%s",\n      { %s },\n      { %s } },' % (
            n, ', '.join('"%s"' % x for x in s), ', '.join(p)))
    open(os.path.join(ROOT, 'include/moncase_ru.h'), 'wb').write(
        ('\r\n'.join(x.replace('\n', '\r\n') for x in out) + '\r\n').encode('cp1251'))
    print(n_out, 'names', file=sys.stderr)


main()
