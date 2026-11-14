from odoo import fields, models

class StoreReadiness(models.Model):
    _name = "brocode.store_readiness"
    _description = "Checklist Kesiapan Toko"
    _inherit = ["mail.thread"]

    branch_id = fields.Many2one("res.company", string="Cabang", required=True, default=lambda self: self.env.company)
    staff_user_id = fields.Many2one("res.users", string="Staf Bertugas", default=lambda self: self.env.user)
    record_date = fields.Date(string="Tanggal", default=fields.Date.context_today, required=True)
    
    opening_time = fields.Float(string="Waktu Buka (Jam)", tracking=True)
    closing_time = fields.Float(string="Waktu Tutup (Jam)", tracking=True)
    
    opening_status = fields.Selection([
        ('PreOpening', 'Pre-Opening'),
        ('StoreOpen', 'Store Open'),
        ('Operational', 'Operational')
    ], string="Status Pagi", default='PreOpening', tracking=True)
    
    closing_status = fields.Selection([
        ('Closing', 'Closing'),
        ('ClosedOnTime', 'Closed On Time'),
        ('ClosedOvertime', 'Closed Overtime')
    ], string="Status Malam", tracking=True)

    checklist_cleanliness = fields.Boolean(string="Area Pangkas Bersih")
    checklist_sterilization = fields.Boolean(string="Alat Steril")
    checklist_cash_register = fields.Boolean(string="Modal Kasir Siap")
    
    overtime_notes = fields.Text(string="Catatan Keterlambatan Tutup")