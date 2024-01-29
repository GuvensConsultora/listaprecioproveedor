# -*- coding: utf-8 -*-
# from odoo import http


# class Listpriceproveedor(http.Controller):
#     @http.route('/listpriceproveedor/listpriceproveedor', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/listpriceproveedor/listpriceproveedor/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('listpriceproveedor.listing', {
#             'root': '/listpriceproveedor/listpriceproveedor',
#             'objects': http.request.env['listpriceproveedor.listpriceproveedor'].search([]),
#         })

#     @http.route('/listpriceproveedor/listpriceproveedor/objects/<model("listpriceproveedor.listpriceproveedor"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('listpriceproveedor.object', {
#             'object': obj
#         })
