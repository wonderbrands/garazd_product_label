# Copyright © 2018 Garazd Creation (<https://garazd.biz>)
# @author: Yurii Razumovskyi (<support@garazd.biz>)
# @author: Iryna Razumovska (<support@garazd.biz>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

from odoo import api, fields, models


class PrintProductLabel(models.TransientModel):
    _inherit = "print.product.label"

    @api.model
    def _get_products(self):
        res = super(PrintProductLabel, self)._get_products()
        if self._context.get('active_model') == 'purchase.order':
            purchases = self.env['purchase.order'].browse(
                self._context.get('default_purchase_ids'))
            for order in purchases:
                for line in order.order_line.filtered(
                        lambda l: l.display_type is False):
                    label = self.env['print.product.label.line'].create({
                        'product_id': line.product_id.id,
                        'qty': line.product_qty,
                        'qty_initial': line.product_qty,
                    })
                    res.append(label.id)
        return res

    label_ids = fields.One2many(default=_get_products)
