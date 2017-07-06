# -*- coding: utf-8 -*-
{
        "name" : "NSTDA-APP :: BOOKSTORE",
        "version" : "2.0",
        "author" : 'Thawatchai C.',
        "category" : 'NSTDA Apps',
        "description": """ Bookstore ระบบเบิกจ่ายสินค้า/ของที่ระลึก  """,
        'website': 'http://www.nstda.or.th',
        'depends': ['base', 'mail', 'email_template', 'nstdaperm', 'nstdamas'],
        'data': [
                'static/views/nstda_bst.xml',
                'security/module_data.xml',    
                'security/nstda_bst_security.xml',
                'security/ir.model.access.csv',
                'wizard/nstda_bst_note_view.xml',
                'view/nstda_bst_hbill_view.xml',
                'view/nstda_bst_dbill_view.xml',
                'view/nstda_bst_stock_view.xml',
                'view/nstda_bst_sequence.xml',
                'view/nstda_bst_discount_view.xml',
                'view/nstda_bst_report_view.xml',
                'view/nstda_bst_mail_template_view.xml',
                'view/nstda_bst_bill_report_view.xml',
                'view/nstda_bst_pick_report_view.xml',
                'view/nstda_bst_view.xml',
                'view/nstda_bst_menu_view.xml',

        ],
        'qweb': ['static/views/base.xml'],
        'demo': [],
        'installable': True,
        'images': [],
}
