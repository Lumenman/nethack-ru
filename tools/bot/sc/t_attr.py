import os
exec(open(os.path.join(os.path.dirname(__file__), 'common.py'), encoding='utf-8').read())
K('\x18', 'attr1')
for i in range(6):
    K(' ', 'attr%d' % (i + 2))
K('\x1b')
