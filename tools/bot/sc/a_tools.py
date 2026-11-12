import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())

wh = W('благословенный волшебный свисток')
lamp = W('масляная лампа')
whip = W('бычий бич')
towel = W('полотенце')
ball = W('хрустальный шар')
fig = W('статуэтка')
mark = W('волшебный маркер')
pie = W('кремовый пирог')
jelly = W('комок маточного молочка')
grease = W('банка смазки')
stone = W('пробный камень')
S('after wishes')

if wh:
    T('a' + wh, 'apply whistle')
if lamp:
    T('a' + lamp, 'light lamp'); T('a' + lamp, 'snuff lamp')
if whip:
    T('a' + whip, 'whip prompt'); T('.', 'whip self')
    T('a' + whip, 'whip prompt2'); T('>', 'whip down')
if towel:
    T('a' + towel, 'towel')
if ball:
    T('a' + ball, 'crystal ball'); esc()
if pie:
    T('a' + pie, 'pie face')
    if towel:
        T('a' + towel, 'towel after pie')
if grease:
    T('a' + grease, 'grease prompt'); T('a', 'grease weapon')
if stone:
    T('a' + stone, 'touchstone prompt'); T('a', 'rub spear')
if fig:
    T('a' + fig, 'figurine prompt'); T('l', 'figurine east')
if mark:
    T('E', 'engrave prompt'); T(mark, 'engrave with marker')
    S('engrave text?')
    K('Привет мир' + CR, quiet=0.8); S('engraved'); M()
    T(':', 'look here')
    T(';', 'farlook prompt'); T('.', 'farlook self spot')
T('\x18', 'attributes ^X', quiet=1.0); esc(3)
