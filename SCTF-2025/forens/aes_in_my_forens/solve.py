import pyzipper

zip_filename = 'aes_in_my_forens.zip'

sha1_hash_string = '9b9a2f352b707449bb52b660643df2a9a02752b4'

password_bytes = bytes.fromhex(sha1_hash_string)

with pyzipper.AESZipFile(zip_filename) as zf:
    zf.setpassword(password_bytes)
    print(zf.read('falg.txt'))
