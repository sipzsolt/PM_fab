from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, Boolean
from sqlalchemy.orm import relationship
from flask_appbuilder import Model
from app import db
# from views import db


class PM_Skillset(Model):
    __tablename__ = 'pm_skillset'

    id = Column(Integer, primary_key=True)
    name =  Column(String(150), unique = True, nullable=False)

    def __repr__(self):
        return self.name


class PM_User(Model):
    __tablename__ = 'pm_user'

    id = Column(Integer, primary_key=True)

    office_name = Column(String(150))
    position = Column(String(30))
    attachment_ids = Column(String(500))


    office_address_id = Column(Integer, ForeignKey('pm_address.id'))
    office_address = relationship("PM_Address", foreign_keys = [office_address_id])
    office_contact_id = Column(Integer, ForeignKey('pm_contact.id'))
    office_contact = relationship("PM_Contact", foreign_keys = [office_contact_id])
    mailing_address_id = Column(Integer, ForeignKey('pm_address.id'))
    mailing_address = relationship("PM_Address", foreign_keys = [mailing_address_id])
    personal_contact_id = Column(Integer, ForeignKey('pm_contact.id'))
    personal_contact = relationship("PM_Contact", foreign_keys = [personal_contact_id])


    def __repr__(self):
        return self.name




supplkills = db.Table('supplkills', Model.metadata,
    db.Column('pm_skillset_id', Integer, ForeignKey('pm_skillset.id')),
    db.Column('pm_supplier', Integer, ForeignKey('pm_supplier.id'))
)

class PM_Supplier(Model):
    __tablename__ = 'pm_supplier'

    id = Column(Integer, primary_key=True)
    skillset = relationship('PM_Skillset', secondary=supplkills, backref=db.backref('supplkill', lazy='dynamic'))
    skill_grade = Column(String(500))
    introduction = Column(String(1000))

    quality_assurance = Column(String(150))
    certification = Column(String(300))
    goods_service = Column(String(150))
    goods_list = Column(String(150))
    service_list = Column(String(150))

    consultant_name = Column(String(200))
    gdpr = Column(Boolean(False))
    attachment_ids = Column(String(500))
    project_ids = Column(String(500))

    consultant_id = Column(Integer, ForeignKey('pm_contact.id'))
    consultant = relationship("PM_Contact", foreign_keys=[consultant_id])

    company_relations_id = Column(Integer, ForeignKey('pm_company_relations.id'))
    company_relations = relationship("PM_Company_Relations", foreign_keys = [company_relations_id])

    mailing_address_id = Column(Integer, ForeignKey('pm_address.id'))
    mailing_address = relationship("PM_Address", foreign_keys = [mailing_address_id])

    bank_id = Column(Integer, ForeignKey('pm_banking.id'))
    bank = relationship("PM_Banking", foreign_keys = [bank_id])



    def __repr__(self):
        return str(self.id)


class PM_Customer(Model):
    __tablename__ = 'pm_customer'

    id = Column(Integer, primary_key=True)
    introduction = Column(String(1000))
    ignored = Column(String(1000))
    consultant_name = Column(String(200))
    attachment_ids = Column(String(500))

    consultant_id = Column(Integer, ForeignKey('pm_contact.id'))
    consultant = relationship("PM_Contact", foreign_keys=[consultant_id])

    mailing_address_id = Column(Integer, ForeignKey('pm_address.id'))
    mailing_address = relationship("PM_Address", foreign_keys = [mailing_address_id])

    company_relations_id = Column(Integer, ForeignKey('pm_company_relations.id'))
    company_relations = relationship("PM_Company_Relations", foreign_keys = [company_relations_id])

    bank_id = Column(Integer, ForeignKey('pm_banking.id'))
    bank = relationship("PM_Banking", foreign_keys = [bank_id])



    def __repr__(self):
        return str(self.id)


# ids = db.Table('ids', Model.metadata,
#     db.Column('skillset_id', Integer, ForeignKey('skillset.id')),
#     db.Column('customer_user_id', Integer, ForeignKey('user.id')),
#     db.Column('project_history_id', Integer, ForeignKey('project.id'))
# )
projskills = db.Table('projskills', Model.metadata,
    db.Column('pm_skillset_id', Integer, ForeignKey('pm_skillset.id')),
    db.Column('pm_project_id', Integer, ForeignKey('pm_project.id'))
)


