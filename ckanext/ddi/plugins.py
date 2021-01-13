# -*- coding: utf-8 -*-

import logging

import ckan.plugins as plugins
import ckan.plugins.toolkit as tk

from ckanext.ddi import blueprints
log = logging.getLogger(__name__)


class DdiImport(plugins.SingletonPlugin):
    plugins.implements(plugins.IBlueprint)
    plugins.implements(plugins.IConfigurer)

    def get_blueprint(self):
        return blueprints.ddi_import_blueprint

    def update_config(self, config):
        tk.add_template_directory(config, 'templates')
        tk.add_resource('fanstatic', 'ddi')
