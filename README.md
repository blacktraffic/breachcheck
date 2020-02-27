# breachcheck

Checks if your AD hashes are in the HIBP breach 

I've provided an sgrep binary, compiled on kali rolling. If that doesn't work for you, get and compile sgrep, aka 'sorted grep' here: https://sourceforge.net/projects/sgrep/files/latest/download 

Get and expand the HIBP data https://downloads.pwnedpasswords.com/passwords/pwned-passwords-ntlm-ordered-by-hash-v5.7z

ln -s pwned-passwords-ntlm-ordered-by-hash-v5 allbreach.txt 

Usage: 

$ echo guessme | python3 breach.py
Found 'guessme' in breach list

$ echo guessme | python3 convert-to-ntlm.py
3046cf4e584c9efd33b72e382c7dee6c

$ echo 3046cf4e584c9efd33b72e382c7dee6c | python3 breach-ntlm.py
Found '3046cf4e584c9efd33b72e382c7dee6c' in breach list

