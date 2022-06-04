import sys
import boto3
import os
from botocore.exceptions import ClientError
from faker import Faker
from faker.providers import DynamicProvider
from random import randint
import argparse
import csv
import datetime
import pandas as pd

# Defining input parameters
parser = argparse.ArgumentParser()
parser.add_argument('--records', default='100', 
    help='Amount of mock data records to generate')
parser.add_argument('--s3-bucket-name', default='poc-id-graph-733157031621', 
    help='Amazon S3 bucket to upload generated CSV files per dataset')
parser.add_argument('--debug', default=0, type=int, choices=[0,1], 
    help='Turn On/Off debugging (detailed output with muck data generated)')

# Parse input arguments
args = parser.parse_args()
# Global Faker generator
fake = Faker('en_US')
# Get current working directory
cwd = os.getcwd()

# Faker provider to define Loyalty levels
loyalty_provider = DynamicProvider(
    provider_name = "loyalty_level",
    elements = [
        "beginner", 
        "entusiast", 
        "active", 
        "leader"
        ]
    )

# Faker provider to randomize across unique user names
username_id_provider = DynamicProvider(
    provider_name = "username_id",
    elements = [ fake.unique.user_name() for l in range(int(args.records)) ]
    )

# Faker provider to randomize across unique emails
email_provider = DynamicProvider(
    provider_name = "email",
    elements = [ fake.unique.safe_email() for m in range(int(args.records)) ]
    )

# Faker provider to randomize across unique external IDs
external_id_provider = DynamicProvider(
    provider_name = "external_id",
    elements = [ fake.unique.ssn() for s in range(int(args.records)) ]
    )

# Global list with valid usernames from first-party dataset
known_usernames = []
# Global list with valid emails from first-party dataset
known_emails = []
# Global list with valid external IDs from first-party dataset
known_external_ids = []

