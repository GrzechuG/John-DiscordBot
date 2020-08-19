#!/bin/bash
kill -9 $(ps aux|grep john|grep -v 'grep'|awk '{print $2}'|head -n 1)
