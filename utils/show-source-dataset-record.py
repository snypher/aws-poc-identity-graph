import pandas as pd
import argparse
from random import randint

# Defining input parameters
parser = argparse.ArgumentParser()
parser.add_argument('--dataset', required=True, 
    choices=[ 'first-party', 'cookie', 'clickstream', 'transactional' ], 
    help='Source dataset to show')
parser.add_argument('--csv-file', required=True, 
    help='Full path to input CSV file with first-party mock data')
    
# Parse input arguments
args = parser.parse_args()

try:
    if args.csv_file is None or args.dataset is None:
        raise Exception("A CSV file must be provided as input")
    
    if args.dataset is 'first-party':
        col_names = [ 'user_name', 'email', 'phone_number', 'external_id', 
            'street_address', 'postcode', 'city', 'country', 'birthday', 
            'loyalty_points', 'loyalty_level' ]
        cols = [ 0, 1, 2, 3 , 4, 5, 6, 7, 8, 9, 10 ]
    elif args.dataset is 'cookie':
        col_names = [ 'cookie_id', 'session_id', 'last_action', 'user_name', 
        'conversion_id', 'session_duration_sec' ]
        cols = [ 0, 1, 2, 3 , 4, 5 ]
    elif args.dataset is 'clickstream':
        col_names = [ 'session_id', 'client_ip', 'client_platform', 
        'canonical_url', 'domain_name', 'app_id', 'device_id', 'user_name', 
        'events', 'start_timestamp', 'start_event', 'end_timestamp', 
        'end_event', 'session_duration_sec', 'user-agent' ]
        cols = [ 0, 1, 2, 3 , 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ]
    else:    # Anything else is 'transactional'
        col_names = [ 'purchase_id', 'product_name', 'purchased_date', 
        'product_category', 'customer_id', 'reward_points' ]
        cols = [ 0, 1, 2, 3 , 4, 5 ]
    
    csv_file_path = args.csv_file
    lines = len(pd.read_csv(csv_file_path))
    skip=randint(1,lines)
    
    print('Randomly selecting the {} record # {}'.format(args.dataset,skip))
    print('')
    
    df = pd.read_csv(csv_file_path, names=col_names, usecols=cols, skiprows=skip, nrows=1)
except Exception as e:
    print(f"Unexpected exception : {str(e)}")
    raise e