Rails.application.routes.draw do
  resources :players
  get "/search", to: "players#search", as: :search
  post "/add_all", to:"players#add_all", as: :add_all
end
