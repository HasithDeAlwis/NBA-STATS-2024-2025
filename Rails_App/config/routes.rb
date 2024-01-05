Rails.application.routes.draw do
  resources :players
  get "/search", to: "players#search", as: :search
end
