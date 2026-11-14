from odoo import fields, models

class ExpenseClaim(models.Model):
    _name = "brocode.expense"
    _description = "Klaim Biaya dan Reimbursement"
    _inherit = ["mail.thread"]

    name = fields.Char(string="Nomor Klaim", required=True, default='New')
    requested_by = fields.Many2one("res.users", string="Pemohon", default=lambda self: self.env.user)
    transaction_date = fields.Date(string="Tanggal Transaksi", required=True)
    
    category = fields.Selection([
        ('operasional', 'Operasional Kasir'),
        ('konsumsi', 'Konsumsi Rapat'),
        ('perbaikan', 'Perbaikan Sarana'),
        ('transportasi', 'Transportasi & Logistik')
    ], string="Kategori Biaya", required=True)
    
    amount = fields.Float(string="Nominal Pengajuan (Rp)", required=True, tracking=True)
    receipt_image = fields.Binary(string="Bukti Nota (Foto)")
    
    claim_status = fields.Selection([
        ('ExpenseDraft', 'Draft'),
        ('Submitted', 'Submitted'),
        ('UnderAudit', 'Under Audit'),
        ('RevisionNeeded', 'Revision Needed'),
        ('Approved', 'Approved'),
        ('Reimbursed', 'Reimbursed')
    ], string="Status Klaim", default='ExpenseDraft', tracking=True)
    
    revision_notes = fields.Text(string="Catatan Revisi Finance")