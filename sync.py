import os

s3_str = "aws s3 sync . s3://matthewcampbell.io"
s3_str_www = "aws s3 sync . s3://www.matthewcampbell.io"

exclude = ' --exclude "*.git*" --exclude "*.py"'
try:
	os.system(s3_str + exclude)
	os.system(s3_str_www + exclude)
except Exception as e:
	print(e)
print("S3 sync successful!")

