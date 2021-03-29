#!/usr/bin/python39
# -*- coding: utf-8 -*-

from hashlib import sha256


def updatehash(*args):
    hashing_text = ""; h = sha256()
    for arg in args:
        hashing_text += str(arg)

    h.update(hashing_text.encode('utf-8'))
    return h.hexdigest()


class Block:
    data = None
    hash = None
    nonce = 0
    previous_hash = "0" * 64

    def __init__(self, data, number=0):
        self.data = data
        self.number = number

    def hash(self):
        return updatehash(
            self.previous_hash,
            self.number,
            self.data,
            self.nonce
        )

    def __str__(self):
        return str("Block#: {}\nHash: {}\nPrevious:{}\nData: {}\nNonce: {}\n".format(self.number, self.hash(), self.previous_hash, self.data, self.nonce))


class Blockchain:
    difficulty = 5

    def __init__(self, chain=[]):
        self.chain = chain

    def add(self, block):
        self.chain.append(block)

    def remove(self, block):
        self.chain.remove(block)

    def mine(self, block):
        try:
            block.previous_hash = self.chain[-1].hash()
        except IndexError:
            pass

        while True:
            if block.hash()[:self.difficulty] == "0" * self.difficulty:
                self.add(block); break
            else:
                block.nonce += 1

    def isValid(self):
        for i in range(1, len(self.chain)):
            previous = self.chain[i].previous_hash
            current = self.chain[i-1].hash()
            if previous != current or current[:self.difficulty] != "0" * self.difficulty:
                return False
        return True


def main():
    blockchain = Blockchain()
    db = ["block1test", "block2test", "block3test"]

    num = 0
    for data in db:
        num += 1
        blockchain.mine(Block(data, num))

    for block in blockchain.chain:
        print(block)

    blockchain.chain[1].data = "NEW DATA"
    print(blockchain.isValid())


if __name__ == '__main__':
    main()
