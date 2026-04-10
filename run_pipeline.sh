#!/bin/bash

for i in {1..3}
do
  echo "Run $i"
  docker run -v $(pwd):/app pipelineapp
  sleep 5
done
