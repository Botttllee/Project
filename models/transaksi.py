from odoo import models, fields, api

class HotelAppointment(models.Model):
    _name = 'book.hotel'
    _description = 'Booking a hotel in this app'

    STATUS_SELECTION = [
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('finish', 'Finish'),
        ('cancel', 'Cancel'),
    ]

    name = fields.Many2one('kamar.hotel', string='nama kamar')
    # tipe_kamar = fields.Char(related = "name.tipe_kamar.name")
    # fasilitas_kamar = fields.Many2many('fasilitas.hotel', string='fasilitas kamar', related = "name.fasilitas_kamar")
    # fasilitas_kamar = fields.Many2many('fasilitas.hotel', string='Fasilitas Kamar', related='name.tipe_kamar.fasilitas_kamar')
    customer_id   = fields.Many2one('res.partner', string='Customer')
    checkin_date  = fields.Date(string='Check-In Date')
    checkout_date = fields.Date(string='Check-Out Date')
    # harga_kamar = fields.Float(string='harga kamar', related = 'tipe_kamar.harga_kamar', store=True)
    status = fields.Selection(STATUS_SELECTION, string='Status', default='draft')
    duration = fields.Integer(string='Duration', compute='_compute_duration', store=True)
    note = fields.Text(string='Note')



    @api.depends('checkin_date', 'checkout_date')
    def _compute_duration(self):
        for appointment in self:
            if appointment.checkin_date and appointment.checkout_date:
                duration = (appointment.checkout_date - appointment.checkin_date).days
                appointment.duration = duration if duration >= 0 else 0
            else:
                appointment.duration = 0
