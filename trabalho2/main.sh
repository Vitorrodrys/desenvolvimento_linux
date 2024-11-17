#!/bin/bash
source ./rehearsal.sh
source ./helper.sh

function replace_rehearsal_params() {
    config_file=$1
    rehearsal_params=$2

    command=$(get_command_runnable $config_file)
    factor=A
    for param in $rehearsal_params; do
        if ! factor_exists $CONFIG_FILENAME $factor;then
            echo "The factor $factor does not exists on factors specify"
            exit 1
        fi
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
function help() {
    echo "usage: main.sh CONFIGFILE.TXT"
    exit $1
}
function main() {
    if [ "$1" == "-h" ];then
        help 0
    elif [ $# -lt 1 ];then
        help 1
    fi

    CONFIG_FILENAME=$1
    current_rehearsal=1
    while exists_rehearsal $CONFIG_FILENAME $current_rehearsal; do
        echo "Rehearsal $rehearsal"
        expanded_rehearsal=$(expand_rehearsal_list $CONFIG_FILENAME $current_rehearsal)
        exec_rehearsal $config_file "$expanded_rehearsal"
        echo -e "____________________________________________________________\n\n\n\n\n"
        current_rehearsal=$((current_rehearsal + 1))
    done
}

main $@ 