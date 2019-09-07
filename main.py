#!/usr/bin/env python

import argparse

from change_pswd_func.change_pswd import change_pswd

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Intent test')
    parser.add_argument('old_pswd', help="Old password to be replaced with new one", type=str)
    parser.add_argument('new_pswd', help='New password', type=str)

    args = parser.parse_args()

    change_pswd(args.old_pswd, args.new_pswd)
