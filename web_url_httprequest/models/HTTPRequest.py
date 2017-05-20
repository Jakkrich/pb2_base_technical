# -*- coding: utf-8 -*-
from openerp import models
from openerp import http
from openerp.http import request
import urlparse


class WebUrlHTTPRequest(models.Model):
    _name = 'web.url.httprequest'
    _auto = False

    def get(self, name):
        url = request.httprequest.environ['HTTP_REFERER']
        get = dict(urlparse.parse_qsl(urlparse.urlsplit(url).query))
        if name in get:
            return get[name]
        return False
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
