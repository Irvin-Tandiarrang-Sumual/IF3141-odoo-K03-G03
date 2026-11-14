from odoo import fields, models, api

class Reservation(models.Model):
    _name = "brocode.reservation"
    _description = "Data Reservasi Layanan"
    _inherit = ["mail.thread"]

    name = fields.Char(string="Kode Booking", required=True, copy=False, readonly=True, default='New')
    customer_id = fields.Many2one("res.partner", string="Pelanggan", required=True, tracking=True)
    barber_id = fields.Many2one("res.users", string="Kapster", required=True)
    branch_id = fields.Many2one("res.company", string="Cabang", required=True, default=lambda self: self.env.company)
    
    service_name = fields.Char(string="Nama Layanan", required=True)
    service_time = fields.Datetime(string="Jadwal Layanan", required=True, tracking=True)
    total_price = fields.Float(string="Total Harga (Rp)", tracking=True)
    
    reservation_status = fields.Selection([
        ('SelectingSlot', 'Selecting Slot'),
        ('Locked', 'Locked'),
        ('Confirmed', 'Confirmed'),
        ('Rescheduled', 'Rescheduled'),
        ('Cancelled', 'Cancelled'),
        ('NoShow', 'No Show'),
        ('InService', 'In Service'),
        ('Completed', 'Completed')
    ], string="Status Reservasi", default='SelectingSlot', tracking=True)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('brocode.reservation') or 'BC-BOOKING'
        return super(Reservation, self).create(vals)