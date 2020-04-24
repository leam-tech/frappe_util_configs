from jinja2 import Environment, PackageLoader

def get_jinja_env():
  return Environment(loader=PackageLoader("frappe_util_configs.install"))
