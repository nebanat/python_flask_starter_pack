import click
# import subprocess


@click.command()
@click.argument('name', default='aaron')
def cli(name):
    """
     INFO: see cli/commands/__init__.py for more info
     creating app custom command

     This gives an example of a cli command with
     argument.
     To run a command automatically use the python
     subprocess module see example below

     if you are using docker in your run the command

    :param name: command argument
    :return: prints a message to the console
    """
    click.echo('This is a simple click command with path params {}'.format(name))

    # cmd = 'flask app.py'
    # return subprocess.call(cmd, shell=True) runs the command on cli


