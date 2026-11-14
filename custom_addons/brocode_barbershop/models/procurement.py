from odoo import fields, models

class ProcurementPO(models.Model):
    _name = "brocode.procurement"
    _description = "Pengadaan Purchase Order"
    _inherit = ["mail.thread"]

    name = fields.Char(string="Nomor PO", required=True, copy=False, readonly=True, default='New')
    branch_id = fields.Many2one("res.company", string="Cabang Pemohon", required=True)
    requested_by = fields.Many2one("res.users", string="Pemohon", default=lambda self: self.env.user)
    submission_date = fields.Date(string="Tanggal Pengajuan", default=fields.Date.context_today)
    
    item_name = fields.Char(string="Nama Barang", required=True)
    quantity = fields.Integer(string="Kuantitas", required=True, default=1)
    estimated_price = fields.Float(string="Estimasi Harga Satuan (Rp)")
    total_budget = fields.Float(string="Total Anggaran", compute="_compute_total")
    
    po_status = fields.Selection([
        ('DraftRequest', 'Draft Request'),
        ('Submitted', 'Submitted'),
        ('UnderReview', 'Under Review'),
        ('Rejected', 'Rejected'),
        ('Approved', 'Approved'),
        ('Ordered', 'Ordered'),
        ('Received', 'Received')
    ], string="Status PO", default='DraftRequest', tracking=True)

    rejection_reason = fields.Text(string="Alasan Penolakan")

    def _compute_total(self):
        for record in self:
            record.total_budget = record.quantity * record.estimated_price