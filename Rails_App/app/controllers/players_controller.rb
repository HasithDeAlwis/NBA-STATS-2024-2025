require 'csv'
csv_file_path = '/csv-file/all_players_stats.csv'

class PlayersController < ApplicationController
    def add_all()
        CSV.foreach(csv_file_path, headers: true) do |row|
            print(row['id'])
end
