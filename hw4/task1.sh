#!/bin/bash

pid=$(ps aux | grep "[b]ash infinite.sh" | awk '{print $2}') && { kill -9 $pid && echo "Process infinite.sh with pid: $pid is killed."; } || echo "Process infinite.sh not running."
