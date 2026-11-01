<?php
require_once __DIR__ . '/config.php';

$errors = [];
$success = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['submit_comment'])) {
    if (empty($_SESSION['user_id'])) {
        $errors[] = 'Please log in before posting a comment.';
    } else {
        $comment = trim($_POST['comment'] ?? '');
        // Allow letters, digits, whitespace and common punctuation; 3–1000 characters.
        if (!preg_match("/^[\p{L}\p{N}\s.,!?;:'\"()\-]{3,1000}$/u", $comment)) {
            $errors[] = 'Comment must be 3–1000 characters and use ordinary text punctuation.';
        } else {
            $stmt = $pdo->prepare('INSERT INTO comments (user_id, comment_text) VALUES (?, ?)');
            $stmt->execute([$_SESSION['user_id'], $comment]);
            $success = 'Your comment was added.';
        }
    }
}
$stmt = $pdo->query(
    'SELECT comments.comment_text, comments.created_at, users.name
     FROM comments JOIN users ON comments.user_id = users.id
     ORDER BY comments.created_at DESC LIMIT 30'
);
$comments = $stmt->fetchAll();
function h($value) { return htmlspecialchars((string)$value, ENT_QUOTES, 'UTF-8'); }
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>COVID-19 Information Portal</title>
  <link rel="stylesheet" href="style.css">
  <script defer src="script.js"></script>
</head>
<body>
<header class="topbar">
  <a class="brand" href="index.php">COVID-19 Info</a>
  <nav>
    <a href="#about">About</a><a href="#prevention">Prevention</a><a href="#comments">Comments</a>
    <?php if (!empty($_SESSION['user_id'])): ?>
      <span class="welcome">Hi, <?= h($_SESSION['user_name']) ?></span>
      <a class="nav-button" href="logout.php">Logout</a>
    <?php else: ?>
      <a href="login.php">Login</a><a class="nav-button" href="register.php">Register</a>
    <?php endif; ?>
  </nav>
</header>
<main>
  <section class="hero">
    <div class="hero-copy">
      <p class="eyebrow">INFORMATION • AWARENESS • PREVENTION</p>
      <h1>Stay informed.<br><span>Stay protected.</span></h1>
      <p>Learn about COVID-19 symptoms, prevention, and responsible steps to take when you feel unwell.</p>
      <a class="primary-button" href="#prevention">Explore prevention</a>
    </div>
    <div class="hero-art" aria-label="Illustration of a medical shield">
      <div class="shield">+</div><div class="orb orb-one"></div><div class="orb orb-two"></div>
    </div>
  </section>

  <section id="about" class="section">
    <p class="eyebrow">THE BASICS</p><h2>What is COVID-19?</h2>
    <p class="intro">COVID-19 is an infectious disease caused by the SARS-CoV-2 virus. Symptoms and severity vary. Follow current advice from trusted public-health authorities for guidance relevant to your area.</p>
    <div class="cards">
      <article class="info-card"><div class="card-icon">♡</div><h3>Common symptoms</h3><p>Possible symptoms include fever, cough, sore throat, fatigue, and changes in taste or smell.</p></article>
      <article class="info-card"><div class="card-icon">✚</div><h3>When to seek help</h3><p>Seek urgent medical care for severe breathing difficulty, persistent chest pain, confusion, or other emergency symptoms.</p></article>
      <article class="info-card"><div class="card-icon">✓</div><h3>Reliable information</h3><p>Use official health authorities for current recommendations, vaccination information, and local updates.</p></article>
    </div>
  </section>

  <section id="prevention" class="section prevention">
    <p class="eyebrow">PRACTICAL STEPS</p><h2>Help reduce the spread</h2>
    <div class="steps">
      <div><span>01</span><section><h3>Improve ventilation</h3><p>Prefer well-ventilated spaces when possible.</p></section></div>
      <div><span>02</span><section><h3>Stay home when unwell</h3><p>Reduce contact with others and follow local health advice.</p></section></div>
      <div><span>03</span><section><h3>Practice hygiene</h3><p>Wash hands regularly and cover coughs and sneezes.</p></section></div>
      <div><span>04</span><section><h3>Check trusted sources</h3><p>Recommendations can change as evidence and local conditions change.</p></section></div>
    </div>
    <p class="notice">Educational information only; not a substitute for professional medical advice.</p>
  </section>

  <section id="comments" class="section">
    <p class="eyebrow">COMMUNITY</p><h2>Questions & comments</h2>
    <p class="intro">Share feedback about this information portal. Do not post private medical or personal information.</p>
    <?php foreach ($errors as $error): ?><div class="alert error"><?= h($error) ?></div><?php endforeach; ?>
    <?php if ($success): ?><div class="alert success"><?= h($success) ?></div><?php endif; ?>
    <?php if (!empty($_SESSION['user_id'])): ?>
      <form method="post" class="comment-form" id="commentForm">
        <label for="comment">Your comment</label>
        <textarea id="comment" name="comment" minlength="3" maxlength="1000" required placeholder="Write a comment (3–1000 characters)"></textarea>
        <small id="commentCount">0 / 1000 characters</small>
        <button class="primary-button" type="submit" name="submit_comment">Post comment</button>
      </form>
    <?php else: ?>
      <div class="login-prompt">Please <a href="login.php">log in</a> to post a comment.</div>
    <?php endif; ?>
    <div class="comment-list">
      <?php if (!$comments): ?><p class="muted">No comments yet. Be the first to share feedback after logging in.</p><?php endif; ?>
      <?php foreach ($comments as $item): ?>
        <article class="comment"><div class="comment-heading"><strong><?= h($item['name']) ?></strong><time><?= h($item['created_at']) ?></time></div><p><?= nl2br(h($item['comment_text'])) ?></p></article>
      <?php endforeach; ?>
    </div>
  </section>
</main>
<footer><span>COVID-19 Information Portal</span><span>Educational mini project • PHP & MySQL</span></footer>
</body>
</html>
