#!/usr/bin/env python3

import re


def contains_domain(address, domain):
    domain_pattern = r'[\W\.-]+@' + domain + '$'
    if re.match(domain_pattern, address):
        return True
    return False


def replace_domain(address, old_domain, new_domain):
    old_domain_pattern = r'' + old_domain + '$'
    address = re.sub(old_domain_pattern, new_domain, address)
