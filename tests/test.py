# Input format

# !pip3 install joblib

# load_model works with Python 3.6.13 :: Anaconda, Inc.
from email import message
from pydoc import plain
import unittest
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# import joblib
from keras.models import load_model
import numpy as np
from helper import *

alice1 = load_model('alice.h5')
bob1 = load_model('bob.h5')
eve1 = load_model('eve.h5')


class TestStringMethods(unittest.TestCase):

    def test_encryption(self):
        raw_message = 'Hello World!'
        messages = processRawMessage(raw_message)
        message = messages[0]
        key = messages[1]
        cipher = (alice.predict([message,key]) > 0.5).astype(int)
        ciphertext = processBinaryMessage(cipher)
        # print(ciphertext)
        self.assertNotEqual(raw_message,ciphertext)

    def test_decryption(self):
        raw_message = 'Hello World!'
        messages = processRawMessage(raw_message)
        message = messages[0]
        key = messages[1]
        cipher = alice.predict([message,key])
        decipher = (bob.predict([cipher, key]) > 0.5).astype(int)
        plaintext = processBinaryMessage(decipher)
        self.assertEqual(raw_message, plaintext)
    
    def test_adversarial_performance(self):
        raw_message = 'Hello World!'
        messages = processRawMessage(raw_message)
        message = messages[0]
        key = messages[1]
        cipher = alice.predict([message,key])
        decipher = (bob.predict([cipher, key]) > 0.5).astype(int)
        plaintext = processBinaryMessage(decipher)
        adversary = (eve.predict(cipher) > 0.5).astype(int)
        adv = processBinaryMessage(adversary)

        self.assertEqual(raw_message, plaintext)
        self.assertNotEqual(raw_message, adv)

if __name__ == '__main__':
    unittest.main()
