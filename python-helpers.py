# helpful python functions for openiboot script hackery

def GET_BITS(x, start, length):
     return ((x<<(32 - (start + length)))&0xffffffff) >> (32 - length)

