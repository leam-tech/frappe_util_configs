import click

@click.group(name="frappe-util-configs")
def setup_utils():
  pass

@click.command("jwt-init")
def setup():
  from frappe_util_configs.install.benchconfig import update_config
  update_config()

@click.command("nginx")
@click.option('--force', help='Yes to regeneration of nginx config file', default=False, is_flag=True)
def setup_nginx(force=False):
  from frappe_util_configs.install.bench.nginx import setup_nginx as _setup_nginx
  _setup_nginx(force=force)

setup_utils.add_command(setup)
setup_utils.add_command(setup_nginx)
commands = [setup_utils]