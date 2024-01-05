# This file should ensure the existence of records required to run the application in every environment (production,
# development, test). The code here should be idempotent so that it can be executed at any point in every environment.
# The data can then be loaded with the bin/rails db:seed command (or created alongside the database with db:setup).
#
# Example:
#
#   ["Action", "Comedy", "Drama", "Horror"].each do |genre_name|
#     MovieGenre.find_or_create_by!(name: genre_name)
#   end
player = Player.create(name: "Lebron James", age:40, stats:"2023:25-07-08-1.2-0.8-0.43-0.38**2022:27-6-8-1.1-0.9-0.45-0.40", team:"Los Angeles Lakers", prev_teams: "Los Angeles Lakers**Cleveland Cavaliers")
