#!/usr/bin/env python

def escape(data, quote='"'):
    if quote is not None and len(quote):
        return str(data).replace('\\', '\\\\').replace(quote, "\\{:s}".format(quote))
    else:
        return data

def to_ini(data, comment="#", delimiter="=", indent="", quote="",section_is_comment=False, ucase_prop=False):
    rv = ""

    for prop, val in sorted(data.iteritems()):
        if ucase_prop:
            prop = prop.upper()

        vals = []

        if isinstance(val, list):
            vals = val
        elif not isinstance(val, dict):
            vals = [val]

        for item in vals:
            if (len(quote) == 0 and isinstance(item, basestring) and len(item) == 0):
                item = '""'

            if item is not None:
                rv += "{:s}{:s}{:s}{:s}{:s}{:s}\n".format(indent, prop, delimiter, quote, escape(item, quote), quote)

    for section, props in sorted(data.iteritems()):
        if isinstance(props, dict):
            if rv != "":
                rv += "\n"

            if section_is_comment:
                rv += "{:s} {:s}\n".format(comment, section)
            else:
                rv += "[{:s}]\n".format(section)

            rv += to_ini(
                props,
                delimiter=delimiter,
                indent=indent,
                quote=quote,
                section_is_comment=section_is_comment,
                ucase_prop=ucase_prop)

    return rv

class FilterModule(object):
    def filters(self):
        return {
            'to_ini': to_ini
        }
