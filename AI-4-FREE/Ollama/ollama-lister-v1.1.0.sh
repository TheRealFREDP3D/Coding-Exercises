#!/bin/bash

# ┌────────────────────────────────────────────────────────────────────────────────┐
# │ ollama_lister.sh                                                               │
# │ Author:       Frederick Pellerin (Improved by AI Assistant)                    │
# │ X/GitHub:     @TheRealFredP3D                                                  │
# │ Date:         16-07-2027                                                       │
# │ Version:      1.1.0                                                            │
# └────────────────────────────────────────────────────────────────────────────────┘

# ----------------------------------------------------------------------------------

# This script lists Ollama models installed on the system. It provides options to
# display full or short model names, with or without color output. The script checks
# if Ollama is installed, retrieves the list of models, and formats the output for
# easy readability. It also includes error handling for various scenarios. It add
# an alias 'ollamal' to your shell config file if it doesn't already exist.

# ----------------------------------------------------------------------------------

#Usage: ./ollama-lister-v2.sh [OPTIONS] 

#Options:
#  -h, --help     Show this help message
#  -v, --version  Show version information
#  -f, --full     Show only full model names
#  -s, --short    Show only short model names
#  --no-color     Disable colored output

# ----------------------------------------------------------------------------------

VERSION="1.1.0"

# ANSI color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print formatted headers
print_header() {
    local header_text="$1"
    local width=78
    printf "┌%s┐\n" "$(printf '%.0s─' $(seq 1 $width))"
    printf "│%-${width}s│\n" "$header_text"
    printf "└%s┘\n" "$(printf '%.0s─' $(seq 1 $width))"
}

# Function to check if Ollama is installed
check_ollama_installed() {
    if ! command -v ollama &> /dev/null; then
        echo -e "${RED}Error: Ollama is not installed or not in PATH.${NC}"
        exit 1
    fi
}

# Function to list Ollama models
list_models() {
    local list_type="$1"
    local models
    models=$(ollama list 2>/dev/null)
    
    if [ $? -ne 0 ] || [ -z "$models" ]; then
        echo -e "${RED}Error: Failed to retrieve Ollama models or no models found.${NC}"
        exit 1
    fi
    
    case "$list_type" in
        "full")
            echo "$models" | awk '{ print $1 }' | column
            ;;
        "short")
            echo "$models" | awk -F':' '{ print $1 }' | column
            ;;
        *)
            echo "$models" | column -t
            ;;
    esac
}

# Function to add alias if not exists
add_alias_if_not_exists() {
    local alias_name="$1"
    local alias_command="$2"
    local config_file="$3"
    
    if ! grep -q "alias $alias_name=" "$config_file"; then
        echo "alias $alias_name='$alias_command'" >> "$config_file"
        echo -e "${GREEN}Alias $alias_name added to $config_file${NC}"
    else
        echo -e "${YELLOW}Alias $alias_name already exists in $config_file${NC}"
    fi
}

# Function to display help message
show_help() {
    echo "Usage: $0 [OPTIONS]"
    echo "Options:"
    echo "  -h, --help     Show this help message"
    echo "  -v, --version  Show version information"
    echo "  -f, --full     Show only full model names"
    echo "  -s, --short    Show only short model names"
    echo "  --no-color     Disable colored output"
}

# Parse command line arguments
SHOW_FULL=false
SHOW_SHORT=false
USE_COLOR=true

while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            show_help
            exit 0
            ;;
        -v|--version)
            echo "ollama_lister.sh version $VERSION"
            exit 0
            ;;
        -f|--full)
            SHOW_FULL=true
            shift
            ;;
        -s|--short)
            SHOW_SHORT=true
            shift
            ;;
        --no-color)
            USE_COLOR=false
            shift
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}" >&2
            show_help
            exit 1
            ;;
    esac
done

if [ "$USE_COLOR" = false ]; then
    RED=''
    GREEN=''
    YELLOW=''
    BLUE=''
    NC=''
fi

# Main script execution
check_ollama_installed

print_header "OLLAMA LAZY LISTER"

if [ "$SHOW_FULL" = true ]; then
    print_header "Full Name"
    list_models "full"
elif [ "$SHOW_SHORT" = true ]; then
    print_header "Short Name"
    list_models "short"
else
    list_models "all"
fi

# Detect the current shell and set config file
if [ -n "$ZSH_VERSION" ]; then
    config_file="$HOME/.zshrc"
elif [ -n "$BASH_VERSION" ]; then
    config_file="$HOME/.bashrc"
else
    echo -e "${RED}Unsupported shell. Only Bash and Zsh are supported.${NC}"
    exit 1
fi

# Add alias
script_path=$(readlink -f "$0")
add_alias_if_not_exists "ollamal" "$script_path" "$config_file"

echo -e "${BLUE}Remember to run 'source $config_file' to apply the changes in your current session.${NC}"
