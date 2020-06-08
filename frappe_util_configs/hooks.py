# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "frappe_util_configs"
app_title = "Frappe Util Configs"
app_publisher = "Leam Technology Systems"
app_description = "Useful frappe features for your random purposes"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@leam.ae"
app_license = "MIT"

on_session_creation = "frappe_util_configs.on_session_creation"

override_whitelisted_methods = {
  # This is done so that we can know frappe_util_configs was installed, with no renovation_core
  "renovation_core.utils.site.get_versions": "frappe_util_configs.utils.site.get_versions"
}

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/frappe_util_configs/css/frappe_util_configs.css"
# app_include_js = "/assets/frappe_util_configs/js/frappe_util_configs.js"

# include js, css files in header of web template
# web_include_css = "/assets/frappe_util_configs/css/frappe_util_configs.css"
# web_include_js = "/assets/frappe_util_configs/js/frappe_util_configs.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "frappe_util_configs.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "frappe_util_configs.install.before_install"
# after_install = "frappe_util_configs.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "frappe_util_configs.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"frappe_util_configs.tasks.all"
# 	],
# 	"daily": [
# 		"frappe_util_configs.tasks.daily"
# 	],
# 	"hourly": [
# 		"frappe_util_configs.tasks.hourly"
# 	],
# 	"weekly": [
# 		"frappe_util_configs.tasks.weekly"
# 	]
# 	"monthly": [
# 		"frappe_util_configs.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "frappe_util_configs.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "frappe_util_configs.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "frappe_util_configs.task.get_dashboard_data"
# }

