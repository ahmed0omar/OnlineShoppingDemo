# Online Shopping Demo

It is a django apis for some of Online Shopping web app that's handle (users, products, carts, and orders).
I is made with django rest framework , django web framework and JWt using python 3.8.

## How to install it?

- First Clone this repo

```bash
    git clone https://github.com/ahmed0omar/OnlineShoppingDemo
```

- Change into the project directory

```bash
    cd OnlineShoppingDemo
```

- Create a Virtualenv at the project directory

```bash
    virtualenv venv
```

- Activate the virtualenv

```bash
    venv\scripts\activate
```

- Install the project Dependencies

```bash
    pip install -r requirements.txt
```

- Modify `OnlineShoppingDemo/setting.py` with database settings, as following where I using `mysql DBME`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ShoppingDemo',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': ''
    }
}
```

- Create database
Run the following command in MySQL shell:

```sql
CREATE DATABASE `ShoppingDemo` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
```

Run the following commands in Terminal:

```bash
python manage.py makemigrations
python manage.py migrate
```  

- Create a superuser

```bash
    python manage.py createsuperuser
```

- Change the razorpay credentials in the settings file

- Spin Up The Django Developement Server

```bash
    python manage.py runserver
```

Now You Are all set and the server Is Running on the url <http://localhost:8000>

## project available apis

### user apis

- `auth/users/`(list and register users)
- `auth/users/me/`(show current user)
- `auth/users/set_password/` ( set new password)
- `auth/users/set_username/`( set new username)
- `auth/jwt/create/` (Jwt user login
- `auth/jwt/refresh/` (jwt refresh)
- `auth/jwt/verify/` (jwt verify)

### Store apis

- #### Product apis  :-

  - `store/products/`(list all product and add product in cass of is admin)
  - `store/products/product_pk/`(retrieve the product with specified product_pk and update its attributes in case of admin user)

- #### Cart apis :-

  - `store/carts/` ( list all carts in cass of the user is admin and retrieve current user cart, and create new cart for current user option)
  - `store/carts/cart_pk` ( retrieve the cart data for specified cart_pk and delete it option)
  - `store/carts/cart_pk/items` ( get the cart items for specified cart_pk and add product to it option)
  - `store/carts/cart_pk/items/item_pk` (update the specified (`item_pk`) item quantity or delete the item option )

- #### Order apis :-

  - `store/orders/` ( list all orders in cass of    admin user and retrieve current user orders,
    and create new order based on specified cart for current user)
  - `store/orders/order_pk` ( retrieve the order items and allow the admins to change the order status)
