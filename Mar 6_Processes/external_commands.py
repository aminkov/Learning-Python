import subprocess
# subprocess.call(["date", "+%H:%M:%S"])

# TASK PRint the current working directory

cd = subprocess.check_output("cd")

print(cd)
