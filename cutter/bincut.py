import argparse
import os
import shutil
import sys


def genSpoint(bytes_list):
    separate_point = []
    try:
        for addr in bytes_list.split(','):
            separate_point.append(int(addr, 16))
    except ValueError:
        sys.exit(__file__ + ': error: invalid bytes arguments')
    separate_point.sort()
    return separate_point


def cut(target, separate_point):
    cnt = 0
    sub_bytes = 0
    shutil.copy(target, 'tmp')
    for sp in separate_point:
        end = sp - sub_bytes
        with open('tmp', 'rb') as fout:
            stream = fout.read()
            with open(str(cnt), 'wb') as fout2:
                fout2.write(stream[:end])
            with open('tmp', 'wb') as fout2:
                fout2.write(stream[end:])
        cnt = cnt + 1
        sub_bytes = sp
    os.rename('tmp', str(cnt))


def main():
    header = 'Binary Cutter v0.0.1 by GONDA, Akihiko'
    bytes_help = 'split the target by bytes list'
    target_help = 'a target binary file'
    parser = argparse.ArgumentParser(description=header)
    parser.add_argument('-b', '--bytes', help=bytes_help)
    parser.add_argument('target', metavar='TARGET', type=str, help=target_help)

    args = parser.parse_args()
    separate_point = genSpoint(args.bytes)
    target = args.target

    cut(target, separate_point)

    
if __name__ == '__main__':
    main()
