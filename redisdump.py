#!/usr/bin/env python


import redis
import argparse


def main(margs):
    r = redis.StrictRedis(margs.host, margs.port)
    for key in r.keys():
        print(key + " = " + r.get(key))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Redis Dump")
    parser.add_argument('-H', '--host', required=True)
    parser.add_argument('-p', '--port', default='6379')

    args = parser.parse_args()
    main(args)
