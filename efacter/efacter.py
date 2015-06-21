#!/usr/bin/python

from Facter import Facter
import json, sys
from optparse import OptionParser
from datetime import datetime
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter
from pygments.styles import native


usage = "usage: %prog [options] <fact.element1.element2> [anotherFact.element1] [andAnother] ... "
optionparser = OptionParser(usage=usage)

optionparser.add_option("-j", "--json", dest="jsonOutput", default=False, action="store_true",
        help="Output JSON")
optionparser.add_option("-o", "--json-one-string", dest="oneString", default=4, action="store_const", const=None,
        help="Output JSON as one string (without indent)")
optionparser.add_option("-d", "--delimiter", dest="delimiter", default='.', action="store", metavar="DELIMITER",
        help="Delimiter for elements (default is '.'))")
optionparser.add_option("-n", "--no-colour", dest="noColour", default=False, action="store_true",
        help="Disable colours in the output")

(options, args) = optionparser.parse_args()
if len(args) < 1:
    optionparser.error("You need to provide at list one argument")
headerStyle = '\033[1m\033[92m'

facter = Facter(args)
facter.separator = options.delimiter

pieces = facter.pieces()
if options.jsonOutput:
    if options.noColour:
        print json.dumps(pieces, indent=options.oneString)
    else:
        print highlight(
                json.dumps(pieces, indent=options.oneString),
                JsonLexer(),
                TerminalFormatter()
                ).rstrip('\n')
else:
    for piece in args:
        if options.noColour:
            print "%s: %s" % (
                    piece,
                    json.dumps(pieces[piece], indent=4)
                    )
        else:
            print "%s: %s" % (
                    headerStyle + piece + '\033[0m',
                    highlight(
                        json.dumps(pieces[piece], indent=4),
                        JsonLexer(),
                        TerminalFormatter()
                        ).rstrip('\n')
                    )
sys.exit(0)
