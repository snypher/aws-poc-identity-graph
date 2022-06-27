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
        raise Exception("A CSV file and a dataset must be provided as input")
    
    if args.dataset == 'first-party':
        col_names = [ 'user_name', 'email', 'phone_number', 'external_id', 
            'street_address', 'postcode', 'city', 'country', 'birthday', 
            'loyalty_points', 'loyalty_level' ]
    elif args.dataset == 'cookie':
        col_names = [ 'cookie_id', 'session_id', 'last_action', 'user_name', 
            'conversion_id', 'session_duration_sec' ]
    elif args.dataset == 'clickstream':
        col_names = [ 'session_id', 'client_ip', 'client_platform', 
            'canonical_url', 'domain_name', 'app_id', 'device_id', 'user_name', 
            'events', 'start_timestamp', 'start_event', 'end_timestamp', 
            'end_event', 'session_duration_sec', 'user-agent' ]
    elif args.dataset == 'transactional':
        col_names = [ 'purchase_id', 'product_name', 'purchased_date', 
            'product_category', 'customer_id', 'reward_points' ]
    else:   # Anything else raise and error
        raise Exception("A valid dataset must be selected")
    
    csv_file_path = args.csv_file
    lines = len(pd.read_csv(csv_file_path))
    skip=randint(1,lines)
    
    print('Randomly selecting the {} record # {}'.format(args.dataset,skip))
    print('')
    
    df = pd.read_csv(csv_file_path, names=col_names, skiprows=skip, nrows=1)
    print('Mock data for a single {} record'.format(args.dataset))
    print('----------------------------------------')
    print(df.squeeze())
    print('')
except Exception as e:
    print(f"Unexpected exception : {str(e)}")
    raise e