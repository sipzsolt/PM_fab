from flask import flash
from wtforms import Form, StringField, FieldList, FormField, BooleanField, SelectMultipleField, widgets, RadioField, IntegerField, DateField, FileField, TextAreaField
from wtforms.validators import DataRequired, Email, ValidationError
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget, DatePickerWidget
from flask_appbuilder.forms import DynamicForm
from app import db
from .models import PM_Skillset


emailmessage = 'Please add a correct email format!'


# <___ Custom widgets ___>

def select_multi_checkbox(field, ul_class='', **kwargs):
    kwargs.setdefault('type', 'checkbox')
    field_id = kwargs.pop('id', field.id)

    html = [u'<div class="checkbox">']
    html.append(u'<ul %s>' % widgets.html_params(id=field_id, class_=ul_class))
    for value, label, checked in field.iter_choices():
        choice_id = u'%s-%s' % (field_id, value)
        options = dict(kwargs, name=field.name, value=value, id=choice_id, onchange='check("'+choice_id+'")')
        radiooptions = dict(kwargs, id="ra"+choice_id, style="display: none")
        if checked:
            options['checked'] = 'checked'
        flash(list(options.keys()), "info")
        html.append(u'<li><input %s/> ' % widgets.html_params(**options))
        html.append(u'<label for="%s">%s</label></li>' % (field_id, label))

        html.append(u'<div %s>' % widgets.html_params(**radiooptions))

        html.append(u'<label class="radio-inline">')
        html.append(u'<input type="radio" name="%s" id="low" value="low" checked>low' % ("ra"+choice_id))
        html.append(u'</label>')

        html.append(u'<label class="radio-inline">')
        html.append(u'<input type="radio" name="%s" id="medium" value="medium" checked>medium' % ("ra"+choice_id))
        html.append(u'</label>')

        html.append(u'<label class="radio-inline">')
        html.append(u'<input type="radio" name="%s" id="high" value="high" checked>high' % ("ra"+choice_id))
        html.append(u'</label>')


        html.append(u'</div>')
    html.append(u'</ul>')

    html.append(u'</div>')

    return u''.join(html)


def files_with_text(field, ul_class='', **kwargs):
    kwargs.setdefault('type', 'file')
    field_id = kwargs.pop('id', field.id)

    # html = [u'<ul %s>' % widgets.html_params(id=field_id, class_=ul_class, style="list-style-type: none;")]
    html = [u'<div %s>' % widgets.html_params(class_=field.name+'container')]

    html.append(u'<div class="row">')
    html.append(u'<input %s>' % widgets.html_params(type='text', name=field.name + '-0'))
    html.append(u'<button %s>' % widgets.html_params(type='button', class_="btn btn-default btn-sm add_form_field", id=field.name + '-btn-0', onclick='addFormField("'+field.name+'","0")'))
    html.append(u'<span class="glyphicon glyphicon-plus-sign"></span>')
    html.append(u'</button>')
    html.append(u'</div>')

    html.append(u'<input %s multiple>' % widgets.html_params(type='file', name=field.name + '-file-0', id=field.name + '-file-0', class_='fileinput', onchange='addFileName("'+field.name+'","0")'))
    html.append(u'<div %s>' % widgets.html_params(class_=field.name + '-filenames-0'))
    html.append(u'</div>')

    html.append(u'</div>')

    return u''.join(html)


def radio_with_text(field, ul_class='', **kwargs):
    kwargs.setdefault('type', 'radio')
    field_id = kwargs.pop('id', field.id)

    html = [u'<ul %s>' % widgets.html_params(id=field_id, class_=ul_class, style="list-style-type: none;")]
    for value, label, checked in field.iter_choices():
        choice_id = u'%s-%s' % (field_id, value)
        options = dict(kwargs, name=field.name, value=value, id=choice_id, onchange='checkRadio("'+choice_id+'", "'+field.name+'")')
        radiooptions = dict(kwargs, id="ra"+choice_id, style="display: none")
        if checked:
            options['checked'] = 'checked'
        html.append(u'<li><input %s/> ' % widgets.html_params(**options))
        html.append(u'<label for="%s">%s</label></li>' % (field_id, label))

    html.append(u'<input type="text" id="%s" name="%s" style="display: none"/>'  % (field.name+"-othertext", field.name+"-othertext"))
    html.append(u'</ul>')

    return u''.join(html)


# <___ Custom form fields ___>

class MultiFileField(FileField):

    def pre_validate(self, form):
        """per_validation is disabled"""


class MultiCheckboxFieldWithRate(SelectMultipleField):

    def pre_validate(self, form):
        """per_validation is disabled"""


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

    def pre_validate(self, form):
        """per_validation is disabled"""


# <___ Form templates ___>

