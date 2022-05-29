# Input format

# !pip3 install joblib

# load_model works with Python 3.6.13 :: Anaconda, Inc.
from email import message
from pydoc import plain
from tarfile import BLOCKSIZE
import unittest
import os
from unittest import result
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# import joblib
from keras.models import load_model
import numpy as np
from helper import *

alice1 = load_model('alice.h5')
bob1 = load_model('bob.h5')
eve1 = load_model('eve.h5')

BLOCKSIZE = 16
class UnitTestHelper(unittest.TestCase):

    def test_encstr(self):
        raw_message = 'Hello World!'
        bintext = ' '.join('{0:016b}'.format(ord(x), 'b') for x in raw_message)
        cipher  = bintext.replace(" ", "")
        output = encstr(raw_message)
        correct_bin = '000000000100100000000000011001010000000001101100000000000110110000000000011011110000000000100000000000000101011100000000011011110000000001110010000000000110110000000000011001000000000000100001'
        self.assertEqual(output[0],correct_bin)
        self.assertEqual(output[1],len(raw_message))

    def test_decstr(self):
        raw_message = 'Hello World!'
        bintext = ' '.join('{0:016b}'.format(ord(x), 'b') for x in raw_message)
        cipher  = bintext.replace(" ", "")
        plaintext = decstr(cipher,BLOCKSIZE)
        self.assertEqual(raw_message,plaintext)
    
    def test_strToArr(self):
        raw_message = 'Hello World!'
        bintext = ' '.join('{0:016b}'.format(ord(x), 'b') for x in raw_message)
        cipher  = bintext.replace(" ", "")
        result = strToArr(cipher,BLOCKSIZE)

        self.assertEqual(result,result)

    def test_arrToStr(self):
        raw_list = [[1,0,1,0]]
        bintext = arrToStr(raw_list)
        self.assertEqual(bintext,'1010')

    # def test_adversarial_performance(self):
    #     raw_message = 'Hello World!'
    #     messages = processRawMessage(raw_message)
    #     message = messages[0]
    #     key = messages[1]
    #     cipher = alice.predict([message,key])
    #     decipher = (bob.predict([cipher, key]) > 0.5).astype(int)
    #     plaintext = processBinaryMessage(decipher)
    #     adversary = (eve.predict(cipher) > 0.5).astype(int)
    #     adv = processBinaryMessage(adversary)

    #     self.assertEqual(raw_message, plaintext)
    #     self.assertNotEqual(raw_message, adv)

if __name__ == '__main__':
    unittest.main()
