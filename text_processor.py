#!/usr/bin/env python3
import sys
with open(sys.argv[1]) as f:
    print(f.read().replace(sys.argv[2], sys.argv[3]))
