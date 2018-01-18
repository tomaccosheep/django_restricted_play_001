#!/bin/bash
python3 ./manage.py runserver 8001 & echo $! > ./pid_log.txt
