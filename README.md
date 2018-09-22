# FAST_FOOD_FAST API

Fast-Food-Fast is a food delivery service app for a restaurant.

### Badges
[![Build Status](https://travis-ci.com/Gfreedoms/Fast-Food-Fast.svg?branch=api)](https://travis-ci.com/Gfreedoms/Fast-Food-Fast)
[![Coverage Status](https://coveralls.io/repos/github/Gfreedoms/Fast-Food-Fast/badge.svg?branch=api)](https://coveralls.io/github/Gfreedoms/Fast-Food-Fast?branch=api)
[![Maintainability](https://api.codeclimate.com/v1/badges/f3539663b70ac1e25979/maintainability)](https://codeclimate.com/github/Gfreedoms/Fast-Food-Fast/maintainability)


- ## API
This App exposes endpoints that allows ```customers and hotel owners``` toaccess food and manage orders respectively

- ## Heroku URL
[FAST FOOD FAST hosted on  heroku ](https://food-food-fast-api.herokuapp.com/api/v1/orders)

## Functionality

- Retrieving Order for food
- Placing order for food
- Retrieving a specific order.
- Delete order

- #### Available Resource Endpoints

|Method | Endpoint | Usage |
| ---- | ---- | --------------- |
|POST| `/api/v1/orders` | Post an Order|
|GET| `/api/v1/orders` | Retrieve a list of orders|
|GET| `//api/v1/orders/1` | Retrieve order with with id that equals 1.|
|PUT| `//api/v1/orders/1` |Update order with a given id |
|DELETE| `/api/v1/orders/1` | Delete Order with a  give id.|


## Getting Started 🕵
- To run on local machine git clone this project :
```
 $ git clone https://github.com/Gfreedoms/Fast-Food-Fast.git
 ```

 Copy and paste the above command in your terminal, the project will be downloaded to your local machine.

- To consume API in client of choice navigate to:
 ```
 http://localhost:5000/
 ```

### Prerequisites
The application is built using python: Flask framework.
>[Flask](http://flask.pocoo.org/) is a micro-framework for the Python programming language.


To Install python checkout:
```
https://www.python.org/
```


### Installing
For this section I will assume you have python3 and it's configured on your machine. </br>
Navigate to the folder you cloned and run: </br>

- Install Requirements
```
$ cd src
$ pip install -r requirements.txt
```


- Run API 🏃
```
$ cd src
$ python app.py runserver
```
The API should be accessible via : http://127.0.0.1:5000/


## Running the tests

```
$ cd the directory where you have cloned the project
$ pytest.py
```

- Coding style tests

[PEP8](https://pypi.org/project/pycodestyle/) (pycodestyle) standards are followed in project. </br>

```
$ cd the directory where you have cloned the project
$ pycodestyle .

```


## Set Up Notifications Package
 - [Check this out to set up the Notifications Package](src/api/utils/notifications/README_notifications.md)

## Deployment 🚀

- [Check this out to deploy to heroku](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)

## Built With  🏗 🔨⚒

* [Flask](http://flask.pocoo.org/) - The web framework used
* [Flaskrestplus](https://flask-restplus.readthedocs.io/en/stable/) - Extension for Flask that adds support for quickly building REST APIs.

## Contributing 👍

- Please Fork me! :-)

## Versioning ⚙

`This is the version one`

## Authors 📚

* **FREEDOM GEMMAR**


## License 🤝

- This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments 🙏

* [Andela ](https://andela.com/) - Bootcamp Cohort 12 Ninjas !
* Fellow "BOOTCAMPERS"
* [Motivation](https://www.youtube.com/watch?v=dQw4w9WgXcQ) - BEST RESOURCE EVER!!! 🤓🤓
