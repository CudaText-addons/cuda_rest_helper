import os
from cudatext import *
from cudax_lib import get_translation

_   = get_translation(__file__)  # I18N

fn_config = os.path.join(app_path(APP_DIR_SETTINGS), 'plugins.ini')

option_section = 'rest_helper'
option_headers = '=-~^"\''

def is_underline(s):
    for ch in option_headers:
        if s.startswith(ch):
            return True
    return False

def cjk_len(txt):
    lenTxt = len(txt)
    lenTxt_utf8 = len(txt.encode('utf-8'))
    rst_len = int((lenTxt_utf8 - lenTxt) / 2 + lenTxt) 
    return rst_len

class Command:

    def __init__(self):

        global option_headers
        option_headers = ini_read(fn_config, option_section, 'headers', option_headers)

    def config(self):

        ini_write(fn_config, option_section, 'headers', option_headers)
        file_open(fn_config)

    def header(self, level):

        carets = ed.get_carets()
        if len(carets)>1:
            return msg_status(_('Multi-carets not supported'))

        x, y, x1, y1 = carets[0]
        
        if y+1>=ed.get_line_count():
            ed.set_text_line(-1, '')
        
        line1 = ed.get_text_line(y)
        line2 = ed.get_text_line(y+1)
        
        if not line1.strip():
            return msg_status(_('Cannot make header with empty text'))
            
        if is_underline(line1):
            return msg_status(_('First put caret on header text'))

        if is_underline(line2):
            ed.delete(0, y+1, 0, y+2)
        
        level -= 1
        if level>=len(option_headers):
            return msg_status(_('Header level %d is not specified in config')%(level+1))

        newline = option_headers[level]*cjk_len(line1)
        ed.insert(0, y+1, newline+'\n')

    def under1(self):
        self.header(1)
    def under2(self):
        self.header(2)
    def under3(self):
        self.header(3)
    def under4(self):
        self.header(4)
    def under5(self):
        self.header(5)
    def under6(self):
        self.header(6)
