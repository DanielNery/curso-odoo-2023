from odoo import models, fields

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    
    
    meu_primeiro_modelo_id = fields.Many2one('meu.primeiro.modelo', "Referência para nosso primeiro modelo")
    
    meu_primeiro_modelo_campo_integer_related = fields.Integer(related='meu_primeiro_modelo_id.meu_primeiro_campo_inteiro')
    