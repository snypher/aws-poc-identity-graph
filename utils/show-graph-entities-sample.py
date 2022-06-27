import pandas as pd
import argparse
from random import randint

# Defining input parameters
parser = argparse.ArgumentParser()
parser.add_argument('--dataset', required=True, 
    choices=[ 'first-party', 'cookie', 'clickstream', 'transactional' ], 
    help='Source dataset to show')
parser.add_argument('--csv-file', required=True, 
    help='Full path to input CSV file with clickstream mock data')
    
# Parse input arguments
args = parser.parse_args()

# Read the CSV file for transactional dataset and display sample graph entities
def show_transactional_sample():
    
    col_names = [ 'purchase_id', 'product_name', 'purchased_date', 
                'product_category', 'customer_id', 'reward_points' ]
    cols1 = [ 1 ]
    cols2 = [ 3 ]
    cols3 = [ 4, 1, 0, 2, 5 ]
    cols4 = [ 1, 3 ]
    csv_file_path = args.csv_file
    lines = len(pd.read_csv(csv_file_path))
    skip=randint(1,lines)
        
    try:
        print('Randomly selecting the {} record # {}'.format(args.dataset,skip))
        print('')
        df1 = pd.read_csv(csv_file_path, names=col_names, usecols=cols1, skiprows=skip, nrows=1)
        print('Sample data for Product vertex')
        print('------------------------------')
        print('label: Product')
        print(df1.squeeze())
        print('')
        df2 = pd.read_csv(csv_file_path, names=col_names, usecols=cols2, skiprows=skip, nrows=1)
        print('Sample data for ProductCategory vertex')
        print('--------------------------------------')
        print('label: ProductCategory')
        print(df2.squeeze())
        print('')
        df3 = pd.read_csv(csv_file_path, names=col_names, usecols=cols3, skiprows=skip, nrows=1)
        print('Sample data for CustomerID to Product edge')
        print('------------------------------------------')
        print('label: hasPurchased')
        print(df3.squeeze())
        print('')
        df4 = pd.read_csv(csv_file_path, names=col_names, usecols=cols4, skiprows=skip, nrows=1)
        print('Sample data for Product to ProductCategory edge')
        print('-----------------------------------------------')
        print('label: inCategory')
        print(df4.squeeze())
        print('')
    except Exception as e:
        print(f"Unexpected exception : {str(e)}")
        raise e

