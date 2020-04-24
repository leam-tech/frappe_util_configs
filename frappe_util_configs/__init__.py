# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import frappe

__version__ = '0.0.1'


def on_session_creation(login_manager):
  from .auth import make_jwt
  if frappe.form_dict.get('use_jwt'):
    frappe.local.response['token'] = make_jwt(
        login_manager.user, frappe.flags.get('jwt_expire_on'))
    frappe.wait_for_attach()
    frappe.flags.jwt_clear_cookies = True
