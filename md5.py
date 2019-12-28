#!/usr/bin/env python

import hashlib

end_chars = str(input("Captcha Code:"))

i = 0
while (True):
    plaintext = str(i)
    m = hashlib.md5()
    m.update(plaintext)
    h = m.hexdigest()
    # print plaintext, h;
    if h.endswith(end_chars):
        print "Hash:",h
        print "Number:",plaintext
        break

    i = i+1