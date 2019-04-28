#/user/bin/env python3
#-*- coding:utf-8 -*-

# __author__ == Qilin

def encrpty(plaintext, key):
    cyphertext = ''
    for charater in plaintext:
        if charater.isalpha():
            number = ord(charater)
            number += key
            if charater.isupper():
                if number > ord('Z'):
                    number -= 26
                elif number < ord('A'):
                    number += 26
            elif charater.islower():
                if number > ord('z'):
                    number -= 26
                elif number < ord('a'):
                    number += 26
            charater = chr(number)
        cyphertext += charater

    return cyphertext

def de

