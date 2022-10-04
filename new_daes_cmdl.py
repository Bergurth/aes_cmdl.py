# this uses python3 and pyAesCrypt
import pyAesCrypt
import sys

password = sys.argv[1]

pyAesCrypt.decryptFile(sys.argv[2], "dataout.txt", password)
# decrypt