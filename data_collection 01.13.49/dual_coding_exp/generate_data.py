import pandas as pd
import pymysql
import boto3
import os
import logging

# Setting up logging
logging.basicConfig(level=logging.INFO)

bucket_name = ''
db_host = ''
db_user = ''
db_password = ''
db_name = ''

# AWS credentials
aws_access_key_id=''
aws_secret_access_key=''
aws_session_token=''

# Connect to the database
try:
    db = pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    logging.info("Connected to the database successfully.")
except Exception as e:
    logging.error(f"Failed to connect to database: {e}")
    exit(1)

# Function to fetch data from the database and save it as a Parquet file
def fetch_data_and_save_parquet():
    files_dir = '/var/www/html/files'
    cursor = db.cursor()
    cursor.execute("SELECT * FROM EmailAddressInput")
    email_data = cursor.fetchall()
    logging.info(f"Fetched email data: {email_data}")
    
    cursor.execute("SELECT * FROM Demographics")
    demo_data = cursor.fetchall()
    logging.info(f"Fetched demographics data: {demo_data}")

    cursor.execute("SELECT * FROM VVIQResponses")
    vviq_data = cursor.fetchall()
    logging.info(f"Fetched VVIQ responses data: {vviq_data}")

    cursor.execute("SELECT * FROM AttentionCheck")
    attention_check_data = cursor.fetchall()
    logging.info(f"Fetched attention check data: {attention_check_data}")

    for email_entry in email_data:
        email = email_entry['EmailAddress']
        prefix = email.split('@')[0]
        file_name = os.path.join(files_dir, f'{prefix}.parquet')
        
        demo_entry = next((item for item in demo_data if item['EmailAddress'] == email), None)
        vviq_entry = next((item for item in vviq_data if item['EmailAddress'] == email), None)
        attention_check_entry = next((item for item in attention_check_data if item['EmailAddress'] == email), None)
        
        logging.info(f"Demo entry for {email}: {demo_entry}")
        logging.info(f"VVIQ entry for {email}: {vviq_entry}")
        logging.info(f"Attention check entry for {email}: {attention_check_entry}")

        if demo_entry and vviq_entry and attention_check_entry:
            data = {
                'EmailAddress': [email_entry['EmailAddress']],
                'FutureContactConsent': [email_entry['FutureContactConsent']],
                'Age': [demo_entry['Age']],
                'Sex': [demo_entry['Sex']],
                'Ethnicity': [demo_entry['Ethnicity']],
                'Race': [demo_entry['Race']],
                'VVIQ_Q1': [vviq_entry['VVIQ_Q1']],
                'VVIQ_Q2': [vviq_entry['VVIQ_Q2']],
                'VVIQ_Q3': [vviq_entry['VVIQ_Q3']],
                'VVIQ_Q4': [vviq_entry['VVIQ_Q4']],
                'VVIQ_Q5': [vviq_entry['VVIQ_Q5']],
                'VVIQ_Q6': [vviq_entry['VVIQ_Q6']],
                'VVIQ_Q7': [vviq_entry['VVIQ_Q7']],
                'VVIQ_Q8': [vviq_entry['VVIQ_Q8']],
                'VVIQ_Q9': [vviq_entry['VVIQ_Q9']],
                'VVIQ_Q10': [vviq_entry['VVIQ_Q10']],
                'VVIQ_Q11': [vviq_entry['VVIQ_Q11']],
                'VVIQ_Q12': [vviq_entry['VVIQ_Q12']],
                'VVIQ_Q13': [vviq_entry['VVIQ_Q13']],
                'VVIQ_Q14': [vviq_entry['VVIQ_Q14']],
                'VVIQ_Q15': [vviq_entry['VVIQ_Q15']],
                'VVIQ_Q16': [vviq_entry['VVIQ_Q16']],
                'IdealParticipation': [attention_check_entry['IdealParticipation']],
                'AttentionCheckTask': [attention_check_entry['AttentionCheckTask']]
            }
            df = pd.DataFrame(data)
            df.to_parquet(file_name, index=False)
            logging.info(f"Saved data to Parquet file: {file_name}")
            upload_to_s3(file_name, f'{prefix}.parquet')

# Function to upload the Parquet file to S3
def upload_to_s3(file_path, s3_key):
    try:
        s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token,
            region_name='us-east-1'
        )
        s3_client.upload_file(file_path, bucket_name, s3_key)
        logging.info(f"Uploaded '{file_path}' to S3 bucket with key '{s3_key}'.")
    except Exception as e:
        logging.error(f"Failed to upload file to S3: {e}")

# Main function
def main():
    fetch_data_and_save_parquet()

if __name__ == "__main__":
    main()
