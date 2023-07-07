<h1 align="center">Golden Owl Code Test</h1>
<p>
  <a href="/" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/Documentation-yes-brightgreen.svg" />
  </a>
  <a href="./LICENSE" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

> This is Thanh Ngoc's submission for Golden Owl's Code Test for Back-end Intern Position

### 🏠 [Source Code](https://github.com/esvm4/ThanhNgoc-GoldenOwl-CodeTest)

### ✨ [Deployed Web](/)

## Author

👤 **Thanh Ngoc**

-   Github: [@esvm4](https://github.com/esvm4)

## Usage

-   Clone code from this repository
    ```bash
    git clone git@github.com:esvm4/BackendIntern-CodeTest.git
    cd BackendIntern-CodeTest
    ```
-   Create a virtual environment (optional)
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate # choose your own shell environment
    ```
-   Install all dependencies and packages
    ```bash
    pip install -r requirements.txt
    ```
-   Run preprocessing script to generate data for the app
    ```bash
    python3 preprocessing.py
    ```
-   Run the app
    ```bash
    python3 app.py
    ```
-   Open your browser of choice and go to `localhost:5004` or `127.0.0.1:5004` to view the local website

## Features

### Must have

-   [ ] Display all products in `Our Products` section (for products data please check from [Technical Requirements](#technical-requirements-checklist)):
    -   [x] Single product should have name, description, price, image and `Add To Cart` button.
    -   [x] User able to click on `Add To Cart` to add target product to their cart.
    -   [ ] Added product doesn't have `Add To Cart` button anymore, it should have `Check Mark Icon` (✓) instead.
    -   [x] Display all added products in `Your Cart` section:
    -   [x] Each product in cart should have name, price, image, increase/decrease amount button and remove button.
    -   [x] User able to increase/decrease amount of a product in cart. When product's amount is decreased to zero, that product will be removed from cart naturally.
    -   [x] User able to remove product from cart.
    -   [x] Show total price of all products in car. When user increase/decrease product's amount or remove product, total price should be re-calculate correctly.
    -   [x] When there are no products in cart, we should show `Your cart is empty` message.
    -   [x] Products in cart should be persistent: When user visit the application, products are added before should be showed, user don't need to add products again.
-   [x] UI must follow correctly design from [live demo](https://gshoes.vercel.app/).

### Nice to have

-   [x] Responsive design (look good on all devices: desktops, tablets & mobile phones).
-   [ ] Smooth animations (don't really need to be same as the demo, just do what you think is good).
-   [ ] Deploy the application to heroku.

## Technical Requirements Checklist

-   [x] BE & FE : Can use Django MVT or Flask and Jinja templates
-   [x] Database : Using Postgres or MySQL
-   [ ] Deployment: Heroku
-   [x] Products data: [shoes.json](https://github.com/LarryPham1801/webdev-intern-assignment/blob/main/app/data/shoes.json)
-   [x] Images & icons: [assets/](https://github.com/LarryPham1801/webdev-intern-assignment/blob/main/app/assets)
-   [x] Fonts: [Rubik](https://fonts.google.com/specimen/Rubik?query=Rubik)
-   [x] Colors:
    -   White: #FFFFFF
    -   Black: #303841
    -   Gray: #777777
    -   Yellow: #F6C90E

## 📝 License

Copyright © 2023 [Thanh Ngoc](https://github.com/esvm4).<br />
This project is [MIT](./LICENSE) licensed.
