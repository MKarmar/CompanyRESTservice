import requests
import json

url='http://localhost:3000/api/v1/companies' #Update depending on context
header = {'content-type': 'application/json'}

def get_companies():
    try:
        companies_json = requests.get(url)
    except requests.exceptions.ConnectionError:
        return '500'
    companies_python = json.loads(companies_json.text)
    return companies_python['data']

def get_company(company_id):
    urlTemp=url+'/'+company_id
    try:
        companies_json = requests.get(urlTemp)
    except requests.exceptions.ConnectionError:
        return '500'
    companies_python = json.loads(companies_json.text)
    return companies_python['data']

def create_company(name, owner, address, city, country, phone, email):
    data = {}
    data['Name'] = name
    data['Beneficial_owner'] = owner
    data['Address'] = address
    data['City'] = city
    data['Country'] = country
    data['Phone_number'] = phone
    data['E_Mail'] = email
    try:
        reply_json = requests.post(url, headers=header, json=data)
    except requests.exceptions.ConnectionError:
        return '500'
    reply_python = json.loads(reply_json.text)
    return reply_python['status']

def delete_company(company_id):
    urlTemp=url+'/'+company_id
    try:
        deletion_confirmation_json = requests.delete(urlTemp)
    except requests.exceptions.ConnectionError:
        return '500'
    deletion_confirmation_python = json.loads(deletion_confirmation_json.text)
    return deletion_confirmation_python['status']

def update_company(company_id, name, owner, address, city, country, phone, email):
    urlTemp=url+'/'+company_id
    data = {}
    data['Name'] = name
    data['Beneficial_owner'] = owner
    data['Address'] = address
    data['City'] = city
    data['Country'] = country
    data['Phone_number'] = phone
    data['E_Mail'] = email
    try:
        reply_json = requests.put(urlTemp, headers=header, json=data)
    except requests.exceptions.ConnectionError:
        return '500'
    reply_python = json.loads(reply_json.text)
    return reply_python['status']

if __name__=='__main__':
    create_company('name', 'owner', 'address', 'city', 'country', 'phone', 'email')
