import requests
import sys
import json
from datetime import date, datetime


today = datetime.now()

url = 'https://sonarcloud.io/api/measures/component_tree?component=fga-eps-mds_2021-1-PUMA&metricKeys=files,functions,complexity,coverage,ncloc,comment_lines_density,duplicated_lines_density,security_rating,tests,test_success_density,test_execution_time,reliability_rating&ps=500'

file_name = 'fga-eps-mds-2021_1-PUMA-'

def consumer(file_dest):
    res = requests.get(url)
    metrics = res.json()
    # print(metrics)
    f = open(f'./analytics-raw-data/{file_name}{today.strftime("%d-%m-%Y-%H")}_{file_dest}.json', 'w')
    f.write(json.dumps(metrics))
    f.close()

if __name__ == '__main__':
    file_version = sys.argv[1]
    consumer(file_version)
