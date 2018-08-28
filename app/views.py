from flask import render_template, flash, redirect, request, url_for
from flask_appbuilder import BaseView, expose, has_access, ModelView, SimpleFormView
from flask_appbuilder.actions import action
from app import db, appbuilder
import datetime
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.models.sqla.filters import FilterStartsWith, FilterEqualFunction, FilterEqual
from flask_babel import lazy_gettext as _
import os
import uuid

from .models import PM_Skillset, PM_User, PM_Supplier, PM_Customer, PM_Project, PM_Rating, PM_Project_QA, PM_Company_Relations, PM_Address, PM_Contact, PM_Banking, PM_Attachment
from .forms import New_PM_Customer, New_PM_Supplier, Add_Skill, Add_Skillt, New_PM_Project

import logging

import pdb

log = logging.getLogger(__name__)


# <___ Custom functions ___>

def skill_update():
    skilldb = db.session.query(PM_Skillset).all()
    skillchoices = [(x, str(x).capitalize()) for x in skilldb]

    return skillchoices

def phone_corr(nr):
    return nr.replace('+','').replace('-','')

# adding data to sql with tablename
def Add_Table(tablename = '', data = []):
    if tablename == 'pm_skillset':
        inquery = PM_Skillset(name=form.skill.data.lower())
        db.session.add(inquery)
    elif tablename == 'pm_user':
        inquery = ''    # n/a yet
        db.session.add(inquery)
    elif tablename == 'pm_supplier':
        inquery = PM_Supplier(skill_grade=skillgrade,
                                 introduction=form.introduction.data, quality_assurance=form.quality_assurance.data,
                                 certification=form.certification.data, goods_service=form.goods_service.data,
                                 goods_list=form.goods_list.data, service_list=form.service_list.data,
                                 company_relations_id=corelqueryid, mailing_address_id=mailaddrqueryid,
                                 bank_id=bankqueryid, attachment_ids="1")
        db.session.add(inquery)
    elif tablename == 'pm_customer':
        inquery = PM_Customer(introduction=form.introduction.data,
                                 company_relations_id=corelqueryid, mailing_address_id=mailaddrqueryid,
                                 bank_id=bankqueryid, attachment_ids="1")
        db.session.add(inquery)
    elif tablename == 'pm_project':
        inquery = PM_Project(skill_grade=skillgrade,
                               name=form.name.data,
                               description=form.description.data,
                               budget=form.budget.data,
                               employees_need=form.employees_need.data,
                               person_days=form.person_days.data,
                               responsible_person=form.responsible_person.data,
                               backup_person=form.backup_person.data,
                               project_planned_start=form.project_planned_start.data,
                               project_planned_end=form.project_planned_end.data,
                               customer_id=1,
                               project_history_ids="3",
                               attachment_ids="1")
        db.session.add(inquery)
    elif tablename == 'pm_rating':
        inquery = ''    # n/a yet
        db.session.add(inquery)
    elif tablename == 'pm_project_qa':
        inquery = ''    # n/a yet
        db.session.add(inquery)
    elif tablename == 'pm_address':
        # need some edit
        inquery = PM_Address(street_address=form.company_address.data,
                                   postal_nr=form.company_postal_nr.data,
                                   city=form.company_city.data, country=form.company_country.data)
    elif tablename == 'pm_contact':
        # need some edit
        inquery = PM_Contact(phone_office=phone_corr(form.company_phone.data),
                                   email=form.company_email.data,
                                   fax=form.company_fax.data, website=form.company_website.data)
        db.session.add(inquery)
    elif tablename == 'pm_attachment':
        filefields = [x for x in request.files.keys()]
        returndict = {}
        # create dict for fields that will be returned with attachment ids
        for i in data:
            returndict[i] = ''
        # pdb.set_trace()
        filenames = []
        unique_filenames = []
        for filefield in filefields:
            for i in request.files.getlist(filefield):
                filenames.append(i.filename)
                unique_filenames.append(uuid.uuid4().hex)
                unique_filename = uuid.uuid4().hex
                i.save(appbuilder.app.config['UPLOAD_FOLDER'] + unique_filename)

                inquery = PM_Attachment(table_id=filefield.split('-')[0],
                                         table_name=request.form[filefield.replace('file-','')],
                                         file=i.filename,
                                         ufilename=unique_filename)

                db.session.add(inquery)
                db.session.commit()
                returndict[filefield.split('-')[0]] += str(inquery.id) + ';'
                # db.session.flush()
                # inquery = ''

        return returndict
    elif tablename == 'pm_banking':
        inquery = PM_Banking(bank_name=form.bank_name.data, branch_name=form.branch_name.data,
                               bank_account_number=form.bank_account_number.data,
                               account_currency=form.account_currency.data,
                               iban=form.iban.data, bic=form.bic.data,
                               routing_bank_details=form.routing_bank_details.data,
                               annual_value_of_total_sales=form.annual_value_of_total_sales.data,
                               annual_value_of_export_sales=form.annual_value_of_export_sales.data,
                               audit_reports=form.audit_reports.data,
                               bankruptcy_legal_action=form.bankruptcy_legal_action.data,
                               branch_address_id=branchaddrqueryid, branch_contact_id=branchcontqueryid,
                               attachment_ids="1")
        db.session.add(inquery)
    elif tablename == 'pm_company_relations':
        inquery = PM_Company_Relations(company_name=form.company_name.data,
                                          parent_company=form.parent_company.data,
                                          subsidiaries=form.subsidiaries.data,
                                          associates=form.associates.data,
                                          international_offices=form.international_offices.data,
                                          type_of_business=type_of_business,
                                          nature_of_business=nature_of_business,
                                          year_of_establishment=form.year_of_establishment.data,
                                          employees=form.employees.data,
                                          licence_number=form.licence_number.data,
                                          vat_tax_id=form.vat_tax_id.data,
                                          working_languages=";".join([x for x in form.working_languages.data]),
                                          company_address_id=compaddrqueryid, company_contact_id=compcontqueryid,
                                          attachment_ids="1"
                                          )
        db.session.add(inquery)
    else:
        inquery = ''

    if inquery == '':
        inquery = "Not adequate data!"
    else:
        db.session.commit()
    return inquery


