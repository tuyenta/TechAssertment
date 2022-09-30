#!/usr/bin/env python3
import argparse
import json
import sys
from typing import TextIO

from ingester.main import ingest


def main(infile: TextIO) -> int:
    data = json.load(infile)
    infile.close()

    ingest(data)

    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="insert data into db")
    parser.add_argument(
        "infile", nargs="?", type=argparse.FileType("r"), default=sys.stdin
    )
    args = parser.parse_args()

    sys.exit(main(args.infile))