class PM_Project(Model):
    __tablename__ = 'pm_project'

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    type = Column(String(150), nullable=False)
    phases = Column(String(1500), nullable=False)
    description = Column(String(1500))
    skillset = relationship('PM_Skillset', secondary=projskills, backref=db.backref('projskill', lazy='dynamic'))
    skill_grade = Column(String(500))
    budget = Column(String(150), nullable=False)
    employees_need = Column(Integer)
    person_days = Column(Integer)
    responsible_person = Column(String(150))
    backup_person = Column(String(150))
    project_planned_start = Column(Date)
    project_planned_end = Column(Date)

    attachment_ids = Column(String(500))
    project_history_ids = Column(String(500))

    customer_id = Column(Integer, ForeignKey('pm_customer.id'))
    customer = relationship("PM_Customer")


    # ids = relationship("Skillset", secondary=ids, backref=db.backref('f_ids', lazy='dynamic'))

    def __repr__(self):
        return self.name


class PM_Rating(Model):
    __tablename__ = 'pm_rating'

    id = Column(Integer, primary_key=True)
    rate = Column(Integer)
    comment = Column(String(1500))
    sources = Column(String(1500))

    attachment_ids = Column(String(500))  # evidence


    user_id = Column(Integer, ForeignKey('pm_user.id'))
    user = relationship("PM_User")
    project_id = Column(Integer, ForeignKey('pm_project.id'))
    project = relationship("PM_Project")


    def __repr__(self):
        return str(self.id)

class PM_Project_QA(Model):
    __tablename__ = 'pm_project_qa'

    id = Column(Integer, primary_key=True)
    message = Column(String(1500))

    attachment_ids = Column(String(500))


    user_id = Column(Integer, ForeignKey('pm_user.id'))
    user = relationship("PM_User")
    project_id = Column(Integer, ForeignKey('pm_project.id'))
    project = relationship("PM_Project")


    def __repr__(self):
        return str(self.id)


class PM_Address(Model):
    __tablename__ = 'pm_address'

    id = Column(Integer, primary_key=True)
    street_address = Column(String(150))
    postal_nr = Column(String(20))
    city = Column(String(50))
    country = Column(String(30))

    def __repr__(self):
        return str(self.id)


class PM_Contact(Model):
    __tablename__ = 'pm_contact'

    id = Column(Integer, primary_key=True)
    phone_mobile = Column(String(30))
    phone_office = Column(String(30))
    phone_private = Column(String(30))
    email = Column(String(150), nullable=False)
    email_secondary = Column(String(150))
    fax = Column(String(50))
    website = Column(String(200))

    def __repr__(self):
        return str(self.id)


class PM_Attachment(Model):
    __tablename__ = 'pm_attachment'

    id = Column(Integer, primary_key=True)
    table_id = Column(String(200))
    table_name = Column(String(200))
    file = Column(String(200))
    ufilename = Column(String(200))

    def __repr__(self):
        return str(self.id)


class PM_Banking(Model):
    __tablename__ = 'pm_banking'

    id = Column(Integer, primary_key=True)
    bank_name = Column(String(150))
    branch_name = Column(String(150))
    bank_account_number = Column(String(150))
    account_currency = Column(String(50))
    iban = Column(String(150))
    bic = Column(String(150))
    routing_bank_details = Column(String(150))
    annual_value_of_total_sales = Column(String(150))
    annual_value_of_export_sales = Column(String(150))
    audit_reports = Column(String(300))
    bankruptcy_legal_action = Column(String(5))

    attachment_ids = Column(String(500))


    branch_address_id = Column(Integer, ForeignKey('pm_address.id'))
    branch_address = relationship("PM_Address", foreign_keys = [branch_address_id])
    branch_contact_id = Column(Integer, ForeignKey('pm_contact.id'))
    branch_contact = relationship("PM_Contact", foreign_keys = [branch_contact_id])


    def __repr__(self):
        return self.bank_name


class PM_Company_Relations(Model):
    __tablename__ = 'pm_company_relations'

    id = Column(Integer, primary_key=True)
    company_name = Column(String(150), nullable=False)
    parent_company = Column(String(150))
    subsidiaries = Column(String(300))
    associates = Column(String(300))
    international_offices = Column(String(300))
    type_of_business = Column(String(150))
    nature_of_business = Column(String(150))
    year_of_establishment = Column(Integer)
    employees = Column(Integer)
    licence_number = Column(String(150))
    vat_tax_id = Column(String(150))
    working_languages = Column(String(150))

    attachment_ids = Column(String(500))


    company_address_id = Column(Integer, ForeignKey('pm_address.id'))
    company_address = relationship("PM_Address", foreign_keys=[company_address_id])
    company_contact_id = Column(Integer, ForeignKey('pm_contact.id'))
    company_contact = relationship("PM_Contact", foreign_keys=[company_contact_id])



    def __repr__(self):
        return self.company_name


db.create_all()
