
def execute_command(cmd, verbose=False):
  import re, subprocess

  if verbose:
  	print('++', cmd)

  prc       = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  stdout, _ = prc.communicate()
  stdout    = stdout.decode('ascii')

  if verbose:
    print(stdout)  

  return stdout