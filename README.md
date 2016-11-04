# aes_cmdl.py
commandline AES encryption. adapted from code from Eli Bendersky.

original code found here:
http://eli.thegreenplace.net/2010/06/25/aes-encryption-of-files-in-python-with-pycrypto

USAGE:
case 1 encrypting
usage: python aes_cmdl.py input_file_name <output_file_name> -p <password>

case 2 decrypting
usage: python daes_cmdl.py input_file_name <output_file_name> -p <password>

in both cases if an output file is not specified, the program will write to standard out "stdout",
and is thus conveniently piped, e.g. into anothoer program, or appended to an existing file ..
