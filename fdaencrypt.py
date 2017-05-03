from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import DES3
from Crypto.Cipher import ARC4
import os
def secret_string(name, key):
    encoded_data = key.encrypt(name.encode('utf-8'), 32)

    return encoded_data

def encrypt_file(filename, symmetric_key):
    encryption = ARC4.new(symmetric_key)

    try:
        File = filename
        data_file = open(File, "r+")
    except FileNotFoundError:
        print("You must enter a valid file name")
        return False

    else:


        with open(filename,'rb') as in_file:

            with open(filename + '.enc', 'wb') as out_file:


                    data = in_file.read()

                    out_file.write((encryption.encrypt(data)))


            return True





        return False

def decrypt_file(filename, symmetric_key):

    if(".enc" in filename):

        with open(filename, 'rb') as in_file:

            decryptor = ARC4.new(symmetric_key)
            with open('DEC' + filename.strip('.enc'), 'wb') as dec_file:

                    data = in_file.read()


                    dec_file.write(decryptor.decrypt(data))

        return True
    else:
        print("File Not Found/Invalid File Name (must be .enc)")
        return False

if __name__ == '__main__':
    random_gen = Random.new().read
    private_key = RSA.generate(1024, random_gen)


    public_key = private_key.publickey()
    encoded_key = secret_string("Nader_is_awesome",public_key)


    print(private_key.decrypt(encoded_key))
