# -*- coding: utf-8 -*-
# from odoo import http


# class hotel_booking_order(http.Controller):
#     @http.route('/hotel_booking_order/hotel_booking_order', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hotel_booking_order/hotel_booking_order/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hotel_booking_order.listing', {
#             'root': '/hotel_booking_order/hotel_booking_order',
#             'objects': http.request.env['hotel_booking_order.hotel_booking_order'].search([]),
#         })

#     @http.route('/hotel_booking_order/hotel_booking_order/objects/<model("hotel_booking_order.hotel_booking_order"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hotel_booking_order.object', {
#             'object': obj
#         })
