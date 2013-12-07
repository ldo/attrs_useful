#+
# This module defines routine to ease getting/setting lots of attributes
# on an object at once.
#
# Written by Lawrence D'Oliveiro <ldo@geek-central.gen.nz>.
#-

def getattrs(obj, attrnames) :
    "returns a dictionary of the current values of the specified attributes of\n" \
    "the specified object. attrnames must be a list or tuple of attribute name strings."
    result = {}
    for attr in attrnames :
        result[attr] = getattr(obj, attr)
    #end for
    return \
        result
#end getattrs

def setattrs(obj, *args, **kwargs) :
    "does bulk setting of attributes on obj. Call this in any of the following ways:\n" \
    "\n" \
    "    setattrs(obj, ((key, val), (key, val) ...))\n" \
    "    setattrs(obj, {key : val, key : val ...})\n" \
    "    setattrs(obj, key = val, key = val ...)\n" \
    "\n" \
    "in each case, “key” is the name of an attribute of the object, and “val” is the\n" \
    "new value to assign to it. In the first two cases, the key must be a string; in the\n" \
    "last case, it is an unquoted word as per usual Python keyword-argument syntax.\n"
    if (len(args) != 0) == (len(kwargs) != 0) :
        raise TypeError("specify attrs via either sequence/dict or keyword args, not both")
    #end if
    if len(args) != 0 :
        assert len(args) == 1, "only one additional non-keyword arg allowed"
        attrset = args[0]
        if type(attrset) in (list, tuple) :
            for arg in attrset :
                key, val = arg
                setattr(obj, key, val)
            #end for
        elif type(attrset) == dict :
            for key in attrset :
                setattr(obj, key, attrset[key])
            #end for
        else :
            raise TypeError("type of arg must be list, tuple or dict")
        #end if
    elif len(kwargs) != 0 :
        for attr in kwargs :
            setattr(obj, attr, kwargs[attr])
        #end for
    #end if
#end setattrs

def delattrs(obj, attrnames, ignore_error = False) :
    "deletes the specified attributes from the specified object. attrnames must be\n" \
    "a tuple or list of string attribute names. ignore_error can be set to True\n" \
    "to quietly ignore deletion failures."
    for attr in attrnames :
        try :
            delattr(obj, attr)
        except AttributeError as fail :
            if not ignore_error :
                raise
            #end if
        #end try
    #end for
#end delattrs
