from flask import Flask, render_template, flash, redirect, session, request, url_for, logging
import accessors
from wtforms import Form, StringField, validators

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/companies')
def companies():
    data = accessors.get_companies()
    if data == '500':
        return render_template('error_loding_companies.html', companies = data)
    else:
        return render_template('companies.html', companies = data)

@app.route('/company/<string:id>')
def company(id):
    data = accessors.get_company(company_id=id)
    if data == '500':
        return render_template('index.html', companies = data)
    else:
        return render_template('company.html', company = data)

class RegisterCompanyForm(Form):
    company_name = StringField('Company Name', validators=[validators.input_required()])
    beneficial_owner  = StringField('Beneficial owner', validators=[validators.optional()])
    address = StringField('Address', validators=[validators.input_required()])
    city = StringField('City', validators=[validators.input_required()])
    country = StringField('Country', validators=[validators.input_required()])
    phone_number  = StringField('Phone number', validators=[validators.optional()])
    e_mail  = StringField('E-Mail', validators=[validators.optional()])


@app.route('/new_company', methods=['GET', 'POST'])
def new_company():
    form = RegisterCompanyForm(request.form)
    if request.method == 'POST' and form.validate():
        company_name=form.company_name.data
        beneficial_owner=form.beneficial_owner.data
        address=form.address.data
        city=form.city.data
        country=form.country.data
        phone_number=form.phone_number.data
        e_mail=form.e_mail.data
        response = accessors.create_company(company_name, beneficial_owner, address, city,
                                        country, phone_number, e_mail)
        if(response =='Success'):
            return render_template('cretionConfirmation.html')
        else:
            return render_template('error_company_creation.html')
    return render_template('new_company.html', form=form)

@app.route('/delete/<string:id>')
def delete(id):
    status = accessors.delete_company(company_id=id)
    if(status == 'Success'):
        return render_template('delete.html')
    else:
        return render_template('error_deletion_company.html')

class updateCompany(Form):
    company_name = StringField('Company Name', validators=[validators.input_required()])
    beneficial_owner  = StringField('Beneficial owner', validators=[validators.optional()])
    address = StringField('Address', validators=[validators.input_required()])
    city = StringField('City', validators=[validators.input_required()])
    country = StringField('Country', validators=[validators.input_required()])
    phone_number  = StringField('Phone number', validators=[validators.optional()])
    e_mail  = StringField('E-Mail', validators=[validators.optional()])

@app.route('/update_company/<string:id>', methods=['GET', 'POST'])
def update_company(id):
    data = accessors.get_company(company_id=id)
    form = RegisterCompanyForm(request.form)
    if request.method == 'POST' and form.validate():
        company_name=form.company_name.data
        beneficial_owner=form.beneficial_owner.data
        address=form.address.data
        city=form.city.data
        country=form.country.data
        phone_number=form.phone_number.data
        e_mail=form.e_mail.data
        response = accessors.update_company(id, company_name, beneficial_owner, address, city,
                                        country, phone_number, e_mail)
        if(response =='Success'):
            return render_template('updateConfirmaion.html')
        else:
            return render_template('error_updating_company.html')
    return render_template('update_company.html', company = data, form=form)


if __name__=='__main__':
    app.run(debug = True)
