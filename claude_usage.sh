#!/bin/env bash

response=$($(dirname $(readlink -f "$0"))/secret_claude_fetch_usage.sh)

percent=$(jq --join-output '.["five_hour"]["utilization"]' <<< "${response}")

reset=$(jq --join-output '.["five_hour"]["resets_at"]' <<< "${response}")
if [[ -n "$reset" && "$reset" != "null" ]]; then
    reset_unix=$(date -d "$reset" +%s)
    now_unix=$(date +%s)
    diff_unix=$((reset_unix - now_unix))
    diff_hours=$((diff_unix / 3600))
    diff_minutes=$(((diff_unix % 3600) / 60))
else
    diff_hours=0
    diff_minutes=0
fi


printf "%s%% (%d:%02d)" "$percent" "$diff_hours" "$diff_minutes"