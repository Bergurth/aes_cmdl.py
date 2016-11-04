# aes_cmdl.py
commandline AES encryption. adapted from code from Eli Bendersky.

original code found here:
http://eli.thegreenplace.net/2010/06/25/aes-encryption-of-files-in-python-with-pycrypto

USAGE:
</br>
case 1 encrypting
</br>
usage: python aes_cmdl.py input_file_name \<output_file_name> -p \<password>
</br>
case 2 decrypting
</br>
usage: python daes_cmdl.py input_file_name \<output_file_name> -p \<password>
</br>
in both cases if an output file is not specified, the program will write to standard out "stdout",
and is thus conveniently piped, e.g. into another program, or appended to an existing file ..