# <___ ModelViews ___>

class GroupModelView(ModelView):
    datamodel = SQLAInterface(PM_Skillset)
    # related_views = [ContactModelView]


class UserView(ModelView):
    datamodel = SQLAInterface(PM_User)


class SupplierView(ModelView):
    datamodel = SQLAInterface(PM_Supplier)


class CustomerView(ModelView):
    datamodel = SQLAInterface(PM_Customer)


class ProjectView(ModelView):
    datamodel = SQLAInterface(PM_Project, db.session)
    list_title = "Project View"
    # base_filters = [['budget', FilterEqual, '10']]

    label_columns = {'name': 'Project Name', 'customer_id': 'Customer'}
    all_list_columns = ['name', 'description', 'skillset', 'skill_grade', 'budget', 'employees_need', 'person_days', 'responsible_person', 'backup_person', 'project_planned_start'
                    , 'project_planned_end', 'customer_id', 'project_history_ids']

    list_columns = ['name', 'budget', 'customer_id', 'project_planned_start', 'project_planned_end']

    show_fieldsets = [
        (
            'Summary',
            {'fields': all_list_columns}
        ),
        (
            'Personal Info',
            {'fields': ['name'], 'expanded': False}
        ),
    ]

    @action("mulbid", "Bid", "Do you really want to bid all?", "fa-rocket", single=False)
    def mulbid(self, items):
        self.datamodel.delete_all(items)
        self.update_redirect()
        return redirect(self.get_redirect())

class RatingView(ModelView):
    datamodel = SQLAInterface(PM_Rating)


class Project_QAView(ModelView):
    datamodel = SQLAInterface(PM_Project_QA)


# <___ FormViews ___>

