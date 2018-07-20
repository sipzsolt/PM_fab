from flask import render_template, flash, redirect, request, url_for
from flask_appbuilder import BaseView, expose, has_access, ModelView, SimpleFormView
from app import db, appbuilder
import datetime
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.models.sqla.filters import FilterStartsWith, FilterEqualFunction, FilterEqual
from flask_babel import lazy_gettext as _
import os
import uuid

from .models import PM_Skillset, PM_User, PM_Supplier, PM_Customer, PM_Project, PM_Rating, PM_Project_QA, PM_Company_Relations, PM_Address, PM_Contact, PM_Banking, PM_Skilltest, PM_Skillset2, PM_Attachment
from .forms import New_PM_Customer, New_PM_Supplier, Add_Skill, Add_Skillt, New_PM_Project

import logging

import pdb

log = logging.getLogger(__name__)


# <___ Custom functions ___>

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
                                 introduction=form.company.data["introduction"], quality_assurance=form.services.data["quality_assurance"],
                                 certification=form.services.data["certification"], goods_service=form.services.data["goods_service"],
                                 goods_list=form.services.data["goods_list"], service_list=form.services.data["service_list"],
                                 company_relations_id=corelqueryid, mailing_address_id=mailaddrqueryid,
                                 bank_id=bankqueryid, attachment_ids="1")
        db.session.add(inquery)
    elif tablename == 'pm_customer':
        inquery = PM_Customer(introduction=form.company.data["introduction"],
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
        inquery = PM_Address(street_address=form.company.data["company_address"],
                                   postal_nr=form.company.data["company_postal_nr"],
                                   city=form.company.data["company_city"], country=form.company.data["company_country"])
    elif tablename == 'pm_contact':
        # need some edit
        inquery = PM_Contact(phone_office=form.company.data["company_phone"],
                                   email=form.company.data["company_email"],
                                   fax=form.company.data["company_fax"], website=form.company.data["company_website"])
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
        inquery = PM_Banking(bank_name=form.banking.data["bank_name"], branch_name=form.banking.data["branch_name"],
                               bank_account_number=form.banking.data["bank_account_number"],
                               account_currency=form.banking.data["account_currency"],
                               iban=form.banking.data["iban"], bic=form.banking.data["bic"],
                               routing_bank_details=form.banking.data["routing_bank_details"],
                               annual_value_of_total_sales=form.banking.data["annual_value_of_total_sales"],
                               annual_value_of_export_sales=form.banking.data["annual_value_of_export_sales"],
                               audit_reports=form.banking.data["audit_reports"],
                               bankruptcy_legal_action=form.banking.data["bankruptcy_legal_action"],
                               branch_address_id=branchaddrqueryid, branch_contact_id=branchcontqueryid,
                               attachment_ids="1")
        db.session.add(inquery)
    elif tablename == 'pm_company_relations':
        inquery = PM_Company_Relations(company_name=form.company.data["company_name"],
                                          parent_company=form.company.data["parent_company"],
                                          subsidiaries=form.company.data["subsidiaries"],
                                          associates=form.company.data["associates"],
                                          international_offices=form.company.data["international_offices"],
                                          type_of_business=type_of_business,
                                          nature_of_business=nature_of_business,
                                          year_of_establishment=form.company.data["year_of_establishment"],
                                          employees=form.company.data["employees"],
                                          licence_number=form.company.data["licence_number"],
                                          vat_tax_id=form.company.data["vat_tax_id"],
                                          working_languages=";".join([x for x in form.company.data["working_languages"]]),
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

class PM_SkilltestView(ModelView):
    datamodel = SQLAInterface(PM_Skilltest)
    # list_columns = ['name', 'budget', 'customer_id', 'project_planned_start', 'project_planned_end']
    # pdb.set_trace()
    # related_views = [ContactModelView]


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
    # datamodel.query(filters=projfill)

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


class RatingView(ModelView):
    datamodel = SQLAInterface(PM_Rating)


class Project_QAView(ModelView):
    datamodel = SQLAInterface(PM_Project_QA)


# <___ FormViews ___>

class New_PM_CustomerForm(SimpleFormView):
    form = New_PM_Customer
    form_title = 'Customer Registration'
    message = 'The form was submitted'

    def form_get(self, form):
        # form.field[0].data = 'This was prefilled'
        True

    def form_post(self, form):
        # post process form
        #
        attachmentiddict = Add_Table('pm_attachment', ['company', 'banking'])
        #
        compaddrquery = PM_Address(street_address=form.company.data["company_address"],
                                   postal_nr=form.company.data["company_postal_nr"],
                                   city=form.company.data["company_city"], country=form.company.data["company_country"])
        db.session.add(compaddrquery)
        db.session.commit()
        compaddrqueryid = compaddrquery.id
        #
        compcontquery = PM_Contact(phone_office=form.company.data["company_phone"],
                                   email=form.company.data["company_email"],
                                   fax=form.company.data["company_fax"], website=form.company.data["company_website"])
        db.session.add(compcontquery)
        db.session.commit()
        compcontqueryid = compcontquery.id
        #

        if form.company.data["type_of_business"] == 'other':
            type_of_business = request.form["company-type_of_business-othertext"]
        else:
            type_of_business = form.company.data["type_of_business"]

        if form.company.data["nature_of_business"] == 'other':
            nature_of_business = request.form["company-nature_of_business-othertext"]
        else:
            nature_of_business = form.company.data["nature_of_business"]
        corelquery = PM_Company_Relations(company_name=form.company.data["company_name"],
                                          parent_company=form.company.data["parent_company"],
                                          subsidiaries=form.company.data["subsidiaries"],
                                          associates=form.company.data["associates"],
                                          international_offices=form.company.data["international_offices"],
                                          type_of_business=type_of_business,
                                          nature_of_business=nature_of_business,
                                          year_of_establishment=form.company.data["year_of_establishment"],
                                          employees=form.company.data["employees"],
                                          licence_number=form.company.data["licence_number"],
                                          vat_tax_id=form.company.data["vat_tax_id"],
                                          working_languages=";".join(
                                              [x for x in form.company.data["working_languages"]]),
                                          company_address_id=compaddrqueryid, company_contact_id=compcontqueryid,
                                          attachment_ids=attachmentiddict['company']
                                          )
        db.session.add(corelquery)
        db.session.commit()
        corelqueryid = corelquery.id
        #
        mailaddrquery = PM_Address(street_address=form.mailing.data["mailing_address"],
                                   postal_nr=form.mailing.data["mailing_postal_nr"],
                                   city=form.mailing.data["mailing_city"], country=form.mailing.data["mailing_country"])
        db.session.add(mailaddrquery)
        db.session.commit()
        mailaddrqueryid = mailaddrquery.id
        #
        branchaddrquery = PM_Address(street_address=form.banking.data["branch_address"],
                                     postal_nr=form.banking.data["branch_postal_nr"],
                                     city=form.banking.data["branch_city"], country=form.banking.data["branch_country"])
        db.session.add(branchaddrquery)
        db.session.commit()
        branchaddrqueryid = branchaddrquery.id
        #
        branchcontquery = PM_Contact(phone_office=form.banking.data["branch_phone"],
                                     fax=form.banking.data["branch_fax"], email="n@n.n")
        db.session.add(branchcontquery)
        db.session.commit()
        branchcontqueryid = branchcontquery.id
        #
        bankquery = PM_Banking(bank_name=form.banking.data["bank_name"], branch_name=form.banking.data["branch_name"],
                               bank_account_number=form.banking.data["bank_account_number"],
                               account_currency=form.banking.data["account_currency"],
                               iban=form.banking.data["iban"], bic=form.banking.data["bic"],
                               routing_bank_details=form.banking.data["routing_bank_details"],
                               annual_value_of_total_sales=form.banking.data["annual_value_of_total_sales"],
                               annual_value_of_export_sales=form.banking.data["annual_value_of_export_sales"],
                               audit_reports=form.banking.data["audit_reports"],
                               bankruptcy_legal_action=form.banking.data["bankruptcy_legal_action"],
                               branch_address_id=branchaddrqueryid, branch_contact_id=branchcontqueryid,
                               attachment_ids=attachmentiddict['banking'])
        db.session.add(bankquery)
        db.session.commit()
        bankqueryid = bankquery.id
        #
        custquery = PM_Customer(introduction=form.company.data["introduction"],
                                 company_relations_id=corelqueryid, mailing_address_id=mailaddrqueryid,
                                 bank_id=bankqueryid, attachment_ids=attachmentiddict['company']+attachmentiddict['banking'])

        db.session.add(custquery)
        db.session.commit()
        flash(self.message, 'info')


class New_PM_SupplierForm(SimpleFormView):
    form = New_PM_Supplier
    form_title = 'Supplier Registration'
    message = 'The form was submitted'

    def form_get(self, form):
        # flash(self.formdata('company_address', form.company), 'info')
        True

    def form_post(self, form):
        # post process form
        #
        attachmentiddict = Add_Table('pm_attachment', ['company', 'banking'])
        #
        compaddrquery = PM_Address(street_address=form.company.data["company_address"], postal_nr=form.company.data["company_postal_nr"],
                                   city=form.company.data["company_city"], country=form.company.data["company_country"])
        db.session.add(compaddrquery)
        db.session.commit()
        compaddrqueryid = compaddrquery.id
        #
        compcontquery = PM_Contact(phone_office=form.company.data["company_phone"], email=form.company.data["company_email"],
                                   fax=form.company.data["company_fax"], website=form.company.data["company_website"])
        db.session.add(compcontquery)
        db.session.commit()
        compcontqueryid = compcontquery.id
        #
        if form.company.data["type_of_business"] == 'other':
            type_of_business = request.form["company-type_of_business-othertext"]
        else:
            type_of_business = form.company.data["type_of_business"]

        if form.company.data["nature_of_business"] == 'other':
            nature_of_business = request.form["company-nature_of_business-othertext"]
        else:
            nature_of_business = form.company.data["nature_of_business"]

        corelquery = PM_Company_Relations(company_name=form.company.data["company_name"], parent_company=form.company.data["parent_company"],
                                          subsidiaries=form.company.data["subsidiaries"],
                                          associates=form.company.data["associates"],
                                          international_offices=form.company.data["international_offices"],
                                          type_of_business=type_of_business,
                                          nature_of_business=nature_of_business,
                                          year_of_establishment=form.company.data["year_of_establishment"],
                                          employees=form.company.data["employees"],
                                          licence_number=form.company.data["licence_number"], vat_tax_id=form.company.data["vat_tax_id"],
                                          working_languages=";".join([x for x in form.company.data["working_languages"]]),
                                          company_address_id=compaddrqueryid, company_contact_id=compcontqueryid,
                                          attachment_ids=attachmentiddict['company']
                                          )
        db.session.add(corelquery)
        db.session.commit()
        corelqueryid = corelquery.id
        #
        mailaddrquery = PM_Address(street_address=form.mailing.data["mailing_address"], postal_nr=form.mailing.data["mailing_postal_nr"],
                                   city=form.mailing.data["mailing_city"], country=form.mailing.data["mailing_country"])
        db.session.add(mailaddrquery)
        db.session.commit()
        mailaddrqueryid = mailaddrquery.id
        #
        branchaddrquery = PM_Address(street_address=form.banking.data["branch_address"], postal_nr=form.banking.data["branch_postal_nr"],
                                     city=form.banking.data["branch_city"], country=form.banking.data["branch_country"])
        db.session.add(branchaddrquery)
        db.session.commit()
        branchaddrqueryid = branchaddrquery.id
        #
        branchcontquery = PM_Contact(phone_office=form.banking.data["branch_phone"], fax=form.banking.data["branch_fax"], email="n@n.n")
        db.session.add(branchcontquery)
        db.session.commit()
        branchcontqueryid = branchcontquery.id
        #
        bankquery = PM_Banking(bank_name=form.banking.data["bank_name"], branch_name=form.banking.data["branch_name"],
                               bank_account_number=form.banking.data["bank_account_number"],
                               account_currency=form.banking.data["account_currency"],
                               iban=form.banking.data["iban"], bic=form.banking.data["bic"],
                               routing_bank_details=form.banking.data["routing_bank_details"],
                               annual_value_of_total_sales=form.banking.data["annual_value_of_total_sales"],
                               annual_value_of_export_sales=form.banking.data["annual_value_of_export_sales"],
                               audit_reports=form.banking.data["audit_reports"],
                               bankruptcy_legal_action=form.banking.data["bankruptcy_legal_action"],
                               branch_address_id=branchaddrqueryid, branch_contact_id=branchcontqueryid,
                               attachment_ids=attachmentiddict['banking'])
        db.session.add(bankquery)
        db.session.commit()
        bankqueryid = bankquery.id
        #
        skillgrade = ";".join([x + '-' + request.form["raskillset-skillset-" + x] for x in form.skillset.data['skillset']])

        supplquery = PM_Supplier(skill_grade=skillgrade,
                                 introduction=form.company.data["introduction"], quality_assurance=form.services.data["quality_assurance"],
                                 certification=form.services.data["certification"], goods_service=form.services.data["goods_service"],
                                 goods_list=form.services.data["goods_list"], service_list=form.services.data["service_list"],
                                 company_relations_id=corelqueryid, mailing_address_id=mailaddrqueryid,
                                 bank_id=bankqueryid, attachment_ids=attachmentiddict['company']+attachmentiddict['banking'])

        db.session.add(supplquery)
        db.session.commit()

        # get skill from skillset query then append supplier's just committed id to supplier's supplkill backref table
        for i in form.skillset.data['skillset']:
            db.session.query(PM_Skillset).filter(PM_Skillset.name==i).first().supplkill.append(supplquery)

        db.session.commit()

        flash(self.message, 'info')


class Add_SkillForm(SimpleFormView):
    form = Add_Skill
    form_title = 'Add Skills'
    message = 'The form was submitted'

    def form_get(self, form):
        # form.skill.data = dir(form)
        True

    def form_post(self, form):
        # post process form

        inquery = PM_Skillset(name=form.skill.data.lower())
        db.session.add(inquery)

        db.session.commit()
        db.create_all()
        pdb.set_trace()

        flash(self.message, 'info')


class New_PM_ProjectForm(SimpleFormView):
    form = New_PM_Project
    form_title = 'New Project'
    message = 'The form was submitted'

    def form_get(self, form):
        True

    def form_post(self, form):
        # post process form
        skillgrade = ";".join([x + '-' + request.form["raskillset-skillset-" + x] for x in form.skillset.data['skillset']])
        projquery = PM_Project(skill_grade=skillgrade,
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

        db.session.add(projquery)
        db.session.commit()

        # get skill from skillset query then append supplier's just committed id to supplier's projskill backref table
        for i in form.skillset.data['skillset']:
            db.session.query(PM_Skillset).filter(PM_Skillset.name == i).first().projskill.append(projquery)

        db.session.commit()

        flash(self.message, 'info')


# <___ Testing ___>

class Add_SkilltForm(SimpleFormView):
    form = Add_Skillt
    form_title = 'Add Skillst'
    message = 'The form was submitted'

    def upload_file(self):
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))

    def form_get(self, form):
        # flash(form.data, 'info')
        True

    def form_post(self, form):
        # post process form
        # for attr in dir(request):
        #     flash("obj.%s = %r" % (attr, getattr(request, attr)), 'info')
        # skillgrade = ";".join([request.form["raskillset-" + x] for x in form.skillset.data])
        #
        # filenames = []
        # unique_filenames = []
        # for i in request.files.getlist('files-file-0'):
        #     filenames.append(i.filename)
        #     unique_filenames.append(uuid.uuid4().hex)
        #     unique_filename = uuid.uuid4().hex
        #     i.save(self.appbuilder.app.config['UPLOAD_FOLDER'] + unique_filename)
        #
        # cntr = 0
        # for i in filenames:
        #     attquery = PM_Attachment(table_id='test',
        #                              table_name=request.form['files-0'],
        #                              file=i,
        #                              ufilename=unique_filenames[cntr])
        #     cntr += 1
        #
        #     db.session.add(attquery)
        # db.session.commit()

        # Add_Table('pm_attachment', ['com', 'com2'])

        # flash(Add_Table('pm_attachment', ['com', 'com2']), 'info')
        flash(self.message, 'info')
        # pdb.set_trace()


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
appbuilder.add_view(New_PM_CustomerForm, "Customer Registration", icon="fa-group", label=_('Customer Registration'), category="My Forms", category_icon="fa-cogs")
appbuilder.add_view(New_PM_SupplierForm, "Supplier Registration", icon="fa-group", label=_('Supplier Registration'), category="My Forms", category_icon="fa-cogs")
appbuilder.add_view(New_PM_ProjectForm, "New Project", icon="fa-group", label=_('New Project'), category="My Forms", category_icon="fa-cogs")
appbuilder.add_view(Add_SkillForm, "Add Skills", icon="fa-group", label=_('Add Skills'), category="My Forms", category_icon="fa-cogs")
appbuilder.add_view(Add_SkilltForm, "Add Skillst", icon="fa-group", label=_('Add Skillst'), category="My Forms", category_icon="fa-cogs")
#models
appbuilder.add_view(GroupModelView, "List Groups", icon="fa-folder-open-o", category="Contacts", category_icon='fa-envelope')
appbuilder.add_view(UserView, "List Users", icon="fa-folder-open-o", category="Contacts", category_icon='fa-envelope')
appbuilder.add_view(SupplierView, "List Suppliers", icon="fa-folder-open-o", category="Contacts", category_icon='fa-envelope')
appbuilder.add_view(CustomerView, "List Customer", icon="fa-folder-open-o", category="Contacts", category_icon='fa-envelope')
appbuilder.add_view(ProjectView, "List Project", icon="fa-folder-open-o", category="Contacts", category_icon='fa-envelope')
appbuilder.add_view(RatingView, "List Rating", icon="fa-folder-open-o", category="Contacts", category_icon='fa-envelope')
appbuilder.add_view(Project_QAView, "List ProjectQA", icon="fa-folder-open-o", category="Contacts", category_icon='fa-envelope')

appbuilder.add_view(PM_SkilltestView, "List PM_SkilltestView", icon="fa-folder-open-o", category="Contacts", category_icon='fa-envelope')
# appbuilder.add_view(ContactModelView, "List Contacts", icon="fa-envelope", category="Contacts")
appbuilder.add_separator("Contacts")

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