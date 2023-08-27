import base64

from io import BytesIO
from xlsxwriter import Workbook

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

    tax_ids = fields.Many2many(
        comodel_name ="account.tax",
        relation="account_tax_meu_primeiro_modelo_rel",
        column1="meu_primeiro_modelo_id",
        column2="account_tax_id",
        string="Impostos"
    )

    start_date = fields.Datetime(string="Data Inicial", required=True)
    end_date = fields.Datetime(string="Data Final", required=True)
    allday = fields.Boolean('Dia Inteiro', default=False)

    def generate_excel_report(self):
        
        # Criar um arquivo xlsx em memória
        output = BytesIO()
        workbook = Workbook(output)
        worksheet = workbook.add_worksheet()
        
        # Personalizar o seu relatório
        # colocar cor, registros, editar tamanhos
        worksheet.set_column("A:A", 20)
        
        # Add a bold format to use to highlight cells.
        bold = workbook.add_format({"bold": True})

        # Write some simple text.
        worksheet.write("A1", "Hello")

        # Text with formatting.
        worksheet.write("A2", "World", bold)

        # Write some numbers, with row/column notation.
        worksheet.write(2, 0, 123)
        worksheet.write(3, 0, 123.456)
        
        workbook.close()
        
        # Obter os dados do arquivo em formato base64
        xlsx_data = output.getvalue()
        output.close()
        
        # Criar um anexo no Odoo com o arquivo xlsx
        attachment = self.env["ir.attachment"].create({
            "name": "report.xlsx",
            "type": 'binary',
            "datas": base64.b64encode(xlsx_data),
            "res_model": self._name,
            "res_id": self.id
        })
        
        # Retornar a ção para abrir o anexo recém criado
        return {
            "type": "ir.actions.act_url",
            "url": f"/web/content/{attachment.id}?download=true",
            "target": 'self'
        }
        
        
        
        

class MeuPrimeiroModuloLinha(models.Model):
    _name = 'meu.primeiro.modelo.linha'
    
    nome = fields.Char(string="Nome")
    
    primeiro_modelo_id = fields.Many2one('meu.primeiro.modelo', string="Primeiro Modelo")
    