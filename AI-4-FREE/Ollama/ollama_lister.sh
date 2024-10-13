      `#!/bin/bash

      #  ┌──────────────────────────────────────────────────────────────────────────┐
      #  │ ollama_lister.sh                                                         │  
      #  │ Author:       Frederick Pellerin                                         │
      #  │ X/GitHub:     @TheRealFredP3D                                            │
      #  │ Date:         16-07-2027                                                 │
      #  │ Change log:   17-07-2027 - Fix - the script was adding a alias when one  │
      #  │                                  already existed.                        │
      #  └──────────────────────────────────────────────────────────────────────────┘

      # 1.Download the file`ollama_list.sh`
      # 'https://github.com/TheRealFREDP3D/AI-4-FREE/blob/main/Ollama/ollama_lister.sh'

      # 2. Make the file executable by running:
      # `chmod +x ollama_lister.sh`

      # 3. Run the script using:
      #./ollama_list.sh

      echo "┌──────────────────────────────────────────────────────────────────────────┐"
      echo "│ ollama_lister.sh                                                         │"
      echo "│ A tool designed to make life easier for people who frequently work       │"
      echo "│ with multiple Ollama AI models, providing a quick and visually appealing │"
      echo "│ way to view and manage their model list.                                 │"
      echo "│ This script detect your active shell, check if the alias 'ollamal' exist.│"
      echo "│ If not, add it to your shell config file.                                │"
      echo "└──────────────────────────────────────────────────────────────────────────┘"
      echo ""
      echo "┌──────────────────────────────────────────────────────────────────────────┐"
      echo "│                            OLLAMA LAZY LISTER                            │"
      echo "└──────────────────────────────────────────────────────────────────────────┘"
      ollama list

      echo ""
      echo "****************************************************************************"
      echo ""

      echo "┌──────────────────────────────────────────────────────────────────────────┐"
      echo "│                                 Full Name                                │"
      echo "└──────────────────────────────────────────────────────────────────────────┘"
      awk '{ print $1 }' <(ollama list)

      echo ""
      echo "****************************************************************************"
      echo ""

      echo "┌──────────────────────────────────────────────────────────────────────────┐"
      echo "│                                 Short Name                                │"
      echo "└──────────────────────────────────────────────────────────────────────────┘"
      awk -F':' '{ print $1 }' <(ollama list)

      echo ""
      echo "****************************************************************************"
      echo ""

      # Detect the current shell
      if [ -n "$ZSH_VERSION" ]; then
          config_file="$HOME/.zshrc"
      elif [ -n "$BASH_VERSION" ]; then
          config_file="$HOME/.bashrc"
      else
          echo "Unsupported shell. Only Bash and Zsh are supported." 
          exit 1
      fi

      add_alias_if_not_exists() {
        local alias_name="$1"
        local alias_command="$2"
        local config_file="$3"
        
        if ! grep -q "alias $alias_name=" "$config_file"; then
          echo "alias $alias_name='$alias_command'" >> "$config_file"
          echo "Alias $alias_name added to $config_file"
        else
          echo "Alias $alias_name already exists in $config_file"
        fi
      }

      add_alias_if_not_exists "ollamal" "$PWD/ollama_lister.sh" "$config_file"

      # Remind the user to source the config file
      echo "Remember to run 'source $config_file' to apply the changes in your current session."