class New_PM_CustomerForm(SimpleFormView):
    # route_base = '/new_pm_customerform'
    form = New_PM_Customer
    form_title = 'Customer Registration'
    message = 'The form was submitted'

    def form_post(self, form):
        # post process form
        #
        attachmentiddict = Add_Table('pm_attachment', ['audit_reports', 'compfiles', 'bankfiles'])
        #
        compaddrquery = PM_Address(street_address=form.company_address.data,
                                   postal_nr=form.company_postal_nr.data,
                                   city=form.company_city.data, country=form.company_country.data)
        db.session.add(compaddrquery)
        db.session.commit()
        compaddrqueryid = compaddrquery.id
        #
        compcontquery = PM_Contact(phone_office=phone_corr(form.company_phone.data),
                                   email=form.company_email.data,
                                   fax=form.company_fax.data, website=form.company_website.data)
        db.session.add(compcontquery)
        db.session.commit()
        compcontqueryid = compcontquery.id
        #
        consquery = PM_Contact(phone_office=phone_corr(form.consultant_phone.data),
                                   email=form.consultant_email.data)
        db.session.add(consquery)
        db.session.commit()
        consqueryid = consquery.id
        #

        if form.type_of_business.data == 'other':
            type_of_business = request.form["type_of_business-othertext"]
        else:
            type_of_business = form.type_of_business.data

        if form.nature_of_business.data == 'other':
            nature_of_business = request.form["nature_of_business-othertext"]
        else:
            nature_of_business = form.nature_of_business.data
        corelquery = PM_Company_Relations(company_name=form.company_name.data,
                                          parent_company=form.parent_company.data,
                                          subsidiaries=form.subsidiaries.data,
                                          associates=form.associates.data,
                                          international_offices=form.international_offices.data,
                                          type_of_business=type_of_business,
                                          nature_of_business=nature_of_business,
                                          year_of_establishment=form.year_of_establishment.data,
                                          employees=form.employees.data,
                                          licence_number=form.licence_number.data,
                                          vat_tax_id=form.vat_tax_id.data,
                                          working_languages=";".join([x for x in form.working_languages.data]),
                                          company_address_id=compaddrqueryid, company_contact_id=compcontqueryid,
                                          attachment_ids=attachmentiddict['compfiles']
                                          )
        db.session.add(corelquery)
        db.session.commit()
        corelqueryid = corelquery.id
        #
        mailaddrquery = PM_Address(street_address=form.mailing_address.data,
                                   postal_nr=form.mailing_postal_nr.data,
                                   city=form.mailing_city.data, country=form.mailing_country.data)
        db.session.add(mailaddrquery)
        db.session.commit()
        mailaddrqueryid = mailaddrquery.id
        #
        branchaddrquery = PM_Address(street_address=form.branch_address.data,
                                     postal_nr=form.branch_postal_nr.data,
                                     city=form.branch_city.data, country=form.branch_country.data)
        db.session.add(branchaddrquery)
        db.session.commit()
        branchaddrqueryid = branchaddrquery.id
        #
        branchcontquery = PM_Contact(phone_office=phone_corr(form.branch_phone.data),
                                     fax=form.branch_fax.data, email="n@n.n")
        db.session.add(branchcontquery)
        db.session.commit()
        branchcontqueryid = branchcontquery.id
        #
        if len(attachmentiddict['audit_reports']) == 0:
            audit_reports = 'n'
        else:
            audit_reports = 'y'
        bankquery = PM_Banking(bank_name=form.bank_name.data, branch_name=form.branch_name.data,
                               bank_account_number=form.bank_account_number.data,
                               account_currency=form.account_currency.data,
                               iban=form.iban.data, bic=form.bic.data,
                               routing_bank_details=form.routing_bank_details.data,
                               annual_value_of_total_sales=form.annual_value_of_total_sales.data,
                               annual_value_of_export_sales=form.annual_value_of_export_sales.data,
                               audit_reports=audit_reports,
                               bankruptcy_legal_action=form.bankruptcy_legal_action.data,
                               branch_address_id=branchaddrqueryid, branch_contact_id=branchcontqueryid,
                               attachment_ids=attachmentiddict['bankfiles']+attachmentiddict['audit_reports'])
        db.session.add(bankquery)
        db.session.commit()
        bankqueryid = bankquery.id
        #
        custquery = PM_Customer(introduction=form.introduction.data,
                                 company_relations_id=corelqueryid, mailing_address_id=mailaddrqueryid,
                                 bank_id=bankqueryid, attachment_ids='', consultant_name=form.consultant_name.data,
                                 consultant_id=consqueryid, ignored=form.ignored.data)

        db.session.add(custquery)
        db.session.commit()
        flash(self.message, 'info')
        # return redirect(self.route_base + "/form")
        self.update_redirect()
        self.get_redirect()
        redirect(self.route_base)

def sxor(s1,s2):
    # convert strings to a list of character pair tuples
    # go through each tuple, converting them to ASCII code (ord)
    # perform exclusive or on the ASCII code
    # then convert the result back to ASCII (chr)
    # merge the resulting array of characters as a string
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

def xor_two_str(a,b):
    return ''.join([hex(ord(a[i%len(a)]) ^ ord(b[i%(len(b))]))[2:] for i in range(max(len(a), len(b)))])

