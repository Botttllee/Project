from odoo import models, fields, api

class KamarHotel(models.Model):
    _name = 'kamar.hotel'
    _description = 'Informasi mengenai kamar hotel'

    description = fields.Text()
    name = fields.Integer(string="Nama Kamar")
    panjang_kamar = fields.Float()
    lebar_kamar = fields.Float()
    luas_kamar = fields.Float(compute='_compute_area')
    status_kamar = fields.Boolean()
    harga_kamar = fields.Integer()
    fasilitas_kamar = fields.Integer()
    transaksi_booking = fields.Integer()

    # configuration_id = fields.Many2one('hotel.configuration', string='Configuration')
    # fasilitas_kamar_ids = fields.One2many('fasilitas.hotel', 'kamar_id', string='Fasilitas Kamar')

    # tipe_kamar_id = fields.Many2one('tipe.kamar', string='Tipe Kamar', ondelete='set null')

    @api.onchange('panjang_kamar', 'lebar_kamar')
    def _compute_area(self):
        for rec in self:
            rec.luas_kamar = rec.panjang_kamar * rec.lebar_kamar






# class hotel(models.Model):
#     _name = 'kamar.hotel'
#     _description = 'berikut adalah informasi mengenai kamar hotel'

#     name = fields.Integer(string="Nama Kamar")
#     lantai = fields.Integer()
#     panjang_kamar = fields.Float()
#     lebar_kamar = fields.Float()
#     luas_kamar = fields.Float(compute='_compute_area')
#     status_kamar = fields.Boolean()
#     harga_kamar = fields.Integer()
#     fasilitas_kamar = fields.Integer()
#     transaksi_booking = fields.Integer()
#     description = fields.Text()

#     @api.onchange('panjang_kamar','lebar_kamar')
#     def _compute_area(self):
#         for rec in self:
#             rec.luas_kamar = rec.panjang_kamar * rec.lebar_kamar

            
