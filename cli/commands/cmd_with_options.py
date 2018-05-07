# import subprocess
import click


@click.command()
@click.option('--skip-init/--no-skip-init',
              default=True, help='skip __init__.py files?')
@click.argument('path', default='yourapp')
def cli(skip_init, path):
    """
    INFO: see cli/commands/__init__.py for more info
    creating app custom command

    creates and run a cli command with options
    to run a command automatically use the python
    subprocess module see example below

    :param skip_init: an example that runs a command that skips init files
    :param path: command line argument when running the command
    :return: Outputs text based on the value skip init
    """
    if skip_init:
        click.echo('The command will skip all init files')
        # cmd = 'flask app.py'
        # return subprocess.call(cmd, shell=True) runs the command on cli
        return

    click.echo('The command will not skip all init files')
