# this uses python3 and pyAesCrypt
import pyAesCrypt
import sys

password = sys.argv[1]
# encrypt
pyAesCrypt.encryptFile(sys.argv[2], "data.txt.aes", password)
# decrypt