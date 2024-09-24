# Comrades Online E commerce Application
# Bora Chakula

**Bora Chakula** is an online meal ordering application that allows university students to conveniently order meals from their favorite eateries. The application aims to streamline the ordering process, enabling students to avoid long queues and enjoy a hassle-free dining experience.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- User registration and authentication
- Browse and search for meals
- Add meals to cart
- Secure payment processing via M-Pesa
- View order history
- Admin dashboard to manage meals and orders

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: PostgreSQL (or any other database of your choice)
- **Payment Integration**: M-Pesa API
- **Version Control**: Git

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/steve-ongera/Comrades-Online-E-commerce-Application.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd bora-chakula
   ```

3. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up your database**:
   - Update the database settings in `settings.py`.
   - Run migrations:
     ```bash
     python manage.py migrate
     ```

6. **Create a superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

8. **Open your browser and navigate to** `http://127.0.0.1:8000/` to access the application.

## Usage

- **User Registration**: Sign up to create an account.
- **Login**: Access your account to browse meals and place orders.
- **Order Meals**: Add your desired meals to the cart and proceed to checkout.
- **Payment**: Choose M-Pesa as your payment method and enter your phone number to complete the transaction.
- **Order History**: View your past orders in your account dashboard.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create your feature branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add some feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **Stephen Ongera** 
  phone : +254112284093
  Email: gadafisteve001@gmail.com 
  GitHub: https://github.com/steve-ongera
