import pandas as pd
import argparse
from random import randint

# Defining input parameters
parser = argparse.ArgumentParser()
parser.add_argument('--csv-file', required=True, 
    help='Full path to input CSV file with clickstream mock data')
    
# Parse input arguments
args = parser.parse_args()

col_names = [ 'session_id', 'client_ip', 'client_platform', 'canonical_url', 
    'domain_name', 'app_id', 'device_id', 'user_name', 'events', 
    'start_timestamp', 'start_event', 'end_timestamp', 'end_event', 
    'session_duration_sec', 'user-agent' ]
cols1 = [ 0, 2, 3, 5, 8, 9, 10, 11, 12, 13 ]
cols2 = [ 0, 1 ]
cols3 = [ 0, 4 ]
cols4 = [ 0, 6 ]
cols5 = [ 0, 7 ]

try:
    if args.csv_file is None:
        raise Exception("A CSV file must be provided as input")
    
    csv_file_path = args.csv_file
    lines = len(pd.read_csv(csv_file_path))
    skip=randint(1,lines)
    
    print('Randomly selecting the clickstream record # {}'.format(skip))
    print('')
    
    df1 = pd.read_csv(csv_file_path, names=col_names, usecols=cols1, skiprows=skip, nrows=1)
    print('Sample data for SessionID vertex')
    print('--------------------------------')
    print(df1.squeeze())
    print('')
    df2 = pd.read_csv(csv_file_path, names=col_names, usecols=cols2, skiprows=skip, nrows=1)
    print('Sample data for SessionID to ClientIP edge')
    print('------------------------------------------')
    print(df2)
    print('')
    df3 = pd.read_csv(csv_file_path, names=col_names, usecols=cols3, skiprows=skip, nrows=1)
    print('Sample data for SessionID to DomainName edge')
    print('--------------------------------------------')
    print(df3)
    print('')
    df4 = pd.read_csv(csv_file_path, names=col_names, usecols=cols4, skiprows=skip, nrows=1)
    print('Sample data for SessionID to DeviceID edge')
    print('------------------------------------------')
    print(df4)
    print('')
    df5 = pd.read_csv(csv_file_path, names=col_names, usecols=cols5, skiprows=skip, nrows=1)
    print('Sample data for SessionID to User edge')
    print('--------------------------------------')
    print(df5)
    print('')
except Exception as e:
    print(f"Unexpected exception : {str(e)}")
    raise e