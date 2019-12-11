#!/usr/bin/env python3
#
# Convert RDS parameter group intom a TF parameter group.
#
# Usage:
#   aws rds describe-db-parameters --db-parameter-group-name customers-logs-primary | python3 convert.py
#

import json
import sys

__version__ = 1.0
__author__ = 'Lev Kokotov <lev.kokotov@instacart.com>'

body = json.loads(sys.stdin.read())

if 'Parameters' not in body:
    print('Input is not valid AWS CLI response. JSON object. with "Parameters" key required.')
    exit(1)

parameters = body['Parameters']

print('resource "aws_db_parameter_group" "parameter_group_name" {')

for parameter in parameters:
    if not parameter['IsModifiable']:
        continue
    if 'ParameterValue' not in parameter:
        continue
    print('  parameter {')
    print('    apply_method = "immediate"')
    print('    name         = "{}"'.format(parameter['ParameterName']))
    print('    value        = "{}" # {}'.format(parameter['ParameterValue'], parameter['Description']))
    print('  }')

print('}')