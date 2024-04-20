{
    'name': 'Hospital Management System',
    'author': 'Yura',
    'application': True,
    'sequence': -100,
    'summary': 'Odoo 15 development',
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/om_hospital_menus.xml',
        'views/patient_views.xml',
        'views/female_patient_views.xml',
        'views/appointment_views.xml',
        'views/doctor_views.xml',
        # 'views/website_form.xml',
    ]
}
