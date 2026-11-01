<?php
require_once __DIR__ . '/config.php';
if (!empty($_SESSION['user_id'])) { header('Location: index.php'); exit; }
$error = '';
$email = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = trim($_POST['email'] ?? '');
    $password = $_POST['password'] ?? '';
    if (!preg_match('/^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/', $email)) {
        $error = 'Enter a valid email address.';
    } else {
        $stmt = $pdo->prepare('SELECT id, name, email, password_hash FROM users WHERE email = ?');
        $stmt->execute([$email]);
        $user = $stmt->fetch();
        if ($user && password_verify($password, $user['password_hash'])) {
            session_regenerate_id(true);
            $_SESSION['user_id'] = $user['id'];
            $_SESSION['user_name'] = $user['name'];
            header('Location: index.php'); exit;
        }
        $error = 'Email or password is incorrect.';
    }
}
function h($v) { return htmlspecialchars((string)$v, ENT_QUOTES, 'UTF-8'); }
?>
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Login | COVID-19 Info</title><link rel="stylesheet" href="style.css"></head>
<body class="auth-body"><a class="back-link" href="index.php">← Back to home</a><main class="auth-card"><p class="eyebrow">WELCOME BACK</p><h1>Log in</h1>
<?php if (isset($_GET['registered'])): ?><div class="alert success">Registration successful. You can now log in.</div><?php endif; ?>
<?php if ($error): ?><div class="alert error"><?= h($error) ?></div><?php endif; ?>
<form method="post" class="auth-form"><label for="email">Email address</label><input id="email" name="email" type="email" value="<?= h($email) ?>" required autocomplete="email"><label for="password">Password</label><input id="password" name="password" type="password" required autocomplete="current-password"><button class="primary-button" type="submit">Log in</button></form>
<p class="auth-bottom">New here? <a href="register.php">Create an account</a></p></main></body></html>
