#!/usr/bin/python3
# displays only the status code of the response.
curl -so /dev/null -w "%{http_code}" "$1"
