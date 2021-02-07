from cx_Freeze import setup, Executable

setup(name = 'Royal Bank',
      version = '0.1',
      description = 'Banking System',
      executables = [Executable("bank.py")])