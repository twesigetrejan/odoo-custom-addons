from odoo import fields, models

from odoo import api, fields, models

class Hostel(models.Model):
    _name = 'hostel.hostel'
    _description = 'Information about a hostel'
    _order = 'id desc, name'
    _rec_name = 'hostel_code'

    name = fields.Char(string='Hostel Name', required=True)
    hostel_code = fields.Char(string='Code', required=True, help='Unique code for the hostel')
    street = fields.Char(string='Street')
    street2 = fields.Char(string='Street 2')
    zip = fields.Char('Zip', change_default=True, help='Postal code of the hostel location')
    city = fields.Char(string='City')
    state_id = fields.Many2one('res.country.state', string='State')
    country_id = fields.Many2one('res.country', string='Country')
    phone = fields.Char(string='Phone', required=True, help='Contact number for the hostel')
    mobile = fields.Char(string='Mobile', required=True)
    email = fields.Char(string='Email')
    display_name = fields.Char(compute='_compute_display_name', store=True)

    @api.depends('hostel_code')
    def _compute_display_name(self):
        for record in self:
            name = record.name
            if record.hostel_code:
                name = f'{name} ({record.hostel_code})'
            record.display_name = name

