class CreatePlayers < ActiveRecord::Migration[7.1]
  def change
    create_table :players do |t|
      t.string :name
      t.string :stats
      t.integer :age
      t.string :team
      t.string :draft_year
      t.string :season_start
      t.string :season_end
      t.string :prev_teams
      
      t.timestamps
    end
  end
end
