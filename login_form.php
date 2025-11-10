<?php
// login_form.php
session_start();
$error = $_SESSION['error'] ?? null;
$success = $_SESSION['success'] ?? null;
unset($_SESSION['error'], $_SESSION['success']);
?>
<!doctype html>
<html>
<head><meta charset="utf-8"><title>Login</title></head>
<body>
  <h2>Login</h2>

  <?php if ($error): ?>
    <div style="color: #a00; background:#fdd; padding:8px; margin-bottom:10px;"><?php echo htmlspecialchars($error); ?></div>
  <?php endif; ?>

  <?php if ($success): ?>
    <div style="color: #060; background:#dfd; padding:8px; margin-bottom:10px;"><?php echo htmlspecialchars($success); ?></div>
  <?php endif; ?>

  <form action="login.php" method="post">
    <label>Username<br><input name="username" required></label><br><br>
    <label>Password<br><input name="password" type="password" required></label><br><br>
    <button type="submit">Login</button>
  </form>

  <p>Don't have an account? <a href="register_form.php">Register here</a></p>
</body>
</html>