class Company(DynamicForm):
    # ('Type of Business', choices=[("limited", "Corporate/ Limited"), ("partner", "Partnership")])
    company_name = StringField('Company Name', validators=[DataRequired()], widget=BS3TextFieldWidget())
    company_address = StringField('Company Street Address', validators=[DataRequired()], widget=BS3TextFieldWidget())
    company_postal_nr = StringField('Company Postal Code', validators=[DataRequired()], widget=BS3TextFieldWidget())
    company_city = StringField('Company City', validators=[DataRequired()], widget=BS3TextFieldWidget())
    company_country = StringField('Company Country', validators=[DataRequired()], widget=BS3TextFieldWidget())
    company_phone = StringField('Company Telephone', validators=[DataRequired()], widget=BS3TextFieldWidget())
    company_fax = StringField('Company Fax', widget=BS3TextFieldWidget())
    company_email = StringField('Company Email', validators=[DataRequired(message='Please add a Company Email!'), Email(message=emailmessage)], widget=BS3TextFieldWidget())
    company_website = StringField('Company Website', widget=BS3TextFieldWidget())
    introduction = TextAreaField('Short Introduction', validators=[DataRequired()])
    parent_company = StringField('Parent Company', widget=BS3TextFieldWidget())
    subsidiaries = TextAreaField('Subsidiaries')
    associates = TextAreaField('Associates')
    international_offices = TextAreaField('International Offices', validators=[DataRequired()])
    type_of_business = RadioField('Type of Business', choices=[("limited", "Corporate/ Limited"), ("partner", "Partnership"), ("other", "Other")], widget=radio_with_text)
    nature_of_business = RadioField('Nature of Business', choices=[("limited", "Corporate/ Limited"), ("partner", "Partnership"), ("other", "Other")], widget=radio_with_text)
    year_of_establishment = IntegerField('Year Established', validators=[DataRequired()], widget=BS3TextFieldWidget())
    employees = IntegerField('Number of Full-time Employees', validators=[DataRequired()], widget=BS3TextFieldWidget())
    licence_number = StringField('Licence Number', validators=[DataRequired()], widget=BS3TextFieldWidget())
    vat_tax_id = StringField('VAT No./Tax I.D', validators=[DataRequired()], widget=BS3TextFieldWidget())
    working_languages = MultiCheckboxField('Working Languages', choices=[("en", "en"), ("ge", "ge"), ("hu", "hu"), ("fr", "fr")])
    files = FileField(u'Files', widget=files_with_text)


class Mailing(DynamicForm):
    mailing_address = StringField('Mailing Street Address', validators=[DataRequired()], widget=BS3TextFieldWidget())
    mailing_postal_nr = StringField('Mailing Postal Code', validators=[DataRequired()], widget=BS3TextFieldWidget())
    mailing_city = StringField('Mailing City', validators=[DataRequired()], widget=BS3TextFieldWidget())
    mailing_country = StringField('Mailing Country', validators=[DataRequired()], widget=BS3TextFieldWidget())


class Banking(DynamicForm):
    bank_name = StringField('Bank Name', validators=[DataRequired()], widget=BS3TextFieldWidget())
    branch_name = StringField('Branch Name', validators=[DataRequired()], widget=BS3TextFieldWidget())
    branch_address = StringField('Branch Street Address', validators=[DataRequired()], widget=BS3TextFieldWidget())
    branch_postal_nr = StringField('Branch Postal Code', validators=[DataRequired()], widget=BS3TextFieldWidget())
    branch_city = StringField('Branch City', validators=[DataRequired()], widget=BS3TextFieldWidget())
    branch_country = StringField('Branch Country', validators=[DataRequired()], widget=BS3TextFieldWidget())
    branch_phone = StringField('Branch Telephone', validators=[DataRequired()], widget=BS3TextFieldWidget())
    branch_fax = StringField('Company Fax', widget=BS3TextFieldWidget())
    bank_account_number = StringField('Bank Account Number', validators=[DataRequired()], widget=BS3TextFieldWidget())
    account_currency = StringField('Account currency', validators=[DataRequired()], widget=BS3TextFieldWidget())
    iban = StringField('International Bank Account Number (IBAN)', validators=[DataRequired()], widget=BS3TextFieldWidget())
    bic = StringField('Swift/Bank Identifier Code (BIC)', validators=[DataRequired()], widget=BS3TextFieldWidget())
    routing_bank_details = StringField('Routing Bank details', validators=[DataRequired()], widget=BS3TextFieldWidget())
    annual_value_of_total_sales = StringField('Annual Value of Total Sales for the last 3 Years', validators=[DataRequired()], widget=BS3TextFieldWidget())
    annual_value_of_export_sales = StringField('Annual Value of Export Sales for the last 3 Years', validators=[DataRequired()], widget=BS3TextFieldWidget())
    audit_reports = FileField("If available, please provide a copy of the company's three latest annual or audited Financial Report.", widget=files_with_text)
    bankruptcy_legal_action = StringField('Do you have outstanding bankruptcy, judgment or pending legal action that could impair operating as a going concern?', validators=[DataRequired()], widget=BS3TextFieldWidget())
    files = FileField(u'Files', widget=files_with_text)


