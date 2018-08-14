class CreateCompanies < ActiveRecord::Migration[5.2]
  def change
    create_table :companies do |t|
      t.string :Name
      t.string :Address
      t.string :City
      t.string :Country
      t.string :E_Mail
      t.string :Phone_number
      t.string :Beneficial_owner

      t.timestamps
    end
  end
end
