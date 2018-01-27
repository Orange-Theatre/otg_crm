# -*- coding: utf-8 -*-

from openerp import models, fields, api, exceptions

import logging
_logger = logging.getLogger(__name__)

class Lead(models.Model):
	_inherit = 'crm.lead'

	# New fields
	contact_id = fields.Many2one('res.partner', 'Contact')

	@api.onchange('partner_id')
	def _onchange_partner_id(self):
		if self.partner_id.id != self.contact_id.parent_id.id:
			self.contact_id = False

	@api.constrains('partner_id', 'contact_id')
	def _check_contact(self):
		if self.partner_id.id != self.contact_id.parent_id.id:
			raise exceptions.ValidationError"You must choose a contact that's associated with the customer account")

