#!/bin/bash

wget https://downloads.pwnedpasswords.com/passwords/pwned-passwords-ntlm-ordered-by-hash-v5.7z
7z x pwned-passwords-ntlm-ordered-by-hash-v5.7z
ln -s pwned-passwords-ntlm-ordered-by-hash-v5.txt allbreach.txt