class New_PM_SupplierForm(SimpleFormView):
    # route_base = '/new_pm_supplierform'
    form = New_PM_Supplier
    form_title = 'Supplier Registration'
    message = 'The form was submitted'

    def form_get(self, form):
        form.skillset.choices = skill_update()

    def form_post(self, form):
        # post process form
        if form.gdpr.data:
            for keys in form.data.keys():  # CSRF included!!
                original = form[keys].data
                form[keys].data = ''
                for i in str(original):
                    form[keys].data += xor_two_str(i, 't')

        # pdb.set_trace()
        #
        attachmentiddict = Add_Table('pm_attachment', ['audit_reports', 'compfiles', 'servicefiles', 'bankfiles'])
        #
        pdb.set_trace()
        compaddrquery = PM_Address(street_address=form.company_address.data, postal_nr=form.company_postal_nr.data,
                                   city=form.company_city.data, country=form.company_country.data)
        db.session.add(compaddrquery)
        db.session.commit()
        compaddrqueryid = compaddrquery.id
        #
        compcontquery = PM_Contact(phone_office=phone_corr(form.company_phone.data), email=form.company_email.data,
                                   fax=form.company_fax.data, website=form.company_website.data)
        db.session.add(compcontquery)
        db.session.commit()
        compcontqueryid = compcontquery.id
        #
        consquery = PM_Contact(phone_office=phone_corr(form.consultant_phone.data),
                               email=form.consultant_email.data)
        db.session.add(consquery)
        db.session.commit()
        consqueryid = consquery.id
        #
        if form.type_of_business.data == 'other':
            type_of_business = request.form["type_of_business-othertext"]
        else:
            type_of_business = form.type_of_business.data

        if form.nature_of_business.data == 'other':
            nature_of_business = request.form["nature_of_business-othertext"]
        else:
            nature_of_business = form.nature_of_business.data

        corelquery = PM_Company_Relations(company_name=form.company_name.data, parent_company=form.parent_company.data,
                                          subsidiaries=form.subsidiaries.data,
                                          associates=form.associates.data,
                                          international_offices=form.international_offices.data,
                                          type_of_business=type_of_business,
                                          nature_of_business=nature_of_business,
                                          year_of_establishment=form.year_of_establishment.data,
                                          employees=form.employees.data,
                                          licence_number=form.licence_number.data, vat_tax_id=form.vat_tax_id.data,
                                          working_languages=";".join([x for x in form.working_languages.data]),
                                          company_address_id=compaddrqueryid, company_contact_id=compcontqueryid,
                                          attachment_ids=attachmentiddict['compfiles']
                                          )
        db.session.add(corelquery)
        db.session.commit()
        corelqueryid = corelquery.id
        #
        mailaddrquery = PM_Address(street_address=form.mailing_address.data, postal_nr=form.mailing_postal_nr.data,
                                   city=form.mailing_city.data, country=form.mailing_country.data)
        db.session.add(mailaddrquery)
        db.session.commit()
        mailaddrqueryid = mailaddrquery.id
        #
        branchaddrquery = PM_Address(street_address=form.branch_address.data, postal_nr=form.branch_postal_nr.data,
                                     city=form.branch_city.data, country=form.branch_country.data)
        db.session.add(branchaddrquery)
        db.session.commit()
        branchaddrqueryid = branchaddrquery.id
        #
        branchcontquery = PM_Contact(phone_office=phone_corr(form.branch_phone.data), fax=form.branch_fax.data, email="n@n.n")
        db.session.add(branchcontquery)
        db.session.commit()
        branchcontqueryid = branchcontquery.id
        #
        if len(attachmentiddict['audit_reports']) == 0:
            audit_reports = 'n'
        else:
            audit_reports = 'y'
        bankquery = PM_Banking(bank_name=form.bank_name.data, branch_name=form.branch_name.data,
                               bank_account_number=form.bank_account_number.data,
                               account_currency=form.account_currency.data,
                               iban=form.iban.data, bic=form.bic.data,
                               routing_bank_details=form.routing_bank_details.data,
                               annual_value_of_total_sales=form.annual_value_of_total_sales.data,
                               annual_value_of_export_sales=form.annual_value_of_export_sales.data,
                               audit_reports=audit_reports,
                               bankruptcy_legal_action=form.bankruptcy_legal_action.data,
                               branch_address_id=branchaddrqueryid, branch_contact_id=branchcontqueryid,
                               attachment_ids=attachmentiddict['bankfiles']+attachmentiddict['audit_reports'])
        db.session.add(bankquery)
        db.session.commit()
        bankqueryid = bankquery.id
        #
        skillgrade = ";".join([x + '-' + request.form["raskillset-" + x] for x in form.skillset.data])

        supplquery = PM_Supplier(skill_grade=skillgrade,
                                 introduction=form.introduction.data, quality_assurance=form.quality_assurance.data,
                                 certification=form.certification.data, goods_service=form.goods_service.data,
                                 goods_list=form.goods_list.data, service_list=form.service_list.data,
                                 company_relations_id=corelqueryid, mailing_address_id=mailaddrqueryid,
                                 bank_id=bankqueryid, attachment_ids=attachmentiddict['servicefiles'],
                                 consultant_name=form.consultant_name.data,
                                 consultant_id=consqueryid, gdpr=form.gdpr.data)

        db.session.add(supplquery)
        db.session.commit()

        # get skill from skillset query then append supplier's just committed id to supplier's supplkill backref table
        for i in form.skillset.data:
            db.session.query(PM_Skillset).filter(PM_Skillset.name==i).first().supplkill.append(supplquery)

        db.session.commit()

        flash(self.message, 'info')
        # return redirect(self.route_base + "/form")
        self.update_redirect()
        self.get_redirect()
        redirect(self.route_base)


