import xmltodict, json
import sys
import re

def read_xml(path):
    with open(path) as xml_file:
        data = xmltodict.parse(xml_file.read())
        return json.loads(json.dumps(data))

def testing(df, coverage):
    for suite in coverage['coverage']['packages']['package']:
        _class = suite['classes']['class']
        try:
            df[_class['@filename']]['coverage'] = float(_class['@line-rate']) * 100
        except:
            pass

def get_test_obj(path_time, path_coverage):
    time = read_xml(path_time)
    coverage = read_xml(path_coverage)

    df = {}
    for suite in time['testsuites']['testsuite']:

        name = suite['@name']
        tests = suite['@tests']
        time = suite['@time']
        try:
            success_density = (int(tests) - int(suite['@failures'])) / int(tests)
        except:
            success_density = 0
        if name == 'Root Suite':
            continue

        name = name.split('->')[0].replace(" ", "")

        if name not in df:

            df[name] = { 'test_execution_time': float(time), 'tests': int(tests), 'test_success_density': success_density }

        else:

            df[name]['test_execution_time'] += float(time)
            df[name]['tests'] += int(tests)

    testing(df, coverage)

    return df

if __name__ == '__main__':

    file = sys.argv[1]
    service = re.search(r'fga-eps-mds-2021_1-PUMA-([a-zA-Z]+)-(.*).json', file).group(1)

    path_time = f'../../../2021-1-PUMA-{service}/test-results.xml'
    path_coverage = f'../../../2021-1-PUMA-{service}/cobertura-coverage.xml'

    df = get_test_obj(path_time, path_coverage)

    j = {}
    file_path = f'../../analytics-raw-data/{file}'
    with open(file_path, 'r') as fp:
        j = json.loads(fp.read())
        fp.close()

    for component in j['components']:
        path = component['path']
        if path in df.keys():
            for key in df[path].keys():
                component['measures'].append({ 'metric': key, 'value': df[path][key] })
    with open(file_path, 'w') as fp:
        fp.write(json.dumps(j))
        fp.close()
