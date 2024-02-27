import boto3
import urllib.request

#fetch image - https://docs.python.org/3/library/urllib.request.html
with urllib.request.urlopen("https://media.tenor.com/Rd6ULrCRvlQAAAAM/funny-dog-funny-animals.gif") as response:
    image = response.read()

# create client
s3 = boto3.client('s3', region_name="us-east-1")

# make request - upload the image to bucket 
response = s3.put_object(
    Body = image,
    Bucket = "ds2002-spq4pq",
    Key = "dog.gif"
)
# make request - generate presigned url
url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': 'ds2002-spq4pq', 'Key': 'dog.gif'},
    ExpiresIn=604800
    )

#Output the url
print(f"Presigned URL: {url}")

#Presigned URL: https://ds2002-spq4pq.s3.amazonaws.com/dog.gif?AWSAccessKeyId=AKIAXYKJUFKQBQQELF7W&Signature=mvLMOCeskXJKjTa3344eiFW4tD0%3D&Expires=1709608418

