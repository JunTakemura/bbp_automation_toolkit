#!/usr/bin/env python3

import os
import sys
import argparse
import requests

def parse_args():
    parser = argparse.ArgumentParser(
        prog='h1_domain_collector.py',
        description='Collects HackerOne in-scope domains')
    )
    parser.add_argument(
        '=u', '--api-username',
        required = True,
        help = 'HackerOne API username (email address)'
    )

