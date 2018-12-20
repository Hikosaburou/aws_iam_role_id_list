#!/usr/bin/env python

import boto3
import datetime
from tabulate import tabulate

def main():
    
    ### IAM Role 一覧取得
    iam = boto3.client('iam')
    response = iam.list_roles()

    header = ['RoleName', 'RoleId']
    table = [[elm['RoleId'], elm['RoleName']] for elm in response['Roles']]
    sorted_table = sorted(table, key=lambda tbl: tbl[1])

    print(tabulate(sorted_table, header, tablefmt='pipe'))

if __name__ == '__main__': main()
