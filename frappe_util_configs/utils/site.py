import frappe

@frappe.whitelist(allow_guest=True)
def get_versions():
  from frappe.utils.change_log import get_versions
  return get_versions()