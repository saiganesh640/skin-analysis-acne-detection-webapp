<?php
// login.php
session_start();
require_once 'db.php';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: login_form.php');
    exit;
}

$username = trim($_POST['username'] ?? '');
$password = $_POST['password'] ?? '';

if (!$username || !$password) {
    $_SESSION['error'] = "Please fill both username and password.";
    header('Location: login_form.php'); exit;
}

// Find user by username (you can also allow login by email if preferred)
$sql = "SELECT id, username, password FROM users4 WHERE username = ? LIMIT 1";
$stmt = $mysqli->prepare($sql);
$stmt->bind_param('s', $username);
$stmt->execute();
$result = $stmt->get_result();
$user = $result->fetch_assoc();
$stmt->close();

if (!$user) {
    $_SESSION['error'] = "Invalid credentials.";
    header('Location: login_form.php'); exit;
}

if (password_verify($password, $user['password'])) {
    // login success
    session_regenerate_id(true);
    $_SESSION['user_id'] = $user['id'];
    $_SESSION['username'] = $user['username'];
    // redirect to your app page
    header('Location: quiz.html'); exit;
} else {
    $_SESSION['error'] = "Invalid credentials.";
    header('Location: login_form.php'); exit;
}
