#!/bin/bash
source ./ensaio.sh
source ./helper.sh

CONFIG_FILENAME=config.txt

function gen_commands() {
    original_command=$(get_command_runnable $CONFIG_FILENAME)
    current_script=$1
    current_factor=$2
    factors_options=$(get_factor $CONFIG_FILENAME $current_factor)
    factor_option_number=1
    for factor in $factors_options;do
        new_command=$(echo $original_command | sed -E "s/$current_factor/$current_factor$factor_option_number/")
        current_script="$current_script;$new_command"
    done
    echo $current_script
}
function generate_rehearsal_shell() {
    #script=echo $A1 $B $C;echo $A2 $B $C
    script="$(get_command_runnable config.txt);"
    factor_char=A
    for i in $(get_command_runnable config.txt);do
        if echo $i | grep '\$';then
            if [ ${i:1:1} == "*" ];then
                script=$(gen_commands $script $factor_char)
            fi
            factor_char=$(increment_char $factor_char)
        fi
    done
    echo $script
}

function main() {
    current_rehearsal=1

   generate_rehearsal_shell
}
main