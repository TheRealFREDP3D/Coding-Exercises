# - the challenge checks for a specific parent process : python
# - the challenge will check that the environment is empty (except LC_CTYPE, which is impossible to get rid of in some cases)

import subprocess
result = subprocess.check_output(
    ["/challenge/embryoio_level28"],
    env={"LC_CTYPE": "C"},
    stderr=subprocess.STDOUT
)
print(result.decode("utf-8"))
