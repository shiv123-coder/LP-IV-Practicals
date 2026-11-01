<?php
require_once __DIR__ . '/config.php';
if (!empty($_SESSION['user_id'])) { header('Location: index.php'); exit; }
$errors = [];
$name = '';
$email = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = trim($_POST['name'] ?? '');
    $email = trim($_POST['email'] ?? '');
    $password = $_POST['password'] ?? '';
    if (!preg_match("/^[\p{L}][\p{L}\s.'-]{1,59}$/u", $name)) {
        $errors[] = 'Name must be 2–60 characters and contain only letters, spaces, apostrophes, periods, or hyphens.';
    }
    if (!preg_match('/^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/', $email)) {
        $errors[] = 'Enter a valid email address.';
    }
    if (!preg_match('/^(?=.*[A-Za-z])(?=.*\d).{8,72}$/', $password)) {
        $errors[] = 'Password must be 8–72 characters and contain at least one letter and one digit.';
    }
    if (!$errors) {
        try {
            $stmt = $pdo->prepare('INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)');
            $stmt->execute([$name, $email, password_hash($password, PASSWORD_DEFAULT)]);
            header('Location: login.php?registered=1'); exit;
        } catch (PDOException $e) {
            $errors[] = 'This email may already be registered. Try logging in.';
        }
    }
}
function h($v) { return htmlspecialchars((string)$v, ENT_QUOTES, 'UTF-8'); }
?>
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Register | COVID-19 Info</title><link rel="stylesheet" href="style.css"></head>
<body class="auth-body"><a class="back-link" href="index.php">← Back to home</a><main class="auth-card"><p class="eyebrow">CREATE AN ACCOUNT</p><h1>Join the community</h1><p class="muted">Register to leave comments on the information portal.</p>
<?php foreach ($errors as $error): ?><div class="alert error"><?= h($error) ?></div><?php endforeach; ?>
<form method="post" class="auth-form">
<label for="name">Full name</label><input id="name" name="name" value="<?= h($name) ?>" required minlength="2" maxlength="60" autocomplete="name">
<label for="email">Email address</label><input id="email" name="email" type="email" value="<?= h($email) ?>" required maxlength="120" autocomplete="email">
<label for="password">Password</label><input id="password" name="password" type="password" required minlength="8" maxlength="72" autocomplete="new-password"><small>At least 8 characters, including a letter and a digit.</small>
<button class="primary-button" type="submit">Create account</button>
</form><p class="auth-bottom">Already registered? <a href="login.php">Log in</a></p></main></body></html>
