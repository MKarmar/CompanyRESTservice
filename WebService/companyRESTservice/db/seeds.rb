5.times do
  Company.create({
    Name: Faker::Company.name,
    Address: Faker::Address.street_address,
    City: Faker::Address.city,
    Country: Faker::Address.country,
    E_Mail: Faker::Internet.email,
    Phone_number: Faker::PhoneNumber.cell_phone,
    Beneficial_owner: Faker::Name.name
    })
end
