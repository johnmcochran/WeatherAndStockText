import boto3
from botocore.exceptions import ClientError
import os
import json


def get_variable(variable_name):
    region_name = "us-east-2"
    secret_name = "WeatherAndStockTextVariables"
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name,
        aws_access_key_id=os.getenv('etl_user_access_key'), # todo: add variables to astro variables
        aws_secret_access_key=os.getenv('etl_user_secret_access_key')
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = get_secret_value_response['SecretString']
    secret = json.loads(secret)
    variable_value = secret[variable_name]
    return variable_value