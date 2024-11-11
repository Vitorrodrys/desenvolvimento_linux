# Aluno: Higor Gabriel Lino Silva
# Mat.: 0070308

#Aluno: Vitor Gabriel Correia Rodrigues
# Mat.: 0071054

#Funcao que cria as pastas
function cria_pasta_destino(){
	origem=$1
	destino=$2

	if [[ -d "$destino" ]]; then
		echo "já criado"
	else
		mkdir -p "$destino"
	fi
}

function cria_subpastas_e_copia(){
	origem=$1
	destino=$2

	for file in "$origem"/*; do
		if [[ -f "$file" ]]; then
			if [[ "$file" == *.* ]]; then
				extension="${file##*.}"
			else
				extension="(vazio)"
			fi
			
			if [[ -d "$destino/$extension" ]]; then
				echo "já criado"
			else
				mkdir -p "$destino/$extension"
			fi

			cp "$file" "$destino/$extension"
		fi
	done
}

cria_pasta_destino "$1" "$2"
cria_subpastas_e_copia "$1" "$2"
