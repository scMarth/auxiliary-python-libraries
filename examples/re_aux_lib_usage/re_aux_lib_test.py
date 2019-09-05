import sys, os
sys.path.insert(0, os.path.dirname(__file__) + '/../../')

import re_aux_lib

print(re_aux_lib.remove_extra_spaces("    This is SoMe        string                ",True))
print("")

print(re_aux_lib.remove_extra_spaces("    This is SoMe        string                ",False))
print("")

print(re_aux_lib.string_contains_expr(".*uick","The quick brown fox jumps over the lazy dog."))
print("")

print(re_aux_lib.create_string_from_tokens(['This','is','an','array','of','tokens'],"|"))
print("")

print(re_aux_lib.create_string_from_tokens(['This','is','an','array','of','tokens']," "))
