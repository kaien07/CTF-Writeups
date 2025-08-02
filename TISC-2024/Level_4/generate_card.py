import struct
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import hashlib

def generate_agpay_file(output_file):
    signature = b'AGPAY'
    version = b'01' # can be any number
    footerSignature = b'ENDAGP'

    encryptionKey = os.urandom(32)
    iv = os.urandom(16)

    cardNumber = b'1234567890123456'
    cardExpiryDate = struct.pack('>I', int(1735689600))
    balance = struct.pack('>Q', 313371337)
    
    decryptedData = cardNumber + b'\x00\x00\x00\x00' + cardExpiryDate + balance

    cipher = AES.new(encryptionKey, AES.MODE_CBC, iv)
    encryptedData = cipher.encrypt(pad(decryptedData, AES.block_size))
    
    checksum = hashlib.md5(iv + encryptedData).digest()

    content = (
        signature +
        version +
        encryptionKey +
        b'\x00' * 10 +  # reserved
        iv +
        encryptedData
 +
        footerSignature +
        checksum
    )

    with open(output_file, 'wb') as f:
        f.write(content)

    print(f"AGPAY file generated: {output_file}")

# Generate the AGPAY file
generate_agpay_file("valid_card.agpay")