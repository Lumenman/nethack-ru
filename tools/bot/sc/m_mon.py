import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
def answer_more(tag):
    for _ in range(8):
        s = b.screen(); top = s.split('\n')[0]; msgs.append(top)
        if 'Подробнее' in top or '[yn' in top:
            K('y', tag + ' info yes', quiet=1.5)
        elif 'Дальше' in s or 'More' in s:
            K(CR, quiet=0.6)
        else:
            break
# look at the pet with ; and with / (encyclopedia)
T(';', 'farlook'); K('m', quiet=0.4); K('.', quiet=1.0); S('look pet'); M()
K('/', quiet=0.6); K('/', quiet=0.6); M(); K('m', quiet=0.4); K('.', quiet=1.2); S('whatis pet')
answer_more('pet'); esc(3)
# create a monster with gender forms and look
ext('wizgenesis'); K('гном-лорд' + CR, quiet=1.0); M(); S('genesis')
T(';', 'farlook2'); K('m', quiet=0.3); K('m', quiet=0.3); K('.', quiet=1.0); S('look 2'); M()
K('/', quiet=0.6); K('?', quiet=0.8); K('гигантский муравей' + CR, quiet=1.2); S('typed mon')
answer_more('typed'); esc(3)
