# COVID-19 Information Website — Mini Project

A simple dynamic website for COVID-19 information using HTML, CSS, JavaScript, PHP and MySQL.

## Features
- COVID-19 information page with prevention guidance and symptoms
- User registration and login (passwords are hashed)
- User comments stored in MySQL
- Server-side regular-expression validation for registration and comments
- Basic responsive design

> This is an educational mini project. COVID-19 guidance can change; replace the sample informational content with current guidance from your local public-health authority before publishing. This project is not a medical advice service.

## Requirements
- PHP 8+
- MySQL 5.7+ / MySQL 8+
- XAMPP, WAMP, or another PHP/MySQL environment

## Setup using XAMPP
1. Copy the `covid19_info_website` folder into `C:\xampp\htdocs\`.
2. Start **Apache** and **MySQL** in XAMPP Control Panel.
3. Open phpMyAdmin at `http://localhost/phpmyadmin`.
4. Import `database.sql`, or open it and run its SQL commands.
5. Check `config.php`. The default XAMPP settings are host `localhost`, user `root`, empty password, database `covid19_info`.
6. Visit `http://localhost/covid19_info_website/`.

## Regular-expression test cases
Open `regex_test_cases.md` for the validation patterns and examples.

## Pages
- `index.php` — information and comments
- `register.php` — account registration
- `login.php` — sign in
- `logout.php` — sign out
- `config.php` — database connection
- `database.sql` — schema
