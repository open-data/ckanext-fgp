__author__ = 'thomros'

from ckan.lib.base import (BaseController, render)

class FgpController(BaseController):
    def ramp_view(self):
        return render('ramp.html')