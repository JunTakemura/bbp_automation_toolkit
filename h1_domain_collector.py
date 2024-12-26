#!/usr/bin/env python3

import os
import sys
import argparse
import requests

# Parse command line arguments
def parse_args():
    parser = argparse.ArgumentParser(
        prog="h1_domain_collector.py",
        description="Collects HackerOne in-scope domains")
    )
    parser.add_argument(
        "-u", "--api-username",
        required = True,
        help = "HackerOne API username (email address)"
    )

    parser.add_argument(
        "-t", "--api-token",
        required = True,
        help = "HackerOne API token"
    )

    parser.add_argument(
        "-b", "--bounty",
        default = True,
        choices = ["True", "False"],
        help = (
            "When set to 'True', only collect programmes that offers bounty"
            "When set to 'False', only collect programmes that does not offer bounty"
            "Default: "True""
        )
    )

    args = parser.parse_args()
    return args

# Retrieve program handles
def get_program_handles(api_username, api_token, bounty):
    handles = []
    page = 1
    while True:
        url = "https://api.hackerone.com/v1/hackers/programs"