class Add_SkillForm(SimpleFormView):
    # route_base = '/add_skillform'
    form = Add_Skill
    form_title = 'Add Skills'
    message = 'The form was submitted'

    def form_post(self, form):
        # post process form

        inquery = PM_Skillset(name=form.skill.data.lower())
        db.session.add(inquery)

        db.session.commit()
        db.create_all()

        flash(self.message, 'info')
        # return redirect(self.route_base + "/form")
        self.update_redirect()
        self.get_redirect()
        redirect(self.route_base)


class New_PM_ProjectForm(SimpleFormView):
    # route_base = '/new_pm_projectform'
    form = New_PM_Project
    form_title = 'New Project'
    message = 'The form was submitted'

    def form_get(self, form):
        form.skillset.choices = skill_update()

    def form_post(self, form):
        # post process form
        # budget = form.budget.data + ' ' + request.form['budget-select']
        # pdb.set_trace()

        budget = '500000' + ' ' + request.form['budget-select']
        skillgrade = ";".join([x + '-' + request.form["raskillset-" + x] for x in form.skillset.data])
        attachmentiddict = Add_Table('pm_attachment', ['projfiles'])

        projquery = PM_Project(skill_grade=skillgrade,
                                name=form.name.data,
                                type=form.type.data,
                                phases=form.phases.data,
                                description=form.description.data,
                                budget=budget,
                                employees_need=form.employees_need.data,
                                person_days=form.person_days.data,
                                responsible_person=form.responsible_person.data,
                                backup_person=form.backup_person.data,
                                project_planned_start=form.project_planned_start.data,
                                project_planned_end=form.project_planned_end.data,
                                customer_id=1,
                                project_history_ids="3",
                                attachment_ids=attachmentiddict['projfiles'])

        db.session.add(projquery)
        db.session.commit()

        # get skill from skillset query then append supplier's just committed id to supplier's projskill backref table
        for i in form.skillset.data:
            db.session.query(PM_Skillset).filter(PM_Skillset.name == i).first().projskill.append(projquery)

        db.session.commit()

        flash(self.message, 'info')
        # return redirect(self.route_base + "/form")
        self.update_redirect()
        self.get_redirect()
        redirect(self.route_base)


# <___ Testing ___>

class Add_SkilltForm(SimpleFormView):
    # route_base = '/add_skilltform'
    form = Add_Skillt
    form_title = 'Add Skillst'
    message = 'The form was submitted'

    def form_post(self, form):
        pdb.set_trace()
        self.update_redirect()
        self.get_redirect()
        redirect(self.route_base)
    # def form_post(self, form):

        # for attr in dir(self):
        #     flash("obj.%s = %r" % (attr, getattr(self, attr)), 'info')
        #
        # pdb.set_trace()
        # self.update_redirect()
        # return redirect(self.route_base + "/form")


