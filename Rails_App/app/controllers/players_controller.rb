require 'csv'
require 'dotenv/load'
require 'rubypython'

class PlayersController < ApplicationController
    def add_all()
        csv_file_path = ENV['CSV_PATH']
        prev_player = CSV.read(csv_file_path)[1]
        puts prev_player
       
    end
end
