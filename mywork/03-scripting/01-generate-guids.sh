#!/bin/bash

set -e

for i in {1..1000}
do
  /usr/bin/uuidgen
done > guids.list
