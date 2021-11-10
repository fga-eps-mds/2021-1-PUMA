import requests
import sys
import json
from datetime import date, datetime


today = datetime.now()

base_url = 'https://sonarcloud.io/api/measures/component_tree?component=fga-eps-mds_2021-1-PUMA-'
metrics = [
    'files',
    'functions',
    'complexity',
    'coverage',
    'ncloc',
    'comment_lines_density',
    'duplicated_lines_density',
    'security_rating',
    'tests',
    'test_success_density',
    'test_execution_time',
    'reliability_rating'
]

file_name = 'fga-eps-mds-2021_1-PUMA'

def consumer(file_dest):
    metrics_str = ",".join(metrics)
    print(metrics_str)
    res = requests.get(base_url+file_dest+'&metricKeys='+metrics_str+'&ps=500')
    m = res.json()
    # print(metrics)
    f = open(f'./analytics-raw-data/{file_name}-{file_dest}-{today.strftime("%m-%d-%Y-%H-%M")}.json', 'w')
    f.write(json.dumps(m))
    f.close()

if __name__ == '__main__':
    file_version = sys.argv[1]
    consumer(file_version)
