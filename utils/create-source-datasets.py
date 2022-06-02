import sys
import boto3
import os
from botocore.exceptions import ClientError
from faker import Faker
from faker.providers import DynamicProvider
from random import randint
import argparse
import csv

# Defining input parameters
parser = argparse.ArgumentParser()
parser.add_argument('--records', default='100', 
    help='Amount of mock data records to generate')
parser.add_argument('--s3-bucket-name', default='poc-id-graph-733157031621', 
    help='Amazon S3 bucket to upload generated CSV files per dataset')
parser.add_argument('--debug', default=False, 
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
def create_first_party_dataset(records):
    filename = 'first_party_data_full.csv'
    fields = [ 'user_name', 'email', 'phone_number', 'external_id', 
        'street_address', 'postcode', 'city', 'country', 'birthday', 
        'loyalty_points', 'loyalty_level' ]
    # Adding custom providers
    fake.add_provider(loyalty_provider)
    fake.add_provider(username_id_provider)
    fake.add_provider(email_provider)
    fake.add_provider(external_id_provider)
    
    print('Creating mock data for first-party source dataset')
    
    # Create CSV file for first-party dataset
    with open(filename, 'w') as csv_file:
        try:
            writer = csv.writer(csv_file)
            writer.writerow(fields)
            if args.debug: print(fields)
        
            for i in range(records):
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
    
# Create mock data for device-and-cookie source dataset
def create_device_cookie_dataset(records):
    filename = 'device_cookie_data_full.csv'
    fields = [ 'cookie_id', 'session_id', 'user_name', 'device_id', 
        'conversion_id', 'clickstream_log' ]
    
    print('Creating mock data for device-and-cookie source dataset')
    
    # Create CSV file for device-and-cookie dataset
    with open(filename, 'w') as csv_file:
        try:
            writer = csv.writer(csv_file)
            writer.writerow(fields)
            if args.debug: print(fields)
            
            for i in range(records):
                cookie_id = fake.unique.uuid4()
                session_id = fake.unique.uuid4()
                last_action = fake.past_datetime(start_date='-10y')
                user_name = ( 
                    fake.username_id() if fake.pybool() 
                    else '' )
                device_id = ( 
                    fake.hexify('^^^^^^^^^^^^^^^^',True) if fake.pybool() 
                    else '' )
                conversion_id = ( 
                    fake.pystr_format('x{{random_int}},x{{random_int}}',None) 
                    if fake.pybool() else '' )
                clickstream_log = ''
                row = [ cookie_id, session_id, last_action, user_name, 
                    device_id, conversion_id, clickstream_log ]
                writer.writerow(row)
                if args.debug: print(row)
                
            print('Device-and-Cookie dataset output file: {0}/{1}'.format(
                cwd,filename))
        except Exception as e:
            print(f"Unexpected exception : {str(e)}")
            raise e
            
# Create mock data for transactional source dataset (e.g. purchase database)
def create_transactional_dataset(records):
    filename = 'transactional_data_full.csv'
    fields = [ 'product_id', 'product_name', 'purchased_date', 
        'product_category', 'customer_id', 'customer_email' ]
    brands = [ 'Samsung', 'LG', 'Sony', 'Motorola', 'BenQ', 'Apple' ]
    product = [ 'TV', 'Cell Phone', 'Tablet', 'Monitor', 
        'Computer', 'Headphones', 'Smartwatch', 'GPS' ]
    models = [ 'S10', 'X10', 'd95', 'SmartX', 'X4T', '456ty']
    categories = [ 'Electronics', 'Home Appliances', 'Health & Sports']
    
    print('Creating mock data for transactional source dataset')
    
    # Create CSV file for device-and-cookie datasetgit status
    with open(filename, 'w') as csv_file:
        try:
            writer = csv.writer(csv_file)
            writer.writerow(fields)
            if args.debug: print(fields)
        
            for i in range(records):
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
                        else fake.ssn() 
                        )
                else:
                    customer_email = ( fake.email() if fake.pybool()
                        else fake.safe_email()
                        )
                row = [ product_id, product_name, purchased_date, 
                    product_category, customer_id, customer_email ]
                writer.writerow(row)
                if args.debug: print(row)
                
            print('Transactional dataset output file: {0}/{1}'.format(
                cwd,filename))
        except Exception as e:
            print(f"Unexpected exception : {str(e)}")
            raise e
            
# Main function
def main():
    try:
        if args.debug: print('Current working directory: {0}'.format(cwd))
        create_first_party_dataset(int(args.records))
        print('\n')
        create_device_cookie_dataset(int(args.records))
        print('\n')
        create_transactional_dataset(int(args.records))
        print('\n')
        fake.unique.clear()
    except Exception as e:
        print(f"Unexpected exception : {str(e)}")
        raise e

if __name__ == '__main__':
    main()