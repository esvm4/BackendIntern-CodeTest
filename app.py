from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shoes.db"
db = SQLAlchemy(app)


class Shoe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(), nullable=False)
    name = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    price = db.Column(db.Float(5, 2), nullable=False)
    color = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return "<Product %r>" % self.id


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("shoe.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    product = db.relationship("Shoe", backref="cart")

    def __repr__(self):
        return "<Cart %r>" % self.id


def calculate_total_price(carts):
    total_price = 0
    for cart in carts:
        total_price += cart.product.price * cart.quantity
    return total_price


@app.route("/", methods=["POST", "GET"])
def home():
    image_urls = {
        "check": url_for("static", filename="assets/check.png"),
        "minus": url_for("static", filename="assets/minus.png"),
        "nike": url_for("static", filename="assets/nike.png"),
        "plus": url_for("static", filename="assets/plus.png"),
        "trash": url_for("static", filename="assets/trash.png"),
    }
    titleProduct = "Our Products"
    titleCart = "Your Cart"
    titlePrice = 0

    if request.method == "POST":
        product_id = request.form.get("product_id")
        # Check if the product is already in cart
        cart_item = Cart.query.filter_by(product_id=product_id).first()
        if not cart_item:
            # If the product is not in the cart, create a new cart item
            cart_item = Cart(product_id=product_id, quantity=1)
            db.session.add(cart_item)
            db.session.commit()
        return redirect(url_for("home"))
    else:
        products = Shoe.query.all()
        carts = Cart.query.all()
        titlePrice = float(str(calculate_total_price(carts))[:10])
        for product in products:
            product.price = float(str(product.price)[:5])
        return render_template(
            "index.html",
            products=products,
            carts=carts,
            **image_urls,
            titleProduct=titleProduct,
            titleCart=titleCart,
            titlePrice=titlePrice
        )


@app.route("/remove-from-cart", methods=["POST"])
def remove_from_cart():
    item_id = request.form.get("item_id")

    cart_item = Cart.query.get(item_id)

    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()

    return redirect(url_for("home"))


@app.route("/update-cart", methods=["POST"])
def update_cart():
    item_id = request.form.get("item_id")
    action = request.form.get("action")
    cart_item = Cart.query.get(item_id)
    if cart_item:
        if action == "increase":
            cart_item.quantity += 1
        elif action == "decrease":
            cart_item.quantity -= 1
            if cart_item.quantity == 0:
                db.session.delete(cart_item)
        db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(port=5004, debug=True)
