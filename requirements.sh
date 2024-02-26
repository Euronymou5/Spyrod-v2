# Simple modificacion del archivo de instalacion requirements.sh

function install() {
   clear
   echo -e "\033[32m[~] Actualizando paquetes..."
   apt update

   sleep 3
   which python3 > /dev/null 2>&1
   if [ "$?" -eq "0" ]; then
   echo -e "\033[32m\n[~] Python3 ya esta instalado."
   else
   echo -e "\033[31m\n[!] Python3 no esta instalado."
   sleep 2
   echo -e "\033[32m\n[~] Instalando python3..."
   apt install python3 -y
   fi

   echo -e "\033[32m\nInstalando requerimientos...\n"
   pip3 install -r requirements.txt
   
   echo -e "\n\033[32m[✔] Instalacion completada."
   echo -e "\n[~] Utiliza el comando: python3 spyrod.py para iniciar la herramienta."
}

install
