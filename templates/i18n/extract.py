#!/usr/bin/env python

import sys
import re

_strings = {}

print '{'
for tmpl in sys.argv[1:]:
    with open(tmpl) as fd:
        strings = re.findall(r'_\(\'(.+?)\'\)', fd.read())
        print '  //', tmpl
        for s in strings:
            if s not in _strings:
                _strings[s] = 1
                print '  "%s": "",' % s

        print ''
print '}'

