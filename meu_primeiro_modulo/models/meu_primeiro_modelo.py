from odoo import models, fields

class MeuPrimeiroModulo(models.Model):
    _name = 'meu.primeiro.modelo'
    _description = "meu primeiro modelo criado no Odoo"
    
    # default=True - Valor padrão do campo
    # readonly=True - Se é um campo para somente leitura
    # required=True - Define se o campo é obrigatório
    # store=True - Define se o campo é obrigatóriamente salvo no banco de dados, os campos por padrão
    #       São store True, eles só se tornam store false quando tem o comnpute
    # compute="função_para_executar_tarefa" - Quando você deseja que o campo seja computado 
    # help="string" - Para ajudar o usuário saber para que serve o campo
    
    
    meu_primeiro_campo_inteiro = fields.Integer(
        string="Número Inteiro", 
        default=0,
        help="Exemplo"
    )

    primeiro_campo_boolean = fields.Boolean(
        string="Madeira",
        help="Campo para definir se a matéria prima do produto é de madeira ou não"
    )
    
    # Exemplo => 1.000.000.000,00
    campo_float = fields.Float(
        string="Campo Float",
        digits=(10, 2)
    )
    
    name = fields.Char(
        string="Nome"
    )
    
    descricao = fields.Text(
        string="Descrição"
    )
    
    tipo = fields.Selection([
        ('ativo', 'Ativo'), 
        ('inativo', 'Inativo'),
    ], string="Tipo")
    
    sale_order_id = fields.Many2one('sale.order', string="Pedido de Vendas")
    # ondelete
    # cascade
    # set null
    # restrict
    # no action
    
    primeiro_modelo_ids = fields.One2many('meu.primeiro.modelo.linha', 'primeiro_modelo_id', string="Primeiro Modelo Linhas")


class MeuPrimeiroModuloLinha(models.Model):
    _name = 'meu.primeiro.modelo.linha'
    
    nome = fields.Char(string="Nome")
    
    primeiro_modelo_id = fields.Many2one('meu.primeiro.modelo', string="Primeiro Modelo")
    