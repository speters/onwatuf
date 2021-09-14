#!/usr/bin/env python3

# TUF firmware file extractor

import os
import argparse
from onwa_tuf import *

parser = argparse.ArgumentParser(description = 'TUF firmware file extractor')
parser.add_argument("-o", "--output-dir", help="output directory", default="tuf-extracted")
parser.add_argument("-w", "--write", help="actually write files (default: only list)", action="store_true")
parser.add_argument('tuffile', nargs=1, type=str, metavar='firmware_update_file.tuf')
args = parser.parse_args()

prefix = args.output_dir

tuf = OnwaTuf.from_file(args.tuffile[0])

for i, tufentry in enumerate(tuf.tuf_entries):
    if (tufentry.file_len + tufentry.file_len2) == 0:
        continue
    print(f" {tufentry.filename}")
    if (args.write):
        filename = prefix + '/' + tufentry.filename
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "wb") as f:
            f.write(tufentry.file_contents)
