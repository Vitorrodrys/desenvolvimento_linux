#!/bin/bash
source factor.sh
source helper.sh


function get_rehearsal() {
    # config file = the configuration file where is the rehearsals and factores
    # rehearsal_name = the name of the rehearsal that you want to get of the file
    local config_file=$1
    local rehearsal_number=$2
    get_factor_or_rehearsal "$config_file" "$rehearsal_number" "ENSAIOS:"
}

function expand_with_all_factor_elements() {
    local config_file=$1
    local factor_name=$2
    local current_elements=$3
    local factor_elements=$(get_factor $config_file $factor_name)

    local new=""
    for factor_element in $factor_elements; do
        if [ -z "$new" ]; then
            new=$(echo "$current_elements" | sed -E "s/$/ $factor_element/")
        else
            new="$new\n$(echo "$current_elements" | sed -E "s/$/ $factor_element/")"
        fi
    done
    echo -e "$new"
}

function expand_rehearsal_list() {
    local config_file=$1
    local rehearsal_number=$2
    local rehearsal
    local expanded
    local factor
    local list=""
    
    rehearsal="$(get_rehearsal "$config_file" "$rehearsal_number")"

    rehearsal_safe=$(echo "$rehearsal" | sed 's/\*/__ASTERISK__/g')

    factor="A"

    IFS=' '
    for param in $rehearsal_safe; do
        param=$(echo "$param" | sed 's/__ASTERISK__/*/g')

        if [ "$param" != "*" ]; then
            if ! is_an_element "$config_file" "$param" "$factor"; then
                echo "Invalid element $param for factor $factor" > /dev/stderr
                exit 1
            fi
            if [ -z "$list" ]; then
                list="$param"
            else
                list=$(echo "$list" | sed -E "s/$/ $param/")
            fi
        else
            list=$(expand_with_all_factor_elements "$config_file" "$factor" "$list")
        fi
        factor=$(increment_factor "$factor")
    done

    echo "$list" | awk 'NF'
}

function exists_rehearsal() {
    config_file=$1
    rehearsal_number=$2
    rehearsal=$(get_rehearsal $config_file $rehearsal_number)
    if [ -z "$rehearsal" ]; then
        return 1 # false
    fi
    return 0 # true
}