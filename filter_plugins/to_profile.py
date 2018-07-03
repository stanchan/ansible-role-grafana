#!/usr/bin/env python

def to_profile(data, delimiter="="):
    rv = ""

    for key, val in sorted(data.iteritems()):
        if key is not None:
            rv += "export {!s}{!s}{!s}\n".format(key, delimiter, val)

    return rv

class FilterModule(object):
    def filters(self):
        return {
            'to_profile': to_profile
        }
