from odoo import models, fields, api

class Member(models.Model):
    _inherit = 'res.partner'

#     # Tambahkan field tambahan untuk model Member
#     # membership_date = fields.Date(string='Membership Date')
#     # membership_level = fields.Selection([('silver', 'Silver'), ('gold', 'Gold'), ('platinum', 'Platinum')], string='Membership Level')

#     # Relasi dengan model transaksi booking hotel
    booking_id = fields.One2many('book.hotel', 'customer_id', string='Hotel Bookings')


