# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ejemplo_1(models.Model):
#     _name = 'ejemplo_1.ejemplo_1'
#     _description = 'ejemplo_1.ejemplo_1'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

