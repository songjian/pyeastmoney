from .eastmoney import hg
import argparse

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('cmd', help='命令 hg', nargs='?', default='hg')
    parser.add_argument('--sty', help='sty', nargs='?', default='HKZB')
    parser.add_argument('--mkt', help='mkt code', nargs='?', default='0')
    parser.add_argument('--stat', help='stat code', nargs='?', default='0')
    args=parser.parse_args()
    if args.cmd == 'hg':
        hg(sty=args.sty, mkt=args.mkt, stat=args.stat)