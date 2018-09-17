# FAST_FOOD_FAST API

Fast-Food-Fast is a food delivery service app for a restaurant.

### Badges
[![Build Status](https://travis-ci.com/Gfreedoms/Fast-Food-Fast.svg?branch=api)](https://travis-ci.com/Gfreedoms/Fast-Food-Fast)
[![Coverage Status](https://coveralls.io/repos/github/Gfreedoms/Fast-Food-Fast/badge.svg?branch=api)](https://coveralls.io/github/Gfreedoms/Fast-Food-Fast)

# APIs

These are APIs to be used on the fast food first front end application

## Functionality

- Placing order for food
- Obtaining a list of orders.
- Fetching a specific order.
- Updating the order status.
- Delete order

These are the endpoints

| METHOD | Endpoint          | Description                                                          | Body (json)                                                    |
| ------ | :---------------- | -------------------------------------------------------------------- | -------------------------------------------------------------- |
| GET    | /api/v1/orders/   | Get all orders                                                       |                                                                |
| GET    | /api/v1/orders/id | Get specific orders using an id                                      |                                                                |
| POST   | /api/v1/orders    | Place a new orders                                                   | order_number, order_description ,order_price ,size |
| PUT    | /api/v1/orders/id | Update a specific orders status to 'complete', | order_status                                                   |
| DELETE | /api/v1/orders/id |delete a specific order                                 |                                                                |

Heroku URL



## Seting Up for Development environment

These are instructions for setting up Fast Food Fast app in a development enivornment.

### Prerequisites

- Python 3.6

- Make a directory on your computer and a virtual environment

 