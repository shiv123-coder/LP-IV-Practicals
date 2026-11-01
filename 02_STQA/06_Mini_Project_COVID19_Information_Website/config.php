<?php
// Update these values if your local MySQL configuration differs.
$DB_HOST = 'localhost';
$DB_NAME = 'covid19_info';
$DB_USER = 'root';
$DB_PASS = '1234';

try {
    $pdo = new PDO(
        "mysql:host={$DB_HOST};dbname={$DB_NAME};charset=utf8mb4",
        $DB_USER,
        $DB_PASS,
        [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES => false
        ]
    );
} catch (PDOException $e) {
    http_response_code(500);
    exit('Database connection failed. Check MySQL is running and config.php settings are correct.');
}
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}
