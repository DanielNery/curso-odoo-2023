from odoo import models, fields

class MeuPrimeiroModulo(models.Model):
    _name = 'meu.primeiro.modelo'
    _description = "meu primeiro modelo criado no Odoo"
    
    meu_primeiro_campo_inteiro = fields.Integer(
        string="Número Inteiro", 
        default=0,
        help="Exemplo"
    )
