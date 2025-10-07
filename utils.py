import boto3
import datetime
import io

def s3_client(region):
    return boto3.client("s3", region_name=region)

def upload_parquet_to_s3(bucket, key, parquet_bytes, region="us-east-1"):
    s3 = s3_client(region)
    s3.put_object(Bucket=bucket, Key=key, Body=parquet_bytes)
    print(f"Uploaded: s3://{bucket}/{key}")

def make_s3_key(table, season):
    today = datetime.date.today().isoformat()
    return f"nfl/bronze/{table}/season={season}/run_date={today}/{table}.parquet"