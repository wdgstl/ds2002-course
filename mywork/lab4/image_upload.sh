#!/bin/bash

aws s3 cp blues.png s3://ds2002-spq4pq/

aws s3 presign --expires-in 604800 s3://ds2002-spq4pq/blues.png

##presigned URL: https://ds2002-spq4pq.s3.amazonaws.com/blues.png?AWSAccessKeyId=AKIAXYKJUFKQBQQELF7W&Signature=qus9JmqY11nB91qgn7suFnuLM94%3D&Expires=1709605042
