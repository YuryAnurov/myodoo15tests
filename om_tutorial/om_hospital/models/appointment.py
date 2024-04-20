from odoo import api, fields, models, _


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = 'mail.thread'
    _description = "Hospital Appointment"
    _rec_name = 'ref'

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    appointment_time = fields.Datetime(string="Appointment Time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today)
    gender = fields.Selection(related='patient_id.gender', readonly=False)
    ref = fields.Char(string="Reference", help="Reference of the patient from patient record")
    prescription = fields.Html(string='Prescription')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], default='draft', string="Status", required=True)

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def action_test(self):
        print("Button Clicked!!!!!")
        return {
            'effect': {
                'fadeout': 'slow',  # можно убрать, тогда будет висеть пока не щелкнешь
                'message': 'Click was extremle successfull',
                'type': 'rainbow_man',
            }
        }
