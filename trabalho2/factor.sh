#!/bin/bash

function get_factor() {
    config_file=$1
    factor_name=$2
    get_factor_or_rehearsal "$config_file" "$factor_name" "FATORES:"
}

function is_an_element(){
    config_file=$1
    element=$2
    factor=$3
    factor_elements=$(get_factor $config_file $factor)
    echo $factor_elements | grep -w $element > /dev/null 2>&1
    return $?
}
function factor_exists(){
    config_file=$1
    factor=$2

    [ -n "$(get_factor $config_file $factor)" ]
}
function increment_char(){
    current=$1
    number=$2
    ascii=$(printf "%d" "'$current'")
    ascii=$((ascii + number))
    new_char=$(printf "%b" "\x$(printf %x $ascii)")
    echo "$new_char"
}
function increment_factor(){
    current=$1
    echo $(increment_char $current 1)
}
function get_factor_by_number() {
    factor_number=$1
    echo $(increment_char A $factor_number)
}