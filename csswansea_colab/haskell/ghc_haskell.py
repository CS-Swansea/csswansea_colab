import os, tempfile, shutil
import csswansea_colab
from csswansea_colab.utils import execute_command

def configure(verbose=False, execute_tests=True):
  print()
  print('installing glasgow haskell compiler')
  execute_command(f'apt-get update', verbose=verbose)
  execute_command(f'apt-get install -y ghc ghc-prof ghc-doc', verbose=verbose)

  print()
  print('ghc version')
  execute_command(f'ghc --version', verbose=True)

  if execute_tests:
    test(verbose=verbose)

def test(verbose=False):
  print()
  print('executing tests')
    
  tmpdir = tempfile.mkdtemp()
  
  with open(f'{tmpdir}/HelloWorld.hs', 'w') as f:
    f.write("""main = putStrLn "Hello World."\n""")

  execute_command(f'ghc {tmpdir}/HelloWorld.hs -o {tmpdir}/HelloWorld', verbose=verbose)
  result = execute_command(f'{tmpdir}/HelloWorld', verbose=verbose)

  if 'Hello World.' not in result:
    raise Exception('glasgow haskell compiler HelloWorld test did not produce the expected output...')
  else:
    print('Tests passed.')

  shutil.rmtree(tmpdir)