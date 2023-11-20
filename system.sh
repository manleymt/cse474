#!/usr/bin/env bash
# ------------------------------------------------------------------------------
# An executable shell script to make administrative tasks easier. 
# ------------------------------------------------------------------------------

set -o errexit
set -o pipefail

# Removes cached files.
function clean {
  docker compose down --remove-orphans -v --rmi all 
}

# Displays script help.
function help {
  printf "%s <task> [args]\n\nTasks:\n" "${0}"
  compgen -A function | grep -v "^_" | cat -n
  printf "\nExtended help:\n  Each task has comments for general usage\n"
}

# Opens a shell in the given container
function shell {
  docker compose exec "${1}" bash
}

# Starts the docker containers
function start {
  docker compose up "${@}"
}

# Stops and removes docker containers.
function stop {
  docker compose down "${@}"
}

# Runs python unit tests on wsgi.
function validate {
  docker compose exec app pytest test -v
}

# Ensures all quality checks pass.
function verify {
  docker compose exec app flake8 qa/webapp
}

TIMEFORMAT=$'\nTask completed in %3lR'
time "${@:-help}"