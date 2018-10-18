#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
from salesforce_reporting import Connection
import salesforce_reporting
import os

sf = Connection(username='andromaco@xappia.com',password='saasy2511', security_token="4fNUFqwEbGVP3NUiJo2Un33PY")

report = sf.get_report('00O1N0000091uFSUAY',details=True)
print(dir(sf.get_report))
parser = salesforce_reporting.ReportParser(report)

#print(parser._get_field_labels())
lines = parser.records()
#for i in items:
#    print (i

reportCsvFile = csv.writer(open(os.path.join(os.path.dirname(__file__), 'AndromacoContenido.csv'), 'a', encoding='UTF-8'))
reportCsvFile.writerows(lines)
