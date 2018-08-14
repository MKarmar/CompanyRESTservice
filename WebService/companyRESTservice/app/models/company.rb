class Company < ApplicationRecord
  validates :Name, presence: true
  validates :Address, presence: true
  validates :City, presence: true
  validates :Country, presence: true
end
