import subprocess

def execute_command(cmd, verbose=False):
  
  print('++', cmd)

  prc       = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  stdout, _ = prc.communicate()
  stdout    = stdout.decode('ascii')

  if verbose:
    print(stdout)  

  return stdout

def execute_interactive_command(cmd, icmds, verbose=False):

  print('++', cmd)
  prc = subprocess.Popen(cmd.split(), stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  
  for icmd in icmds:
    print(f'++ {icmd.strip()}')
    
    prc.stdin.write(f'{icmd.strip()}\n'.encode('ascii'))
    prc.stdin.flush()
  
  stdout, _ = prc.communicate()
  stdout    = stdout.decode('ascii')

  if verbose:
    print(stdout) 

  return stdout