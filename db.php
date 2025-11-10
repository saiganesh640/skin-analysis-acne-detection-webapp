<?php
// db.php — database connection for XAMPP (default settings)

// Database credentials
$host = 'localhost';
$user = 'root';
$pass = '';          // <-- leave empty for XAMPP default
$db   = 'quiz_app';
$port = 3306;

// Create connection using MySQLi
$mysqli = new mysqli($host, $user, $pass, $db, $port);

// Check connection
if ($mysqli->connect_errno) {
    die("❌ Database connection failed: " . $mysqli->connect_error);
} else {
    // Optional message for testing
    // echo "✅ Database connection successful!";
}

// You can now use $mysqli in your other PHP files (register.php, login.php, etc.)
?>
