__author__ = 'Ross Thompson'

import ckan.plugins as plugins
from pylons import config as c

WET_URL_OPTION = 'wet_theme.url'
WET_URL_DEFAULT = 'http://localhost/'

class FgpPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)

    # ITemlateHelpers
    def  get_helpers(self):
        return {'fgp_url': self.fgp_url}

    #IConfigurer
    def update_config(self, config):
        plugins.toolkit.add_template_directory(config, 'templates')
        plugins.toolkit.add_public_directory(config, 'ramp')

    # Helper functions
    def fgp_url(self):
        return str(c.get(WET_URL_OPTION, WET_URL_DEFAULT))

    #IRoutes
    def before_map(self, map):
        map.connect(
            'ramp_view', '/ramp',
            controller='ckanext.fgp.controller:FgpController',
            action='ramp_view',
        )
        return map