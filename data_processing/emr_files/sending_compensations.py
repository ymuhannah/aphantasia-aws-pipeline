import boto3
import pandas as pd
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from datetime import datetime
from num2words import num2words
from io import BytesIO

# Create S3 and SES clients
s3 = boto3.client('s3')
ses = boto3.client('ses', region_name='us-east-1')  # Change region if necessary

# Define bucket and file names
bucket1 = 'sending-egift-cards-parquet'
bucket2 = 'testing-exp-data-parquet'
egift_cards_file = 'egift_cards.parquet'
participants_data_file = 'participants_data.parquet'
compensation_message_file = 'compensation_message.txt'

# Email subject and custom values
email_subject = 'eGift Payment'
study_title = 'Memory for visual content'
experiment_value = 'Aphantasia Dual-coding'
experimenter_value = 'Hannah'
gift_card_value = 10
sender_email = 'ymuhannah@uchicago.edu'  # Replace with your verified SES email address

# Download files from S3
obj1 = s3.get_object(Bucket=bucket1, Key=egift_cards_file)
egift_df = pd.read_parquet(BytesIO(obj1['Body'].read()))

obj2 = s3.get_object(Bucket=bucket2, Key=participants_data_file)
participants_df = pd.read_parquet(BytesIO(obj2['Body'].read()))

s3.download_file(bucket1, compensation_message_file, compensation_message_file)

# Load compensation message template
with open(compensation_message_file, 'r') as file:
    message_template = file.read()

# Function to send email via SES
def send_email(subject, message, recipient):
    try:
        response = ses.send_email(
            Source=sender_email,
            Destination={
                'ToAddresses': [recipient],
            },
            Message={
                'Subject': {
                    'Data': subject,
                },
                'Body': {
                    'Text': {
                        'Data': message,
                    },
                },
            },
        )
        return response
    except (NoCredentialsError, PartialCredentialsError) as e:
        print(f"Error sending email: {e}")
        return None

# Process participants with egift-card-sent == 0
for index, participant in participants_df[participants_df['egift-card-sent'] == 0].iterrows():
    email_address = participant['EmailAddress']
    
    # Find the first unsent gift card with matching value or combine multiple if needed
    matching_cards = egift_df[egift_df['Sent'] == 0]
    amount_list = matching_cards['Amount'].tolist()
    code_list = matching_cards['Code'].tolist()
    
    selected_codes = []
    total_amount = 0
    i = 0
    
    while total_amount < gift_card_value and i < len(amount_list):
        total_amount += amount_list[i]
        selected_codes.append(code_list[i])
        i += 1
    
    # Check if enough gift card value is found
    if total_amount == gift_card_value:
        # Prepare notification message
        if len(selected_codes) == 1:
            is_are = 'is'
            number_of_gift_cards = ''
            code_codes = 'code'
            this_these_codes = 'this code'
        else:
            is_are = 'are'
            number_of_gift_cards = num2words(len(selected_codes)) + ' '
            code_codes = 'codes'
            this_these_codes = 'these codes'

        amount = amount_list[0] if len(selected_codes) == 1 else gift_card_value // len(selected_codes)
        retailer = matching_cards.iloc[0]['Retailer']
        codes = '\n'.join(selected_codes)
        
        notification_message = message_template.replace('[Study title]', study_title)\
                                               .replace('[is/are]', is_are)\
                                               .replace('[Number of gift card]', number_of_gift_cards)\
                                               .replace('[$ Amount & Retailer]', f'${amount} {retailer}')\
                                               .replace('[Code]', codes)\
                                               .replace('[code/codes]', code_codes)\
                                               .replace('[this code/these codes]', this_these_codes)
        
        # Send email
        response = send_email(email_subject, notification_message, email_address)
        if response:
            print(f"Email sent to {email_address}")

            # Update participants_data.parquet
            participants_df.at[index, 'egift-card-sent'] = 1

            # Update egift_cards.parquet
            for code in selected_codes:
                card_index = egift_df[egift_df['Code'] == code].index[0]
                egift_df.at[card_index, 'Experiment'] = experiment_value
                egift_df.at[card_index, 'Subject ID'] = email_address
                egift_df.at[card_index, 'Experimenter'] = experimenter_value
                egift_df.at[card_index, 'Date Given'] = datetime.now().strftime('%Y-%m-%d')
                egift_df.at[card_index, 'Sent'] = 1

# Save updated DataFrames back to Parquet files
participants_buffer = BytesIO()
participants_df.to_parquet(participants_buffer, index=False)
participants_buffer.seek(0)

egift_buffer = BytesIO()
egift_df.to_parquet(egift_buffer, index=False)
egift_buffer.seek(0)

# Upload updated files back to S3
s3.put_object(Bucket=bucket2, Key=participants_data_file, Body=participants_buffer.getvalue())
s3.put_object(Bucket=bucket1, Key=egift_cards_file, Body=egift_buffer.getvalue())

print("All notifications sent and Parquet files updated successfully.")
