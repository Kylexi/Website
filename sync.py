import os

s3_str = "aws s3 sync . s3://matthewcampbell.io"
s3_str_www = "aws s3 sync . s3://www.matthewcampbell.io"

exclude = ' --exclude "*.git*" --exclude "*.py"'
os.system(s3_str + exclude)
os.system(s3_str_www + exclude)
print("S3 sync successful!")