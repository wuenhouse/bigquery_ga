import os, sys
from google.cloud import bigquery

def get_data(dataset_ref, table_id):
    table_ref = dataset_ref.table(table_id)
    table = client.get_table(table_ref)
    #print(table.num_rows)
    #print(table.full_table_id)
    #print(table.schema) 
    tb = table.full_table_id.replace(':','.')
    print tb
    QUERY = (
        'SELECT * '
        'FROM `{0}` ORDER BY event_timestamp DESC LIMIT 1'.format(tb))
    query_job = client.query(QUERY)  # API request
    rows = query_job.result()
    n = 0
    save = []
    if rows:
        for row in rows:
            n += 1
            print list(row.items())
            """
            dd = {}
            for x in row.event_params:
                if x['key'] in ['user_id', 'recording_id', 'place_id', 'timestamp']:
                    dd[x['key']] = x['value']['string_value']
            print dd
            """
            #os._exit(0)
        #print(row.event_name, row.event_date, row.event_timestamp, row.user_id, row.app_info)
    print n
client = bigquery.Client(project='magicmusic-1517832888216')
datasets = list(client.list_datasets())
project = client.project

if datasets:
    print("Datasets in project {}:".format(project))
    for dataset in datasets:  # API request(s)
        print("\t{}".format(dataset.dataset_id))
        dataset_id = dataset.dataset_id
        dataset_ref = client.dataset(dataset_id)
        dataset = client.get_dataset(dataset_ref)
        #print('Dataset ID: {0}'.format(dataset_id))
        #print('Labels:')
        for label, value in dataset.labels.items():
            print('\t{}: {}'.format(label, value))
        print('Tables:')
        tables = list(client.list_tables(dataset_ref))  # API request(s)
        if tables:
            for table in tables:
                print('\t{}'.format(table.table_id))
                if table.table_id == 'events_intraday_20190409':
                    get_data(dataset_ref, table.table_id)
                elif table.table_id == 'events_20190408':
                    get_data(dataset_ref, table.table_id)
            os._exit(0)
        else:
            print('\tThis dataset does not contain any tables.')
else:
    print("{} project does not contain any datasets.".format(project))
os._exit(0)