#!/usr/bin/env python

from typing import List


def find_pswd(pswd: str) -> bool:
    return pswd in load_system_pswd()


def load_system_pswd(filepath='change_pswd_func/file/pswds_on_system') -> List[str]:
    pswds = []
    with open(filepath, 'r') as fr:
        for line in fr.readlines():
            pswds.append(line.strip())
    return pswds