# Create mock data for first-party source dataset (e.g. CRM database)
def create_first_party_dataset():
    filename = 'first_party_data_full.csv'
    fields = [ 'user_name', 'email', 'phone_number', 'external_id', 
        'street_address', 'postcode', 'city', 'country', 'birthday', 
        'loyalty_points', 'loyalty_level' ]
    # Adding custom providers
    fake.add_provider(loyalty_provider)
    fake.add_provider(username_id_provider)
    fake.add_provider(email_provider)
    fake.add_provider(external_id_provider)
    
    print('Creating first-party source dataset')
    
    try:
        # Create CSV file for first-party dataset
        with open(filename, 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(fields)
            if args.debug: print(fields)
        
            for i in range(int(args.records)):
                user_name = fake.unique.username_id()
                email = fake.unique.email()
                phone_number = fake.phone_number()
                external_id = fake.unique.external_id()
                street_address = fake.street_address()
                postcode = fake.postcode()
                city = fake.city()
                country = fake.country()
                birthday = fake.date_of_birth(None,12,115)
                loyalty_points = randint(100,10000)
                loyalty_level = fake.loyalty_level()
                row = [ user_name, email, external_id, phone_number, 
                    street_address, postcode, city, country, birthday, 
                    loyalty_points, loyalty_level 
                    ]
                writer.writerow(row)
                known_usernames.append(row[0])
                known_emails.append(row[1])
                known_external_ids.append(row[2])
                if args.debug: print(row)
            
        print('First-party dataset output file {0}/{1}'.format(
            cwd,filename))
    except Exception as e:
        print(f"Unexpected exception : {str(e)}")
        raise e
            
# Create mock data for transactional source dataset (e.g. purchase database)
def create_transactional_dataset():
    filename = 'transactional_data_full.csv'
    fields = [ 'product_id', 'product_name', 'purchased_date', 
        'product_category', 'customer_id', 'customer_email' ]
    brands = [ 'Samsung', 'LG', 'Sony', 'Motorola', 'BenQ', 'Apple' ]
    product = [ 'TV', 'Cell Phone', 'Tablet', 'Monitor', 
        'Computer', 'Headphones', 'Smartwatch', 'GPS' ]
    models = [ 'S10', 'X10', 'd95', 'SmartX', 'X4T', '456ty']
    categories = [ 'Electronics', 'Home Appliances', 'Health & Sports']
    
    print('Creating transactional source dataset')
    
    try:
        # Create CSV file for transactional dataset
        with open(filename, 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(fields)
            if args.debug: print(fields)
        
            for i in range(int(args.records)):
                product_id = fake.bothify('????-########').upper()
                product_name = '{0} {1} {2}'.format(
                    fake.word(ext_word_list=product),
                    fake.word(ext_word_list=brands),
                    fake.word(ext_word_list=models)
                    )
                purchased_date = fake.past_date(start_date='-10y')
                product_category = fake.word(ext_word_list=categories)
                customer_id = ''
                customer_email = ''
                if fake.pybool():
                    customer_id = ( fake.external_id() if fake.pybool()
                        else fake.ssn() )
                else:
                    customer_email = ( fake.email() if fake.pybool()
                        else fake.safe_email() )
                row = [ product_id, product_name, purchased_date, 
                    product_category, customer_id, customer_email ]
                writer.writerow(row)
                if args.debug: print(row)
                
        print('Transactional dataset output file: {0}/{1}'.format(
            cwd,filename))
    except Exception as e:
        print(f"Unexpected exception : {str(e)}")
        raise e

# Generate mock data for clickstream source dataset
def generate_clickstream_record(session_id, timestamp, platform):
    event_types = [ 'Purchase', 'Search', 'ProductView', 'Whishlist', 
        'PageView', 'DiscardCard', 'CompareProducts', 'SingIn', 'SingUp' ]
    apps = [ 'ecommerce', 'travel', 'health_providers', 'health_services' ]
    row = []
    try:
        session_id = ( session_id if session_id 
            else fake.unique.uuid4() )
        end_timestamp = ( timestamp if timestamp 
            else fake.past_datetime(start_date='-10y') )
        session_duration_sec = randint(30,1800)
        start_timestamp = ( 
            end_timestamp - datetime.timedelta(seconds=session_duration_sec)
            )
        client_ip = fake.ipv4_public()
        client_platform = platform
        canonical_url = fake.url()
        domain_name = fake.domain_name()
        app_id = fake.word(ext_word_list=apps)
        device_id = ( 
            fake.hexify('^^^^^^^^^^^^^^^^',True) if platform == 'mobile' 
            else '' )
        events = randint(2,30)
        start_event = fake.word(ext_word_list=event_types)
        end_event = fake.word(ext_word_list=event_types)
        user_agent = fake.user_agent()
        row = [ session_id, client_ip, client_platform, canonical_url, 
            domain_name, app_id, device_id, events, start_timestamp, 
            start_event, end_timestamp, end_event, session_duration_sec, 
            user_agent ]
        if args.debug: print(row)
    except Exception as e:
        print(f"Unexpected exception : {str(e)}")
        raise e
    return row
            
# Generate mock data for cookie source dataset
def generate_cookie_record():
    row = []
    try:
        if fake.pybool():   # If user accept cookie and tracking
            cookie_id = fake.unique.uuid4()
            session_id = fake.unique.uuid4()
            last_action = fake.past_datetime(start_date='-10y')
            user_name = ( fake.username_id() if fake.pybool() 
                else '' )   # True/False: authenticated/anonymous
            conversion_id = ( 
                fake.pystr_format('x{{random_int}},x{{random_int}}', None) 
                if fake.pybool() else '' )
            row = [ cookie_id, session_id, last_action, 
                user_name, conversion_id ]
            if args.debug: print(row)
    except Exception as e:
        print(f"Unexpected exception : {str(e)}")
        raise e
    return row

# Create source dataset for cookies and clickstream
def create_cookie_clickstream_datasets():
    cookies_filename = 'cookie_data_full.csv'
    clickstream_filename = 'clickstream_data_full.csv'
    cookie_fields = [ 'cookie_id', 'session_id', 'last_action', 'user_name', 
        'conversion_id' ]
    clickstream_fields = [ 'session_id', 'client_ip', 'client_platform', 
        'canonical_url', 'domain_name', 'app_id', 'device_id', 'events', 
        'start_timestamp', 'start_event', 'end_timestamp', 'end_event', 
        'session_duration_sec', 'user-agent' ]
    cookie_row = []
    clickstream_row = []
    
    print('Creating cookie and clickstream source datasets')
    
    try:
        # Create DataFrame for cookie dataset
        cookies_df = pd.DataFrame(columns=cookie_fields)
        # Create DataFrame for clickstream dataset
        clickstream_df = pd.DataFrame(columns=clickstream_fields)
        
        for i in range(int(args.records)):
            if fake.pybool():   # True: is a web client
                cookie_row = generate_cookie_record()
                if cookie_row:
                    clickstream_row = generate_clickstream_record(
                        session_id=cookie_row[1], 
                        timestamp=cookie_row[2],
                        platform='web'
                        )
                    cookies_df.loc[i] = cookie_row
                    clickstream_df.loc[i] = clickstream_row
                    if args.debug: print(cookie_row)
                    clickstream_df.loc[i] = clickstream_row
                    if args.debug: print(clickstream_row)
            else:               # Anything else: is a mobile client
                clickstream_row = generate_clickstream_record(
                    session_id=None,
                    timestamp=None,
                    platform='mobile'
                    )
                clickstream_df.loc[i] = clickstream_row
                if args.debug: print(clickstream_row)
        
        # Create CSV file for cookie dataset
        cookies_df.to_csv(cookies_filename, index=False)
        # Create CSV file for clickstream dataset
        clickstream_df.to_csv(clickstream_filename, index=False)
        
        print('Clickstream dataset output file: {0}/{1}'.format(
                cwd,clickstream_filename))
        print('Cookie dataset output file: {0}/{1}'.format(
                cwd,cookies_filename))
    except Exception as e:
        print(f"Unexpected exception : {str(e)}")
        raise e
        
# Main function
def main():
    try:
        if args.debug: print('Current working directory: {0}'.format(cwd))
        create_first_party_dataset()
        print('\n')
        create_transactional_dataset()
        print('\n')
        create_cookie_clickstream_datasets()
        fake.unique.clear()
    except Exception as e:
        print(f"Unexpected exception : {str(e)}")
        raise e

if __name__ == '__main__':
    main()