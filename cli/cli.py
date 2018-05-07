import os

import click

cmd_folder = os.path.join(os.path.dirname(__file__), 'commands')
cmd_prefix = 'cmd_'


class CLI(click.MultiCommand):
    def list_commands(self, ctx):
        """

        :param ctx: Click context
        :return: Sorted list of all CLI command
        """
        commands = []

        for filename in os.listdir(cmd_folder):
            if filename.endswith('.py') and filename.startswith(cmd_prefix):
                commands.append(filename[4:-3])

        commands.sort()

        return commands

    def get_command(self, ctx, cmd_name):
        """
        Get a specific command by looking up the module

        :param ctx: Click context
        :param cmd_name: Command name
        :return: Module cli function
        """
        ns = {}

        filename = os.path.join(cmd_folder, cmd_prefix + cmd_name + '.py')

        with open(filename) as file:
            code = compile(file.read(), filename, 'exec')
            eval(code, ns, ns)

        return ns['cli']


@click.command(cls=CLI)
def cli():
    """commands to help manage your project"""
    pass
