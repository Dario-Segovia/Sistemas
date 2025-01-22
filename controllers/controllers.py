# -*- coding: utf-8 -*-
# from odoo import http


# class Ejemplo1(http.Controller):
#     @http.route('/ejemplo_1/ejemplo_1', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ejemplo_1/ejemplo_1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ejemplo_1.listing', {
#             'root': '/ejemplo_1/ejemplo_1',
#             'objects': http.request.env['ejemplo_1.ejemplo_1'].search([]),
#         })

#     @http.route('/ejemplo_1/ejemplo_1/objects/<model("ejemplo_1.ejemplo_1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ejemplo_1.object', {
#             'object': obj
#         })

