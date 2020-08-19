#!/bin/bash
if [[ $(ps aux|grep john|wc -l) != 1 ]]
then
	echo "STATUS: **ACTIVE**";
else
	echo "STATUS: *INACTIVE*";
fi


