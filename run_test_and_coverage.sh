#!/usr/bin/env bash
pytest && coverage run --branch --source gilded_rose,gilded_rose_test gilded_rose_test.py && coverage report -m && coverage html

{ exec 3<>/dev/tcp/127.0.0.1/8000; } > /dev/null 2>&1 || PORT_IS_FREE="yes"
if [ -z $PORT_IS_FREE ]; then
	echo "HTTP server running"
else
  echo "Starting HTTP server for code coverage"
	nohup python -m http.server 8000 -d htmlcov &
fi
