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
