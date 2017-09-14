# -*- coding: utf-8 -*-
from openerp import tools, models, fields, api, exceptions, _
from pickle import TRUE
from _ctypes import sizeof
from docutils.parsers import null
from pychart.tick_mark import Null
from dateutil import parser

from datetime import datetime, timedelta
from datetime import datetime
from dateutil import relativedelta as rdelta

import re
import time

from datetime import date
from dateutil.relativedelta import relativedelta
from openerp.exceptions import except_orm, Warning, RedirectWarning
from openerp.http import request
import locale


####################################################################################################


class nstda_bst_mail_alert(models.Model):
    
    _name = 'nstda.bst.mail.alert'
    _table = 'nstda_bst_mail_alert'
    _auto = True
    _inherit = ['mail.thread','ir.needaction_mixin']


    def sendmail_alert(self, cr, uid, ids, context=None):
        env_refs = self.pool.get('nstda.bst.hbill').browse(cr, uid, ids)
        email_template_obj = self.pool.get('email.template')
        email_template_name = 'nstda_bst_mail_alert'
        template_ids = email_template_obj.search(cr, uid, [('model_id.model','=','nstda.bst.hbill'), ('name','=',email_template_name)], context=context)
        if template_ids:
            values = email_template_obj.generate_email(cr, uid, template_ids[0], env_refs.id, context=context)
            
            values['body_html'] = values['body_html'].replace("{to}", env_refs.empid.emp_email)
            values['body_html'] = values['body_html'].replace("{dear}", env_refs.empname)
            values['body_html'] = values['body_html'].replace("{docno}", env_refs.docno)
            values['body_html'] = values['body_html'].replace("{amount}", '{:20,.2f}'.format(env_refs.amount_after_discount))
            
            mail_mail_obj = self.pool.get('mail.mail')
            uid = 1
            msg_id = mail_mail_obj.create(cr, uid, values, context=context)
            if msg_id:
                mail_mail_obj.send(cr, uid, [msg_id], context=context)
                self.write(cr, uid, env_refs.id, {'is_mail_approved':True}, context=context)
        return True
    
    
    def sendmail_approve(self, cr, uid, ids, context=None):
        env_refs = self.pool.get('nstda.bst.hbill').browse(cr, uid, ids)
        email_template_obj = self.pool.get('email.template')
        email_template_name = 'nstda_bst_mail_approval'
        template_ids = email_template_obj.search(cr, uid, [('model_id.model','=','nstda.bst.hbill'), ('name','=',email_template_name)], context=context)
        if template_ids:
            values = email_template_obj.generate_email(cr, uid, template_ids[0], env_refs.id, context=context)
            
            url_rec = str(request.httprequest.host_url) + ':8069/web#id=' + str(env_refs.id) + '&model=nstda.bst.hbill'
            
            values['body_html'] = values['body_html'].replace("{to}", env_refs.boss_emp_id.emp_email)
            values['body_html'] = values['body_html'].replace("{dear}", env_refs.bossname)
            values['body_html'] = values['body_html'].replace("{docby}", env_refs.empname)
            values['body_html'] = values['body_html'].replace("{docno}", env_refs.docno)
            values['body_html'] = values['body_html'].replace("{amount}", '{:20,.2f}'.format(env_refs.amount_after_discount))
            values['body_html'] = values['body_html'].replace("{bst_url}", url_rec)
            
            mail_mail_obj = self.pool.get('mail.mail')
            uid = 1
            msg_id = mail_mail_obj.create(cr, uid, values, context=context)
            if msg_id:
                mail_mail_obj.send(cr, uid, [msg_id], context=context)
                self.write(cr, uid, env_refs.id, {'is_mail_approved':True}, context=context)
        return True
    
    
    def sendmail_success(self, cr, uid, ids, context=None):
        env_refs = self.pool.get('nstda.bst.hbill').browse(cr, uid, ids)
        email_template_obj = self.pool.get('email.template')
        email_template_name = 'nstda_bst_mail_success'
        template_ids = email_template_obj.search(cr, uid, [('model_id.model','=','nstda.bst.hbill'), ('name','=',email_template_name)], context=context)
        if template_ids:
            values = email_template_obj.generate_email(cr, uid, template_ids[0], env_refs.id, context=context)
            
            values['body_html'] = values['body_html'].replace("{to}", env_refs.empid.emp_email)
            values['body_html'] = values['body_html'].replace("{dear}", env_refs.empname)
            values['body_html'] = values['body_html'].replace("{docno}", env_refs.docno)
            values['body_html'] = values['body_html'].replace("{amount}", '{:20,.2f}'.format(env_refs.amount_after_discount))
            values['body_html'] = values['body_html'].replace("{pdate}", env_refs.post_date)
            values['body_html'] = values['body_html'].replace("{receive}", env_refs.receive_emp_name)
            
            mail_mail_obj = self.pool.get('mail.mail')
            uid = 1
            msg_id = mail_mail_obj.create(cr, uid, values, context=context)
            if msg_id:
                mail_mail_obj.send(cr, uid, [msg_id], context=context)
                self.write(cr, uid, env_refs.id, {'is_mail_approved':True}, context=context)
        return True
    
    