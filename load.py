import io
import polars as pl
from utils import upload_parquet_to_s3, make_s3_key
from config import NFL_S3_BUCKET, AWS_REGION

def upload_df(df: pl.DataFrame, table: str, season: int):
    buffer = io.BytesIO()
    df.write_parquet(buffer)
    buffer.seek(0)
    key = make_s3_key(table, season)
    upload_parquet_to_s3(NFL_S3_BUCKET, key, buffer.getvalue(), region=AWS_REGION)