class Skill(DynamicForm):
    skilldb = db.session.query(PM_Skillset).all()
    skillchoices = [(x, str(x).capitalize()) for x in skilldb]

    skillset = MultiCheckboxFieldWithRate('Skillset', choices= skillchoices, widget=select_multi_checkbox)


class Services(DynamicForm):
    quality_assurance = StringField('Quality Assurance Certification (e.g. ISO 9000 or Equivalent)', validators=[DataRequired()], widget=BS3TextFieldWidget())
    certification = StringField('Certification(s)', validators=[DataRequired()], widget=BS3TextFieldWidget())
    goods_service = StringField('Goods / Services Offered', validators=[DataRequired()], widget=BS3TextFieldWidget()) # http://www.unhcr.org/479a04502.pdf Sec 3
    goods_list = StringField('Core Goods Offered', validators=[DataRequired()], widget=BS3TextFieldWidget())
    service_list = StringField('Core Services Offered', validators=[DataRequired()], widget=BS3TextFieldWidget())
    files = FileField(u'Files', widget=files_with_text)


# <___ Forms ___>

class New_PM_Customer(DynamicForm):

    company = FormField(Company,label="Company information")
    mailing = FormField(Mailing,label="Mailing information")
    banking = FormField(Banking,label="Banking information")


class New_PM_Supplier(DynamicForm):
    skillset = FormField(Skill, label="Skill information")
    company = FormField(Company, label="Company information")
    mailing = FormField(Mailing, label="Mailing information")
    services = FormField(Services, label="Services information")
    banking = FormField(Banking, label="Technical Capability and Information on Goods / Services Offered")


def unique(form, field):
    skilldb = db.session.query(PM_Skillset).all()
    skills = [str(x) for x in skilldb]
    if field.data.lower() in skills:
        raise ValidationError('"{0}" is already in the database'.format(field.data.lower()))

class Add_Skill(DynamicForm):
    skill = StringField('Skill', validators=[DataRequired(), unique], widget=BS3TextFieldWidget())


class New_PM_Project(DynamicForm):
    name = StringField('Project Name', validators=[DataRequired()], widget=BS3TextFieldWidget())
    description = TextAreaField('Project Description', validators=[DataRequired()])

    skillset = FormField(Skill, label="Skill information")

    budget = StringField('Project Budget', validators=[DataRequired()], widget=BS3TextFieldWidget())
    employees_need = IntegerField('Employees needed', validators=[DataRequired()], widget=BS3TextFieldWidget())
    person_days = IntegerField('Planned Person Days', validators=[DataRequired()], widget=BS3TextFieldWidget())
    responsible_person = StringField('Responsible Person', widget=BS3TextFieldWidget())
    backup_person = StringField('Backup Person', validators=[DataRequired()], widget=BS3TextFieldWidget())
    project_planned_start = DateField('Project Planned Start', validators=[DataRequired()], widget=DatePickerWidget())
    project_planned_end = DateField('Project Planned End', validators=[DataRequired()], widget=DatePickerWidget())


# <___ Testing ___>

class Com(DynamicForm):

    type_of_business = RadioField('Type of Business', choices=[("limited", "Corporate/ Limited"), ("partner", "Partnership"), ("other", "Other")], widget=radio_with_text)
    nature_of_business = RadioField('Nature of Business', choices=[("limited", "Corporate/ Limited"), ("partner", "Partnership"), ("other", "Other")], widget=radio_with_text)
    company_email = StringField(('Company Email'), validators=[DataRequired(message='Please add a Company Email!'), Email(message=emailmessage)], widget=BS3TextFieldWidget())


class Add_Skillt(DynamicForm):
    skilldb = db.session.query(PM_Skillset).all()
    skillchoices = [(x, str(x).capitalize()) for x in skilldb]

    skillset = MultiCheckboxFieldWithRate(choices= skillchoices, widget=select_multi_checkbox)
    skillt = FormField(Skill, label="Skill information")

    # select_multi_checkbox(skillset)
    type_of_business = RadioField('Type of Business',
                                  choices=[("limited", "Corporate/ Limited"), ("partner", "Partnership"),("other", "Other")],
                                  widget=radio_with_text
                                  )

    com = FormField(Com, label="comp", validators=[])

    company_email = StringField('Company Email', validators=[DataRequired(message='Please add a Company Email!'), Email(message=emailmessage)], widget=BS3TextFieldWidget())

    files = FileField(u'Files', widget=files_with_text)
    # description = TextAreaField(u'Image Description')