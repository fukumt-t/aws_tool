#!/usr/bin/env python
# -*- coding: utf-8 -*-

def emptystr_to_none(item):
    for k, v in item.items():
        if isinstance(v, dict):
            TrustedAdvisorCheck.json_parse(v)
        elif isinstance(v, list):
            for i in range(len(v)):
                list_elem = v[i]

                if isinstance(list_elem, str):
                    if list_elem == '':
                        v[i] = None
                elif isinstance(list_elem, list) or isinstance(list_elem, dict):
                    TrustedAdvisorCheck.json_parse(list_elem)
        elif isinstance(v, str):
            if v == '':
                item[k] = None

    return item
