#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
from salesforce_reporting import Connection
import salesforce_reporting
import os
import pandas as pd

sf = Connection(username='andromaco@xappia.com',password='saasy2511', security_token="4fNUFqwEbGVP3NUiJo2Un33PY")

report = sf.get_report('00O1N0000091uFSUAY',details=True)

parser = salesforce_reporting.ReportParser(report)
lines = parser.records()

###############################
# Headers creation

headers = parser._get_field_labels()
headersList = []
conditionalList = 0
while conditionalList < len(headers):
	headersList.append(headers[conditionalList])
	conditionalList += 1

###############################
# Getting Header index of 'Categoría'

#print('The index is: ' + str(headersList.index('Cat contenido')))

###############################
# Modify 'Cat nameCategory' from 'Verdadero' to 'Category Name' - Ejem: 'Verdadero' - 'Contenido'
# This modify details not the headers of the report
for line in lines:
	line[4] = 'Contenido'

###############################

reportCsvFile = csv.writer(open(os.path.join(os.path.dirname(__file__), 'AndromacoContenido.csv'), 'w', encoding='UTF-8'))
reportCsvFile.writerow(headersList)

reportCsvFile = csv.writer(open(os.path.join(os.path.dirname(__file__), 'AndromacoContenido.csv'), 'a', encoding='UTF-8'))
reportCsvFile.writerows(lines)

