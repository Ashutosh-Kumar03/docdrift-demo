import argparse

p = argparse.ArgumentParser(prog="demo")
p.add_argument("--verbose", action="store_true", help="print more logs")
p.add_argument("--timeout", default=30, help="seconds to wait before giving up")
args = p.parse_args()
