# Company REST service

This project is a simple REST service able to store, update and delete company information.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
In order to run this project please ensure that you have the following functionalities installed.

* Ruby version 2.4.4p296

* Rails 5.2.1

* Faker 1.9.1 - for development purposes

* cURL 7.50.1

### Installing

In order to install this REST service for development, you will need to download the source code from [GitHub](https://github.com/MKarmar/CompanyRESTservice).

Now if the prerequisites are meet, than the project is run like any other rails project, by opening a command line such as bash, navigate to folder in which the project is placed, and typing:
```
  $rails s
```

This will lunch the server. Now the content of the data can be accessed in a restful manner, using as example cURL. In order to get a overview of the content of the REST database, you use the cURL command:
```
  $curl http://localhost:3000/api/v1/companies
```

Now the same procedure are used for the other REST methods which are:
* Getting information of a single company, where #id in the url is the company id assigned by the database
```
  $curl http://localhost:3000/api/v1/companies/#id
```
* Creating a Company
```
  curl -X POST \
  http://localhost:3000/api/v1/companies/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
	"Name":"Name of company",
	"Address":"Address of company",
	"City":"City in which the company is located",
	"Country":"Country in which the company is located",
	"E_Mail":"Optional: E-mail of company",
	"Phone_number":"Optional: phone number of the company",
  "Beneficial_owner": "Optional: beneficial owner of the company"
  }'
```
* Updating company information
```
  curl -X PUT \
  http://localhost:3000/api/v1/companies/#id_of_company \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
  "Attribute to chance":"new value"
  }'
```
* Deleting a company
```
  curl -X DELETE \
  http://localhost:3000/api/v1/companies/#id_of_company \
  -H 'cache-control: no-cache'
```



## Deployment
For deployment of the REST service a docker file can be found at [GitHub](). Using this docker-file, a server contacting the REST service will be created in production mode. If data is required in the database, you will have to seed the database using the command:
```
  $rails db:seed
```
This will create 5 non-existing companies in the database for testing purposes.

## Built With

* [Bundler](https://bundler.io/) - Gem file installer



## Versioning

[GitHub](https://github.com/MKarmar/CompanyRESTservice) is used for versioning of this project.

## Authors
* **Mark Karmar**


## Acknowledgments

* [Readme template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) by Billie Thompson
* Ruby on Rails [REST api tutorial](https://www.youtube.com/watch?v=QojnRc7SS9o)
