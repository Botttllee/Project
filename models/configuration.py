from odoo import models, fields, api

class Configuration(models.Model):
    _name = 'hotel.configuration'
    _description = 'Hotel Configuration'
    name = fields.Char(string="configuration")






