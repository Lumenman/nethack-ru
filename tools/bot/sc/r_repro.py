import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
K('\x07'); K('hostile гном-королева' + CR); M()
for i in range(30):
    K('s'); M()
S('end')
