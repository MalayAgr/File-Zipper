import click
from zipfile import *
import os
from progressbar import *

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings = CONTEXT_SETTINGS)

@click.option('--directory', '-d', type = click.Path(exists = True, dir_okay = True, writable = True), default = '.', help = 'The directory where the files should be extracted')

@click.option('--verbose', '-v', is_flag = True, default = False, help = 'Gives more information about the operation.')

@click.argument('archive', type = click.Path(exists = True), required = True)

@click.argument('files', type = click.STRING, nargs = -1)

def unzipFile(directory, archive, files, verbose):
    '''
    This script extracts the files from a pre-existing archive.

    Arguments -\n
        ARCHIVE - The archive that needs to be extracted.\n
        FILES - These are any specific files that need to be extracted. If you do not supply this, all the files will be extracted.
    '''

    with ZipFile(archive, 'r') as zipFile:
        cwd = os.getcwd()
        os.chdir(directory)

        if files:
            try:
                if verbose:
                    with ProgressBar(widgets = [Timer(), Bar(), Percentage(), " ", AbsoluteETA(), ],
                                     max_value = 100) as bar:
                        fileCount = len(files)
                        i = 100/fileCount
                        for file in files:
                            zipFile.extract(file)
                            bar.update(i)
                            i += 100/fileCount

                        print(f"Extracted {fileCount} file(s) to {'cwd' if directory == '.' else directory}.")
                else:
                    for file in files:
                        zipFile.extract(file)
            except:
                raise click.BadParameter('One or more files were not present in the archive.')
        else:
            zipFile.extractall()
            if verbose:
                print(f"Extracted {len(zipFile.filelist)} file(s) to {'cwd' if directory == '.' else directory}.")

    print('Finished!')
    os.chdir(cwd)
