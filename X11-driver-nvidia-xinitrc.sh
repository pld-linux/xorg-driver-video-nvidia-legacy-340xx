#!/bin/sh
if [ -r ~/.nvidia-settings-rc ]; then
	/usr/X11R6/bin/nvidia-settings -l > /dev/null 2>&1
fi
