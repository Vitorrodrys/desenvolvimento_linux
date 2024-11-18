#!/bin/bash
# Trabalha pratico 2 - Desenvolvimento em Linux
#
# Alunos:
#   - Vitor Gabriel Correia Rodrigues - 0071054
#   - Higor Gabriel Lino Silva - 0070308


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
    start_time=$(date +%s%N) # Captura o tempo de início em nanosegundos
    echo "Running now:"
    echo "$@"
    "$@"
    end_time=$(date +%s%N)

    # Calcula o tempo decorrido em milissegundos
    elapsed_ns=$((end_time - start_time))
    elapsed_ms=$((elapsed_ns / 1000000))

    # Converte para o formato horas:minutos:segundos.milisegundos
    hours=$((elapsed_ms / 3600000))
    minutes=$(((elapsed_ms / 60000) % 60))
    seconds=$(((elapsed_ms / 1000) % 60))
    milliseconds=$((elapsed_ms % 1000))

    # Exibe o tempo formatado
    printf "Execution time: %02d:%02d:%02d.%03d\n" "$hours" "$minutes" "$seconds" "$milliseconds"
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
    echo "usage: main.sh CONFIGFILE.TXT SAIDA.TXT"
    exit $1
}

function worker() {
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
function main() {
    if [ "$1" == "-h" ];then
        help 0
    elif [ $# -lt 2 ];then
        help 1
    fi

    CONFIG_FILENAME=$1
    output_filename=$2
    worker $CONFIG_FILENAME > $output_filename
}

main $@ 