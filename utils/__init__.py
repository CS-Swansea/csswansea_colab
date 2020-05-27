
def execute_command(cmd):
  import re, subprocess
  prc       = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  stdout, _ = prc.communicate()
  return re.sub(r'\W*\n+', '\n', stdout.decode('ascii')).strip('\n')