#!/usr/bin/env python3
# coding: utf-8
"""
main.py
10-31-2019
jack skrable
"""

import os
import yaml
import json
import requests


spec_path = os.path.abspath('~/api-specs/hello-world-proxy-spec.yaml').replace('~\\','')

with open(spec_path, 'r') as f:
    spec = yaml.safe_load(f)

tasks = list(spec['paths'].keys())

endpoint = ''.join(['https://',spec['host'],spec['basePath'],tasks[0]])



with requests.post(endpoint, auth=(un, pw)) as r:
    if r.status_code == 200:
        response = r.json()
    else:
        r.raise_for_status()


r.status_code
r.headers
r.text