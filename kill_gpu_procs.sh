#!/bin/bash
# kill all GPU processes using more than 100MB of memory
# build this into a setuid executable with:
# $ sudo shc -S -f kill_gpu_procs.sh -o kill_gpu_procs
# $ sudo chmod a+x kill_gpu_procs

# get all gpu processes
procs=$(nvidia-smi --query-compute-apps pid,used_gpu_memory --format csv,noheader,nounits)
# filter processes using a lot of memory
big_procs=$(awk -F',' '$2 > 100 {print $1}' <<< $procs)

# kill them all!

while read -r pid
do
    if [[ -n $pid ]]
    then
        echo killing $pid
	kill -9 $pid
    fi
done <<< $big_procs