class MyView(BaseView):

    default_view = 'method1'

    @expose('/method1/')
    @has_access
    def method1(self):
            # do something with param1
            # and return to previous page or index
        return 'Hello'

    @expose('/method2/<string:param1>')
    @has_access
    def method2(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        return param1

    @expose('/method3/<string:param1>')
    @has_access
    def method3(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbyes %s' % (param1)
        return self.render_template('method3.html',
                               param1=param1)

    @expose('/send_email/<string:param1>')
    def send_email(self, param1):
        """
            Method for sending the registration Email to the user
        """
        try:
            from flask_mail import Mail, Message
        except:
            log.error("Install Flask-Mail to use User registration")
            return False
        mail = Mail(self.appbuilder.get_app)
        msg = Message()
        msg.subject = "TEST VERIFICATION MAIL" + str(datetime.datetime.now())
        #url = url_for('.activation', _external=True, activation_hash=register_user.registration_hash)
        url = "asdddd"
        msg.html = self.render_template("mail.html",
                                        url=url,
                                        #username=register_user.username,
                                        username="pnagy",
                                        #first_name=register_user.first_name,
                                        first_name="Péter",
                                        #last_name=register_user.last_name)
                                        last_name="Nagy")
        msg.recipients = ["garzooka22@gmail.com", "rkanyo@gmail.com", "tkanyo@gmail.com"]
        #try:
        mail.send(msg)
        #except Exception as e:
        #    log.error("Send email exception: {0}".format(str(e)))
        #    return False
        return msg.html

    def send_email_view(self, param1):
        """
            Method for sending the registration Email to the user
        """
        try:
            from flask_mail import Mail, Message
        except:
            log.error("Install Flask-Mail to use User registration")
            return False
        mail = Mail(self.appbuilder.get_app)
        msg = Message()
        msg.subject = str(datetime.datetime.now())
        #url = url_for('.activation', _external=True, activation_hash=register_user.registration_hash)
        url = "asdddd"
        msg.html = self.render_template("mail.html",
                                        url=url,
                                        #username=register_user.username,
                                        username="asd",
                                        #first_name=register_user.first_name,
                                        first_name="asd",
                                        #last_name=register_user.last_name)
                                        last_name="asd")
        msg.recipients = ["garzooka22@gmail.com"]
        #try:
        #mail.send(msg)
        #except Exception as e:
        #    log.error("Send email exception: {0}".format(str(e)))
        #    return False
        return msg.html


db.create_all()
#form
appbuilder.add_view(New_PM_CustomerForm, "Customer", icon="fa-group", label=_('Customer'), category="Registration", category_icon="fa-cogs")
appbuilder.add_view(New_PM_SupplierForm, "Supplier", icon="fa-group", label=_('Supplier'), category="Registration", category_icon="fa-cogs")
appbuilder.add_view(New_PM_ProjectForm, "Project", icon="fa-group", label=_('Project'), category="Registration", category_icon="fa-cogs")
appbuilder.add_view(Add_SkillForm, "Skill", icon="fa-group", label=_('Skill'), category="Registration", category_icon="fa-cogs")
appbuilder.add_view(Add_SkilltForm, "Skillst", icon="fa-group", label=_('Skillst'), category="Registration", category_icon="fa-cogs")
#models
appbuilder.add_view(GroupModelView, "List Groups", icon="fa-folder-open-o", category="Administration", category_icon='fa-envelope')
appbuilder.add_view(UserView, "List Users", icon="fa-folder-open-o", category="Administration", category_icon='fa-envelope')
appbuilder.add_view(SupplierView, "List Suppliers", icon="fa-folder-open-o", category="Administration", category_icon='fa-envelope')
appbuilder.add_view(CustomerView, "List Customer", icon="fa-folder-open-o", category="Administration", category_icon='fa-envelope')
appbuilder.add_view(ProjectView, "List Project", icon="fa-folder-open-o", category="Administration", category_icon='fa-envelope')
appbuilder.add_view(RatingView, "List Rating", icon="fa-folder-open-o", category="Administration", category_icon='fa-envelope')
appbuilder.add_view(Project_QAView, "List ProjectQA", icon="fa-folder-open-o", category="Administration", category_icon='fa-envelope')

# appbuilder.add_view(ContactModelView, "List Contacts", icon="fa-envelope", category="Administration")
appbuilder.add_separator("Administration")

appbuilder.add_view(MyView(), "Method1", category='My View')
#appbuilder.add_view(MyView(), "Method2", href='/myview/method2/jonh', category='My View')
# Use add link instead there is no need to create MyView twice.
appbuilder.add_link("Method2", href='/myview/method2/jonh', category='My View')
appbuilder.add_link("Method3", href='/myview/method3/jonh', category='My View')
appbuilder.add_link("send_email", href='/myview/send_email/jonh', category='My View')
appbuilder.add_link("send_email_view", href='/myview/send_email/jonh', category='My View')


"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404


# attachment id req -> can be null