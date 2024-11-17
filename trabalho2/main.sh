#!/bin/bash
source ./rehearsal.sh
source ./helper.sh

CONFIG_FILENAME=config.txt

function replace_rehearsal_params() {
    config_file=$1
    rehearsal_params=$2

    command=$(get_command_runnable $config_file)
    factor=A
    for param in $rehearsal_params; do
        command=$(echo $command | sed "s/\\\$$factor/$param/")
        factor=$(increment_factor $factor)
    done
    echo $command
}

function exe() {
    echo "running now:"
    echo "$@"
    "$@"
}

function exec_rehearsal() {
    config_file=$1
    expanded_rehearsal=$2

    while read -r rehearsal_params; do
        command=$(replace_rehearsal_params $config_file "$rehearsal_params")
        exe $command
    done <<< "$expanded_rehearsal"
}
function main() {
    current_rehearsal=1
    while exists_rehearsal $CONFIG_FILENAME $current_rehearsal; do
        echo "Rehearsal $rehearsal"
        expanded_rehearsal=$(expand_rehearsal_list $CONFIG_FILENAME $current_rehearsal)
        exec_rehearsal $config_file "$expanded_rehearsal"
        echo "____________________________________________________________"
        current_rehearsal=$((current_rehearsal + 1))
    done
}

main 