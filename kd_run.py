import argparse
import logging
import sys
from kaggle_dropbox import KaggleDropbox, auth_first_time


def parse_command_line():
    parser = argparse.ArgumentParser(
            description='Exchange Python variables through Dropbox')
    parser.add_argument(
            '--setup', dest='do_setup',
            action='store_true', help='create auth file')
    parser.add_argument(
            '--basedir', type=str,
            help='parent directory on Dropbox')
    parser.add_argument('--get-file', type=str)
    parser.add_argument('--put-file', type=str)
    parser.add_argument(
            '--get-var', type=str,
            help='get file from dropbox and print as python variable')
    args = parser.parse_args()
    n_excl = bool(args.do_setup) + bool(args.get_file) + \
        bool(args.put_file) + bool(args.get_var)
    assert n_excl == 1, "One and only one of the arguments '--setup', " + \
           "'--get-file', '--put-file' and '--get-var' is expected, got:" + \
           str(args)
    return args


def main():
    args = parse_command_line()
    if args.do_setup:
        auth_first_time()
        sys.exit(0)
    logging.basicConfig()
    logging.getLogger('kaggle_dropbox').setLevel(logging.INFO)
    kd = KaggleDropbox(basedir=args.basedir)
    if args.get_file:
        content = kd.get_file_content(args.get_file)
        if content:
            sys.stdout.buffer.write(content)
        sys.exit(0)
    if args.put_file:
        with open(args.put_file, 'rb') as h:
            content = h.read()
        kd.put_file(args.put_file, content)
        sys.exit(0)
    if args.get_var:
        v = kd.getv(args.get_var)
        print(v)
        sys.exit(0)
    assert False


main()
