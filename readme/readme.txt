plugin for CudaText.
helps to write headers with reStructuredText lexer.

1: place caret on a line which will be header (it must not start with
possible header-chars).
2: call one of N plugin commands in menu "Plugins / reStructuredText Helper",
it will underline current line with header-chars of proper level.

possible header chars by default: =-~" (4 levels).
but this can be changed in plugin config-file: plugins.ini, section [rest_helper].
open config file by menu item: "Options / Settings-plugins / ..."


author: Alexey Torgashin
license: MIT
