import click
from zipfile import *
import os
from progressbar import *

#a dictionary which sets certain strings as keys and some numeric constants as their values
compressions = {'ZIP_STORED': ZIP_STORED, 'ZIP_LZMA': ZIP_LZMA, 'ZIP_DEFLATED': ZIP_DEFLATED, 'ZIP_BZIP2': ZIP_BZIP2}

#by default, Click only allows the long form --help for help
#by using this, we are going to define the short form -h as well
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

#making the function below this an entry point for the command
@click.command(context_settings = CONTEXT_SETTINGS)

#defining an option, 'directory'
#this represents the directory where the archive should be saved
#it defaults to the current working directory
@click.option('--directory', '-d', type = click.Path(exists=True, dir_okay=True, writable=True), default = '.', help = 'The directory where the archive should be saved.')

#defining an option, 'comp'
#this represents the compression that should be used to create the file
#defaults to ZIP_STORED
@click.option('--comp', '-c', type = click.Choice(['ZIP_STORED', 'ZIP_DEFLATED', 'ZIP_BZIP2', 'ZIP_LZMA']), default = 'ZIP_STORED', help = 'The compression that should be used. It defaults to ZIP_STORED.')

#defining an option, 'name'
#this represents the name that should be used for the archive
#defaults to 'my-zipfile.zip'
@click.option('--name', '-n', default = 'my-zipfile.zip', help = "The name that should be given to the archive. Defaults to 'my-zipfile.zip'.")


@click.option('--verbose', '-v', is_flag = True, default = False, help = 'Show a progress bar and more information about the operation.')

#defining an argument, 'files'
#this will collect all the files that need to be archived
#it accepts an unlimited number of files by setting nargs = -1
#the passed file names will be stored in a tuple: (file1.txt, file2.py, file3.exe, ...)
#it requires at least one file name, defined by setting required = True
@click.argument('files', type = click.Path(exists=True), nargs = -1, default = None, required = True)

def zipFile(directory, comp, name, files, verbose):
    '''
    This command creates an archive in the cwd, unless specified otherwise, of the files passed as argument.
    It can accept any number of files.
    '''

    fileCount = len(files)

    #getting the current directory
    cwd = os.getcwd()

    #changing to the directory passed by user
    #this is to save the new archive in this directory
    os.chdir(directory)

    #creating a ZipFile() object
    #it will have the name passed by user: name
    #will be in write mode: 'w'
    #will use the compression passed by user: compressions[comp]
    with ZipFile(name, 'w', compressions[comp]) as zip:

        if verbose:
            with ProgressBar(widgets=[Timer(), Bar(), Percentage(), " ", AbsoluteETA(),], max_value= 100) as bar:
                i = 100/fileCount
                for file in files:
                    zip.write(file)
                    bar.update(i)
                    i += 100/fileCount

            print(f'Zipped {fileCount} files to {directory if directory != "." else "cwd"} under name, {name}.')

        else:
            for file in files:
                zip.write(file)
    #changing back to the original directory
    os.chdir(cwd)
    print('Finished!')

