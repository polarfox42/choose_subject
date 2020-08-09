#! /usr/bin/python3.8
# -*- coding: utf8 -*-

import random
from subjects import SUBJECTS


def run():

    subject = random.choice(SUBJECTS)
    print(subject)


if __name__ == '__main__':
    run()
