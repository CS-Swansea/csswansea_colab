import os, tempfile, shutil
import csswansea_colab
from csswansea_colab.utils import execute_command

def configure(verbose=False, execute_tests=True):
  print()
  print('installing swi-prolog')
  execute_command(f'add-apt-repository -y ppa:swi-prolog/stable', verbose=verbose)
  execute_command(f'apt-get update', verbose=verbose)
  execute_command(f'apt-get install -y swi-prolog', verbose=verbose)

  print()
  print('swi-prolog')
  execute_command(f'swipl --version', verbose=True)

  if execute_tests:
    test(verbose=verbose)

def test(verbose=False):
  print()
  print('executing tests')
    
  tmpdir = tempfile.mkdtemp()
  
  with open(f'{tmpdir}/HelloWorld.pl', 'w') as f:
    f.write("""hello :- format('Hello World.~n').\n""")

  result = execute_command(f'swipl -q -l {tmpdir}/HelloWorld.pl -t hello.', verbose=verbose)

  if 'Hello World.' not in result:
    raise Exception('swi-prolog HelloWorld test did not produce the expected output...')
  else:
    print('Tests passed.')

  shutil.rmtree(tmpdir)