# -*- coding: utf-8 -*-
from odoo import http

# class IstockData(http.Controller):
#     @http.route('/istock_data/istock_data/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/istock_data/istock_data/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('istock_data.listing', {
#             'root': '/istock_data/istock_data',
#             'objects': http.request.env['istock_data.istock_data'].search([]),
#         })

#     @http.route('/istock_data/istock_data/objects/<model("istock_data.istock_data"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('istock_data.object', {
#             'object': obj
#         })