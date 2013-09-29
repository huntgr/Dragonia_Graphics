from cx_Freeze import setup, Executable

includefiles = ['background_.ogg','cave_dragonia.png','mage_dragonia.png','sun.png','cleric_dragonia.png','cyclops.png','desert.png','dragon.png','dragonia!.png','gameover.wav','gameover_.png','garg_dragonia_small.png','ogre.png','player.png','realcave.png','snake.png','warlock_dragonia.png','warrior_dragonia.png','water.png']
includes = ['pygame.py','random.py','sys.py','time.py','copy.py','classes.py']
excludes = []
packages = []

setup(
    name = 'Dragonia',
    version = '1.0.1',
    description = '',
    author = 'Hunt Grayodn',
    author_email = 'huntgraydon@gmail.com',
    options = {'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles}}, 
    executables = [Executable('dragonia_graphics.py')]
)
