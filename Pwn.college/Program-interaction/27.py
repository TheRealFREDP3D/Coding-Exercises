# hacker@program-interaction~level27:/challenge$ ./embryoio_level27 
# WELCOME! This challenge makes the following asks of you:
# - the challenge checks for a specific parent process : python
# - the challenge will check that output is redirected to a specific file path : /tmp/dkinmb

import subprocess

# Execute the command and save the output to a file
subprocess.run(["/challenge/embryoio_level27"], stdout=open("/tmp/dkinmb", "w"))

# Open the file and print its content
with open("/tmp/dkinmb") as f:
    print(f.read())