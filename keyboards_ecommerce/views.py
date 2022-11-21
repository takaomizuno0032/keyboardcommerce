from sys import path_hooks
from xml.etree.ElementTree import Comment
from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from datetime import datetime
from . import db
from .forms import CheckoutForm
from sqlalchemy import or_

from keyboards_ecommerce.models import Category, Keyboard, Order

bp = Blueprint('main', __name__)

# top page


@bp.route('/')
def index():
    keyboards = Keyboard.query.order_by(Keyboard.id).all()
    categories = Category.query.order_by(Category.id).all()

    return render_template('index.html', keyboards=keyboards, categories=categories, display_type="All")

# keyboard detail page


@bp.route('/keyboards/<int:keyboardid>/')
def keyboard_detail(keyboardid):
    keyboard = Keyboard.query.get(keyboardid)
    category = Category.query.get(keyboard.category_id)

    return render_template('detail.html', keyboard=keyboard, category=category)

# search keyboard by category


@bp.route('/categories/<int:categoryid>/')
def keybord_categorised(categoryid):

    keyboards = Keyboard.query.filter(
        Keyboard.category_id == categoryid)

    selected_category = Category.query.get(categoryid)
    return render_template('category.html', keyboards=keyboards, category=selected_category)

# search keyboards by words


@bp.route('/search/', methods=['POST'])
def search():
    search_word = request.form["searchWord"]
    formated_search_word = "%{}%".format(search_word)
    # get keyboards related with search word
    keyboards = Keyboard.query.filter(or_(Keyboard.name.like(formated_search_word), Keyboard.conective.like(
        formated_search_word), Keyboard.description.like(formated_search_word)))
    categories = Category.query.order_by(Category.id).all()

    return render_template('index.html', keyboards=keyboards, categories=categories, display_type="Result by {}".format(search_word))

# order page


@bp.route('/order/', methods=['POST', 'GET'])
def order():
    keyboard_id = request.args.get('keyboard_id')

    # retrieve order if there is one
    if 'order_id' in session.keys():
        order = Order.query.get(session['order_id'])
        # order will be None if order_id stale
    else:
        # there is no order
        order = None

    # create new order if needed
    if order is None:
        order = Order(status=False, firstname='', lastname='',
                      email='', address='', date=datetime.now(), totalcost=0)
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            print('failed at creating a new order')
            order = None

      # calcultate totalprice
    totalprice = 0
    if order is not None:
        for keyboard in order.keyboards:
            totalprice = totalprice + keyboard.price

    # are we adding an item?
    if keyboard_id is not None and order is not None:
        keyboard = Keyboard.query.get(keyboard_id)
        if keyboard not in order.keyboards:
            try:
                order.keyboards.append(keyboard)
                db.session.commit()
            except:
                return 'There was an issue adding the item to your basket'
            return redirect(url_for('main.order'))
        else:
            flash('This keyboard is already in basket', category='danger')
            return redirect(url_for('main.order'))

    return render_template('order.html', order=order, totalprice=totalprice)


# delete item from cart

@bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    id = request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        keyboard_to_delete = Keyboard.query.get(id)
        try:
            order.keyboards.remove(keyboard_to_delete)
            db.session.commit()
            return redirect(url_for('main.order'))
        except:
            return 'Problem deleting item from order'
    return redirect(url_for('main.order'))

# delete all items


@bp.route('/deleteorder')
def deleteorder():
    if 'order_id' in session:
        del session['order_id']
        flash('All items deleted', category="danger")
    return redirect(url_for('main.order'))

# complete order


@bp.route('/checkout/', methods=['POST', 'GET'])
def checkout():
    form = CheckoutForm()
    totalprice = 0
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        for keyboard in order.keyboards:
            totalprice = totalprice + keyboard.price

        if form.validate_on_submit():
            order.status = True
            order.firstname = form.firstname.data
            order.lastname = form.lastname.data
            order.email = form.email.data
            order.address = form.address.data
            totalcost = 0
            for keyboard in order.keyboards:
                totalcost = totalcost + keyboard.price
            order.totalcost = totalcost
            order.date = datetime.now()
            try:
                db.session.commit()
                del session['order_id']
                flash(
                    'Thank you! Products will be shipped within one week!', category="primary")

                return redirect(url_for('main.complete'))
            except:
                return 'There was an issue completing your order'
    return render_template('checkout.html', form=form, order=order, totalprice=totalprice)

# confirm page


@bp.route('/complete/')
def complete():
    return render_template('complete.html')
