
from odoo import models, api, fields
from odoo.exceptions import ValidationError

class HostelCategory(models.Model):
    _name = 'hostel.category'
    _parent_store = True
    _parent_name = 'parent_id'

    
    name = fields.Char('Hostel category')
    
    parent_id = fields.Many2one(
        'hostel.category',
        string = 'Parent Category',
        ondelete = 'restrict',
        index = True,
    )
    parent_path = fields.Char(index= True, unaccent=False)
    child_ids = fields.One2many(
        'hostel.category',
        'parent_id',
        string = 'Child Categories',
    )

    @api.constrains('parent_id')
    def _check_heirarchy(self):
        if not self._check_recursion():
            raise models.ValidationError(
                'Error! You cannot create recursive categories.'
            )
        
    