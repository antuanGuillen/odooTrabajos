# from odoo import http


# class RpgDemo(http.Controller):
#     @http.route('/rpg_demo/rpg_demo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rpg_demo/rpg_demo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rpg_demo.listing', {
#             'root': '/rpg_demo/rpg_demo',
#             'objects': http.request.env['rpg_demo.rpg_demo'].search([]),
#         })

#     @http.route('/rpg_demo/rpg_demo/objects/<model("rpg_demo.rpg_demo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rpg_demo.object', {
#             'object': obj
#         })

