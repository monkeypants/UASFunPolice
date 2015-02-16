#!/usr/bin/env python
from ontology import *

#for foo_bar in glob ./*.ucp:
#    var_name = "ucp_foo_bar"
#    obj_reference = "foo bar"
#    obj_heading = "Foo Bar"
#    obj_description = everything after the first blank line of `cat foo_bar.ucp`
#
#    eval("""%s = ucp('''%s''', '''%s''', '''%s''')""" % (
#        var_name, obj_reference, obj_heading, obj_description))


import glob
for fname in glob.iglob('*.ucp'):
    lhs = fname[:-4]
    words = lhs.split('_')
    varname = "ucp_%s" % lhs
    name_str = ' '.join(words)

    heading_str = ""
    for w in words:
        if w.upper() == w:  # preserve capitalised words
            word = w
        else:
            word = w.title()  # else title-case
        heading_str = "%s %s" % (heading_str, word)
    heading_str = heading_str[1:]  # chomp leading space

    body_lines=[]
    headers=[]
    with open('./%s'%fname, 'r') as f:
        blank_found = False
        for line in f:
            if not blank_found and line in ('',"\n"):
                blank_found = True
            else:
                if blank_found:
                    body_lines.append(line)
                else:
                    headers.append(line)

    body = '' #\n%s\n%s\n\n' % (heading_str, '-'*len(heading_str))
    for line in body_lines:
        body += line


    eval_str = '%s = ucp(\n    """%s""",\n    """%s""",\n    """%s""")' % (
        varname, name_str, heading_str, body)
    print eval_str
    print '#'*30
    print ''
