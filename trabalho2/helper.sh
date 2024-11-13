

function increment_char(){
    current=$1
    ascii=$(printf "%d" "'$current'")
    ascii=$((ascii + 1))
    new_char=$(printf "%b" "\x$(printf %x $ascii)")
    echo "$new_char"
}