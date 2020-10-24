# ***************************************************************************************
#                   __ _                                                            _   
#   ___ ___  _ __  / _(_) __ _ _   _ _ __ ___       _ __  _ __ ___  _   _  ___  ___| |_ 
#  / __/ _ \| '_ \| |_| |/ _` | | | | '__/ _ \_____| '_ \| '__/ _ \| | | |/ _ \/ __| __|
# | (_| (_) | | | |  _| | (_| | |_| | | |  __/_____| |_) | | | (_) | |_| |  __/ (__| |_ 
#  \___\___/|_| |_|_| |_|\__, |\__,_|_|  \___|     | .__/|_|  \___/ \__, |\___|\___|\__|
#                        |___/                     |_|              |___/               
#                    
# ***************************************************************************************

# Text Format
#	* Variables containing the constant values of the text format 

BOLD=`tput bold`
UNDERLINE_ON=`tput smul`
UNDERLINE_OFF=`tput rmul`



# Text Color 
#	* Variables containing the constant values of the text color 

TEXT_BLUE=`tput setaf 4`
TEXT_BLACK=`tput setaf 0`
TEXT_RED=`tput setaf 1`
TEXT_GREEN=`tput setaf 2`
TEXT_YELLOW=`tput setaf 3`
TEXT_BLUE=`tput setaf 4`
TEXT_MAGENTA=`tput setaf 5`
TEXT_CYAN=`tput setaf 6`
TEXT_WHITE=`tput setaf 7`

RESET_FORMATTING=`tput sgr0`


# Argument capture

for ARGUMENT in "$@"
do

    KEY=$(echo $ARGUMENT | cut -f1 -d=)
    VALUE=$(echo $ARGUMENT | cut -f2 -d=)   

    case "$KEY" in
            MODULE)      MODULE=${VALUE} ;;
            REGISTRY)    REGISTRY=${VALUE} ;;
            *)   
    esac    


done

TEMPLATE_MODULE='helloworld'
TEMPLATE_REGISTRY='docker.pkg.github.com/vjmadrid/python-project-helloworld'

# Example de modulo 
# ./configure_project.sh MODULE="projectx" REGISTRY="docker.pkg.github.com/vjmadrid/projectx"

@echo -e "[${TEXT_BLUE}INFO${RESET_FORMATTING}] --- ${TEXT_GREEN}configure-project:rename-variables${RESET_FORMATTING} ${BOLD}(rename-variables)${RESET_FORMATTING} ---"
@echo -e "[${TEXT_BLUE}INFO${RESET_FORMATTING}]"

@echo -e "[${TEXT_BLUE}INFO${RESET_FORMATTING}] --- ${TEXT_GREEN}configure-project:rename-files${RESET_FORMATTING} ${BOLD}(rename-files)${RESET_FORMATTING} ---"
@echo -e "[${TEXT_BLUE}INFO${RESET_FORMATTING}]"

sed -i s/$DUMMY_MODULE/$MODULE/g dev.Dockerfile
# sed -i s/$DUMMY_MODULE/$MODULE/g prod.Dockerfile
# sed -i s/$DUMMY_MODULE/$MODULE/g tests/context.py
# sed -i s/$DUMMY_MODULE/$MODULE/g tests/test_app.py
# mv $DUMMY_MODULE $MODULE

# sed -i s/$DUMMY_MODULE/$MODULE/g pytest.ini
# sed -i s/$DUMMY_MODULE/$MODULE/g setup.cfg
# sed -i s/$DUMMY_MODULE/$MODULE/g sonar-project.properties
# sed -i s~$DUMMY_REGISTRY~$REGISTRY~g Makefile
# sed -i s/example/$MODULE/g Makefile
# sed -i s/$DUMMY_MODULE/$MODULE/g Makefile

# echo -e "\n${TEXT_BLUE}Testing if everything works...${RESET_FORMATTING}\n"

# echo -e "\n${TEXT_BLUE}Test: make run${RESET_FORMATTING}\n"
# make run
# echo -e "\n${TEXT_BLUE}Test: make test${RESET_FORMATTING}\n"
# make test
# echo -e "\n${TEXT_BLUE}Test: make build-dev${RESET_FORMATTING}\n"
# make build-dev

