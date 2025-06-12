from odoo import models, fields, api

class HostelStudent(models.Model):
    _name = 'hostel.student'
    _description = 'Information about a hostel student'
    _order = 'id desc, name'
    _rec_name = 'student_code'

    student_code = fields.Char(string='Student Code', help='Unique code for the student')
    name = fields.Char(string='Student name', required=True, help='Full name of the student')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    active = fields.Boolean(string='Active', default=True, help='Activate/Deactivate student record')
    room_id = fields.Many2one('hostel.room', string='Room', required=True, help='Room assigned to the student')




# from odoo import models, fields, api

# class HostelStudent(models.Model):
#     _name = 'hostel.student'
#     _description = 'Information about a hostel student'
#     _order = 'id desc, name'
#     _rec_name = 'student_code'

#     name = fields.Char(string='Student name', required=True, help='Full name of the student')
#     gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
#     active = fields.Boolean(string='Active', default=True, help='Activate/Deactivate student record')
#     room_id = fields.Many2one('hostel.room', string='Room', required=True, help='Room assigned to the student')