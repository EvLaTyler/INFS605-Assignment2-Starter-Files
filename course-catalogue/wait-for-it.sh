#!/usr/bin/env bash
set -e

host="$1"
port="$2"
shift 2
cmd="$@"

# Simple TCP wait loop
until nc -z "$host" "$port"; do
  >&2 echo "Waiting for $host:$port..."
  sleep 2
done

>&2 echo "$host:$port is available — starting service"
exec $cmd

# This is a universal wait-for-it.sh file for use by each of the microservices in this system.

