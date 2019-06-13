# -*- coding: utf-8 -*-
from odoo import http

# class ProjectHicto(http.Controller):
#     @http.route('/project_hicto/project_hicto/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_hicto/project_hicto/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_hicto.listing', {
#             'root': '/project_hicto/project_hicto',
#             'objects': http.request.env['project_hicto.project_hicto'].search([]),
#         })

#     @http.route('/project_hicto/project_hicto/objects/<model("project_hicto.project_hicto"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_hicto.object', {
#             'object': obj
#         })