# Read the CSV file for first-party dataset and display sample graph entities
def show_firstparty_sample():
    
    col_names = [ 'user_name', 'email', 'phone_number', 'external_id', 
            'street_address', 'postcode', 'city', 'country', 'birthday', 
            'loyalty_points', 'loyalty_level' ]
    cols1 = [ 0, 4, 8 ]
    cols2 = [ 1 ]
    cols3 = [ 2 ]
    cols4 = [ 3 ]
    cols5 = [ 5 ]
    cols6 = [ 6 ]
    cols7 = [ 7 ]
    cols8 = [ 10 ]
    cols9 = [ 0, 1 ]
    cols10 = [ 0, 5 ]
    cols11 = [ 0, 3 ]
    cols12 = [ 0, 2 ]
    cols13 = [ 0, 10, 9 ]
    cols14 = [ 0, 6 ]
    cols15 = [ 6 , 7 ]
    csv_file_path = args.csv_file
    lines = len(pd.read_csv(csv_file_path))
    skip=randint(1,lines)
        
    try:
        print('Randomly selecting the {} record # {}'.format(args.dataset,skip))
        print('')
        df1 = pd.read_csv(csv_file_path, names=col_names, usecols=cols1, skiprows=skip, nrows=1)
        print('Sample data for User vertex')
        print('---------------------------')
        print('label: User')
        print(df1.squeeze())
        print('')
        df2 = pd.read_csv(csv_file_path, names=col_names, usecols=cols2, skiprows=skip, nrows=1)
        print('Sample data for Email vertex')
        print('---------------------------')
        print('label: Email')
        print(df2.squeeze())
        print('')
        df3 = pd.read_csv(csv_file_path, names=col_names, usecols=cols3, skiprows=skip, nrows=1)
        print('Sample data for PhoneNumber vertex')
        print('----------------------------------')
        print('label: PhoneNumber')
        print(df3.squeeze())
        print('')
        df4 = pd.read_csv(csv_file_path, names=col_names, usecols=cols4, skiprows=skip, nrows=1)
        print('Sample data for CustomerID vertex')
        print('----------------------------------')
        print('label: CustomerID')
        print(df4.squeeze())
        print('')
        df5 = pd.read_csv(csv_file_path, names=col_names, usecols=cols5, skiprows=skip, nrows=1)
        print('Sample data for PostCode vertex')
        print('-------------------------------')
        print('label: PostCode')
        print(df5.squeeze())
        print('')
        df6 = pd.read_csv(csv_file_path, names=col_names, usecols=cols6, skiprows=skip, nrows=1)
        print('Sample data for City vertex')
        print('-------------------------------')
        print('label: City')
        print(df6.squeeze())
        print('')
        df7 = pd.read_csv(csv_file_path, names=col_names, usecols=cols7, skiprows=skip, nrows=1)
        print('Sample data for Country vertex')
        print('-------------------------------')
        print('label: Country')
        print(df7.squeeze())
        print('')
        df8 = pd.read_csv(csv_file_path, names=col_names, usecols=cols8, skiprows=skip, nrows=1)
        print('Sample data for LoyaltyLevel vertex')
        print('-------------------------------')
        print('label: LoyaltyLevel')
        print(df8.squeeze())
        print('')
        df9 = pd.read_csv(csv_file_path, names=col_names, usecols=cols9, skiprows=skip, nrows=1)
        print('Sample data for User to Email edge')
        print('----------------------------------')
        print('label: hasEmail')
        print(df9.squeeze())
        print('')
        df10 = pd.read_csv(csv_file_path, names=col_names, usecols=cols10, skiprows=skip, nrows=1)
        print('Sample data for User to PostCode edge')
        print('-------------------------------------')
        print('label: hasPostCodeAddress')
        print(df10.squeeze())
        print('')
        df11 = pd.read_csv(csv_file_path, names=col_names, usecols=cols11, skiprows=skip, nrows=1)
        print('Sample data for User to CustomerID edge')
        print('---------------------------------------')
        print('label: hasExternalId')
        print(df11.squeeze())
        print('')
        df12 = pd.read_csv(csv_file_path, names=col_names, usecols=cols12, skiprows=skip, nrows=1)
        print('Sample data for User to PhoneNumber edge')
        print('----------------------------------------')
        print('label: hasPhone')
        print(df12.squeeze())
        print('')
        df13 = pd.read_csv(csv_file_path, names=col_names, usecols=cols13, skiprows=skip, nrows=1)
        print('Sample data for User to LoyaltyLevel edge')
        print('-----------------------------------------')
        print('label: hasLoyaltyLevel')
        print(df13.squeeze())
        print('')
        df14 = pd.read_csv(csv_file_path, names=col_names, usecols=cols14, skiprows=skip, nrows=1)
        print('Sample data for User to City edge')
        print('---------------------------------')
        print(df14.squeeze())
        print('')
        df15 = pd.read_csv(csv_file_path, names=col_names, usecols=cols15, skiprows=skip, nrows=1)
        print('Sample data for City to Country edge')
        print('------------------------------------')
        print('label: inCountry')
        print(df15.squeeze())
        print('')
    except Exception as e:
        print(f"Unexpected exception : {str(e)}")
        raise e

# Read the CSV file for cooki dataset and display sample graph entities
def show_cookie_sample():
    
    col_names = [ 'cookie_id', 'session_id', 'last_action', 'user_name', 
        'conversion_id', 'session_duration_sec' ]
    cols1 = [ 0, 2, 4, 5 ]
    cols2 = [ 1, 0 ]
    csv_file_path = args.csv_file
    lines = len(pd.read_csv(csv_file_path))
    skip=randint(1,lines)
        
    try:
        print('Randomly selecting the {} record # {}'.format(args.dataset,skip))
        print('')
        df1 = pd.read_csv(csv_file_path, names=col_names, usecols=cols1, skiprows=skip, nrows=1)
        print('Sample data for Cookie vertex')
        print('-----------------------------')
        print('label: Cookie')
        print(df1.squeeze())
        print('')
        df2 = pd.read_csv(csv_file_path, names=col_names, usecols=cols2, skiprows=skip, nrows=1)
        print('Sample data for SessionID to Cookie edge')
        print('----------------------------------------')
        print('label: hasCookie')
        print(df2.squeeze())
        print('')
    except Exception as e:
        print(f"Unexpected exception : {str(e)}")
        raise e
        
