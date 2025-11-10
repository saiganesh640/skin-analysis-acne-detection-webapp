<?php
session_start();
require_once 'db.php';

// Handle POST submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $fullname = trim($_POST['fullname'] ?? '');
    $email    = trim($_POST['email'] ?? '');
    $username = trim($_POST['username'] ?? '');
    $password = $_POST['password'] ?? '';

    // Validation
    if (!$fullname || !$email || !$username || !$password) {
        $_SESSION['error'] = "Please fill all fields.";
        header('Location: register.php'); exit;
    }
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $_SESSION['error'] = "Invalid email address.";
        header('Location: register.php'); exit;
    }

    // Check duplicates
    $stmt = $mysqli->prepare("SELECT id FROM users4 WHERE email = ? OR username = ? LIMIT 1");
    if (!$stmt) {
        $_SESSION['error'] = "Database error: " . $mysqli->error;
        header('Location: register.php'); exit;
    }
    $stmt->bind_param('ss', $email, $username);
    $stmt->execute();
    $stmt->store_result();
    if ($stmt->num_rows > 0) {
        $_SESSION['error'] = "Email or username already taken.";
        $stmt->close();
        header('Location: register.php'); exit;
    }
    $stmt->close();

    // Insert
    $hash = password_hash($password, PASSWORD_DEFAULT);
    $ins = $mysqli->prepare("INSERT INTO users4 (fullname, email, username, password) VALUES (?, ?, ?, ?)");
    if (!$ins) {
        $_SESSION['error'] = "Database error: " . $mysqli->error;
        header('Location: register.php'); exit;
    }
    $ins->bind_param('ssss', $fullname, $email, $username, $hash);
    if ($ins->execute()) {
        $_SESSION['success'] = "Registration successful! Please login.";
        $ins->close();
        header('Location: index.php'); exit;
    } else {
        $_SESSION['error'] = "Registration failed: " . $mysqli->error;
        $ins->close();
        header('Location: register.php'); exit;
    }
}

// show any flash messages (if redirected back)
$error = $_SESSION['error'] ?? null;
$success = $_SESSION['success'] ?? null;
unset($_SESSION['error'], $_SESSION['success']);
?>
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Register | Skin Analyzer</title>
  <link rel="stylesheet" href="style.css" />
  <link href="https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css" rel="stylesheet" />
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');
    *{margin:0;padding:0;box-sizing:border-box;font-family:'Poppins',sans-serif}
    body{min-height:100vh;display:flex;justify-content:center;align-items:center;background:url('https://www.news-medical.net/image-handler/picture/2019/6/shutterstock_1083859292.jpg') no-repeat center center fixed;background-size:cover;position:relative}
    body::before{content:'';position:absolute;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.4);z-index:0}
    .wrapper{position:relative;z-index:1;width:420px;background:rgba(255,255,255,0.15);border:2px solid rgba(255,255,255,0.2);backdrop-filter:blur(10px);border-radius:20px;padding:40px;color:#fff}
    .wrapper h1{text-align:center;margin-bottom:30px}
    .input-box{position:relative;width:100%;height:50px;margin:30px 0}
    .input-box input{width:100%;height:100%;background:transparent;border:2px solid rgba(255,255,255,0.3);border-radius:40px;color:#fff;padding:0 45px 0 20px;outline:none}
    .input-box input::placeholder{color:#ddd}
    .input-box i{position:absolute;right:20px;top:50%;transform:translateY(-50%);font-size:20px;color:#fff}
    .btn{width:100%;height:45px;background:#fff;border:none;border-radius:40px;cursor:pointer;font-weight:600;color:#333}
    .btn:hover{background:#f0f0f0}
    .register-link{text-align:center;font-size:14px;margin-top:20px}
    .register-link a{color:#fff;text-decoration:underline}
    .flash { width:420px;margin:10px auto;padding:10px 14px;border-radius:8px;text-align:center;font-weight:600; }
    .flash.error { background:#fceaea;color:#900;border:1px solid #f2c7c7; }
    .flash.success { background:#eafce9;color:#084;border:1px solid #c7f2d0; }
  </style>
</head>

<body>
  <?php if ($error): ?>
    <div class="flash error"><?php echo htmlspecialchars($error); ?></div>
  <?php endif; ?>
  <?php if ($success): ?>
    <div class="flash success"><?php echo htmlspecialchars($success); ?></div>
  <?php endif; ?>

  <div class="wrapper">
    <form action="register.php" method="POST">
      <h1>Register</h1>

      <div class="input-box">
        <input type="text" name="fullname" placeholder="Full Name" required />
        <i class='bx bx-user'></i>
      </div>

      <div class="input-box">
        <input type="email" name="email" placeholder="Email" required />
        <i class='bx bx-envelope'></i>
      </div>

      <div class="input-box">
        <input type="text" name="username" placeholder="Username" required />
        <i class='bx bx-id-card'></i>
      </div>

      <div class="input-box">
        <input type="password" name="password" placeholder="Password" required />
        <i class='bx bx-lock'></i>
      </div>

      <button type="submit" class="btn">Register</button>

      <div class="register-link">
        <p>Already have an account? <a href="index.php">Login</a></p>
      </div>
    </form>
  </div>
</body>

</html>
