# import os
import string
import sys
import argparse
# import subprocess
from rndstr import rndstr

def main():
    parser = argparse.ArgumentParser(description='rndstr')
    parser.add_argument('arg1')
    args = parser.parse_args()
    specifyNumber = int(sys.argv[1])
    print(rndstr.rndstr(specifyNumber))

if __name__ == "__main__":
    main()