import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
for w in ['жезл огня', 'жезл копания', 'жезл желаний', 'волшебная палочка огня', 'зелье лечения',
          'свиток зачарования доспеха', 'кольцо левитации', 'книга заклинаний силового удара',
          'свиток огня', 'огонь']:
    W(w)
for w in ['wand of fire', 'wand of digging', 'potion of healing', 'scroll of fire']:
    W(w)
K('\x09', quiet=1.0); S('identify')
for _ in range(5):
    if 'Дальше' in b.screen() or '(end)' in b.screen() or 'More' in b.screen(): K(CR, quiet=0.8)
K('i', 'inv', quiet=1.2); K(' ', 'inv2', quiet=1.0); esc()
