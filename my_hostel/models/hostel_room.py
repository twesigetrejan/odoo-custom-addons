from odoo import models, fields, api

class HostelRoom(models.Model):
    _name = 'hostel.room'
    _description = 'Information about a hostel room'
    _order = 'id desc, room_code'
    _rec_name = 'room_code'

    room_code = fields.Char(string='Room code', required=True, help='Unique code for the room')
    hostel_id = fields.Many2one('hostel.hostel', string='Hostel', required=True, help='Hostel to which the room belongs')
    floor_number = fields.Integer(string='Floor Number')
    capacity = fields.Integer(string='Capacity', help='Number of occupants the room can hold')
    rent_amount = fields.Monetary(string='Rent amount', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency', required=True)
    active = fields.Boolean(string='Active', default=True)
    notes = fields.Text(string='Notes')

    student_ids = fields.One2many(
        'hostel.student', 'room_id', string='Students',
        help='Students assigned to this room'
    )

    hostel_amenities_ids = fields.Many2many(
        "hostel.amenities",
        "hostel_room_amenities_rel",
        "room_id",
        "amenity_id",
        string="Hostel amenities",
        domain="[('active', '=', True)]",
        help="Amenities available in this room"
    )







# from odoo import models, fields, api


# class HostelRoom(models.Model):
#     _name = 'hostel.room'
#     _description = 'Information about a hostel room'
#     _order = 'id desc, room_code'
#     _rec_name = 'room_code'

#     room_code = fields.Char(string='Room code', required=True, help='Unique code for the room')
#     hostel_id = fields.Many2one('hostel.hostel', string='Hostel', required=True)
#     floor_number = fields.Integer(string='Floor Number')
#     capacity = fields.Integer(string='Capacity', help='Number of occupants the room can hold')
#     rent_amount = fields.Monetary(string='Rent amount', currency_field='currency_id')
#     currency_id = fields.Many2one('res.currency', string='Currency', required=True)
#     active = fields.Boolean(string='Active', default=True)
#     notes = fields.Text(string='Notes')
#     hostel_id = fields.Many2one('hostel.hostel', string='Hostel', help='Hostel to which the room belongs')
#     student_ids = fields.One2many('hostel.student', 'room_id', string='Students', help='Students assigned to this room')
#     hostel_amenities_ids = fields.Many2many("hostel.amenities","hostel_room_amenities_rel", "room_id", "amenity_id", string="Hostel amenities", domain="[('active', '=', True)]", help="Amenities available in this room")