# Read the CSV file for clickstream dataset and display sample graph entities
def show_clickstream_sample():
    
    col_names = [ 'session_id', 'client_ip', 'client_platform', 'canonical_url', 
        'domain_name', 'app_id', 'device_id', 'user_name', 'events', 
        'start_timestamp', 'start_event', 'end_timestamp', 'end_event', 
        'session_duration_sec', 'user-agent' ]
    cols1 = [ 0, 2, 3, 5, 8, 9, 10, 11, 12, 13, 14 ]
    cols2 = [ 1 ]
    cols3 = [ 4 ]
    cols4 = [ 6 ]
    cols5 = [ 14 ]
    cols6 = [ 0, 1 ]
    cols7 = [ 0, 4 ]
    cols8 = [ 0, 6 ]
    cols9 = [ 0, 7 ]
    cols10 = [ 0, 14 ]
    csv_file_path = args.csv_file
    lines = len(pd.read_csv(csv_file_path))
    skip=randint(1,lines)
        
    try:
        print('Randomly selecting the {} record # {}'.format(args.dataset,skip))
        print('')
        df1 = pd.read_csv(csv_file_path, names=col_names, usecols=cols1, skiprows=skip, nrows=1)
        print('Sample data for SessionID vertex')
        print('--------------------------------')
        print('label: SessionID')
        print(df1.squeeze())
        print('')
        df2 = pd.read_csv(csv_file_path, names=col_names, usecols=cols2, skiprows=skip, nrows=1)
        print('Sample data for ClientIP vertex')
        print('-------------------------------')
        print('label: ClientIP')
        print(df2.squeeze())
        print('')
        df3 = pd.read_csv(csv_file_path, names=col_names, usecols=cols3, skiprows=skip, nrows=1)
        print('Sample data for DomainName vertex')
        print('---------------------------------')
        print('label: DomainName')
        print(df3.squeeze())
        print('')
        df4 = pd.read_csv(csv_file_path, names=col_names, usecols=cols4, skiprows=skip, nrows=1)
        print('Sample data for DeviceID vertex')
        print('-------------------------------')
        print('label: DeviceID')
        print(df4.squeeze())
        print('')
        df5 = pd.read_csv(csv_file_path, names=col_names, usecols=cols5, skiprows=skip, nrows=1)
        print('Sample data for UserAgent vertex')
        print('--------------------------------')
        print('label: UserAgent')
        print(df5.squeeze())
        print('')
        df6 = pd.read_csv(csv_file_path, names=col_names, usecols=cols6, skiprows=skip, nrows=1)
        print('Sample data for SessionID to ClientIP edge')
        print('------------------------------------------')
        print('label: lastSeenAtIP')
        print(df6.squeeze())
        print('')
        df7 = pd.read_csv(csv_file_path, names=col_names, usecols=cols7, skiprows=skip, nrows=1)
        print('Sample data for SessionID to DomainName edge')
        print('--------------------------------------------')
        print('label: lastSeenAtDomain')
        print(df7.squeeze())
        print('')
        df8 = pd.read_csv(csv_file_path, names=col_names, usecols=cols8, skiprows=skip, nrows=1)
        print('Sample data for SessionID to DeviceID edge')
        print('------------------------------------------')
        print('label: usedDevice')
        print(df8.squeeze())
        print('')
        df9 = pd.read_csv(csv_file_path, names=col_names, usecols=cols9, skiprows=skip, nrows=1)
        print('Sample data for SessionID to User edge')
        print('--------------------------------------')
        print('label: loggedAs')
        print(df9.squeeze())
        print('')
        df10 = pd.read_csv(csv_file_path, names=col_names, usecols=cols10, skiprows=skip, nrows=1)
        print('Sample data for SessionID to UserAgent edge')
        print('-------------------------------------------')
        print('label: usedDevice')
        print(df10.squeeze())
        print('')
    except Exception as e:
        print(f"Unexpected exception : {str(e)}")
        raise e

# Main function
def main():
    try:
        if args.csv_file is None or args.dataset is None:
            raise Exception("A CSV file and a dataset must be provided as input")
            
        if args.dataset == 'first-party':
            show_firstparty_sample()
        elif args.dataset == 'cookie':
            show_cookie_sample()
        elif args.dataset == 'clickstream':
            show_clickstream_sample()
        elif args.dataset == 'transactional':
            show_transactional_sample()
        else:   # Anything else raise an error
            raise Exception("A valid dataset must be selected")
    except Exception as e:
        print(f"Unexpected exception : {str(e)}")
        raise e
    
if __name__ == '__main__':
    main()