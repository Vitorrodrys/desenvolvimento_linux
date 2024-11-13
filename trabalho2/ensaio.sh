#!/bin/bash

function get_command_runnable() {
    command_file=$1
    awk '/COMANDO:/ { getline; print }' "$command_file"
}

function get_factor_or_rehearsal() {
    command_file=$1
    factor_name=$2
    factor_or_rehearsal=$3
    awk -v factor_name="$factor_name" -v factor_or_rehearsal="$factor_or_rehearsal" '
    $0 ~ factor_or_rehearsal {
        # Após encontrar a linha com "FATORES:" ou "REHEARSAL:", comece a ler as linhas subsequentes
        while (getline) {
            if ($1 == factor_name) {
                # Imprimir a partir do terceiro campo
                for (i = 3; i <= NF; i++) {
                    printf "%s ", $i
                }
                print ""  # Para imprimir a nova linha
                break
            }
        }
    }' "$command_file" | sed -E 's/[^0-9 *]+|,//g'
}

function get_factor() {
    config_file=$1
    factor_name=$2
    get_factor_or_rehearsal "$config_file" "$factor_name" "FATORES:"
}

function get_rehearsal() {
    # config file = the configuration file where is the rehearsals and factores
    # rehearsal_name = the name of the rehearsal that you want to get of the file
    config_file=$1
    rehearsal_name=$2
    get_factor_or_rehearsal "$config_file" "$rehearsal_name" "ENSAIOS:"
}

