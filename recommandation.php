<?php
// Get data from quiz form
$acne = $_POST['acne'] ?? 'not specified';
$stress = $_POST['stress'] ?? 'not specified';
$sleep = $_POST['sleep'] ?? 'not specified';
$water = $_POST['water'] ?? 'not specified';

// Example: Suppose you already have $skinType from your ML model
// In a real setup, you might pass it via session or database
$skinType = $_POST['skinType'] ?? 'mild acne';

// Generate recommendations
$recommendations = [];

// --- Skin type recommendations ---
if ($skinType == "clear") {
    $recommendations[] = "Your skin looks great! Maintain it with a gentle cleanser and sunscreen daily.";
} elseif ($skinType == "mild acne") {
    $recommendations[] = "Use a salicylic acid-based cleanser and a non-comedogenic moisturizer.";
} elseif ($skinType == "moderate acne") {
    $recommendations[] = "Consider using benzoyl peroxide gel at night and avoid heavy creams.";
} else {
    $recommendations[] = "Consult a dermatologist for a personalized skincare plan.";
}

// --- Stress level impact ---
if ($stress == "high") {
    $recommendations[] = "High stress can worsen acne. Try meditation or 30 mins of light exercise daily.";
} elseif ($stress == "moderate") {
    $recommendations[] = "You’re managing okay — try to take breaks and rest your mind often.";
} else {
    $recommendations[] = "Low stress level — keep it up! Mindfulness is helping your skin too.";
}

// --- Sleep schedule ---
if ($sleep == "less5") {
    $recommendations[] = "Sleep less than 5 hours may cause dark circles and breakouts. Aim for 7–8 hours.";
} elseif ($sleep == "5to7") {
    $recommendations[] = "Good sleep duration — a bit more rest could help skin repair faster.";
} else {
    $recommendations[] = "Excellent sleep! Quality rest keeps your skin glowing.";
}

// --- Water intake ---
if ($water == "low") {
    $recommendations[] = "Increase water intake — hydration helps flush toxins and reduce acne.";
} elseif ($water == "moderate") {
    $recommendations[] = "You're doing well — keep sipping water regularly.";
} else {
    $recommendations[] = "Perfect hydration! Keep it up for soft, healthy skin.";
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Your Personalized Recommendation</title>
  <link rel="stylesheet" href="recommendation.css">
</head>

<body>
  <div class="wrapper">
    <h1>✨ Your Personalized Skin Report ✨</h1>

    <div class="summary">
      <h3>🧾 Summary</h3>
      <p><strong>Detected Skin Type:</strong> <?= htmlspecialchars($skinType) ?></p>
      <p><strong>Acne:</strong> <?= htmlspecialchars($acne) ?></p>
      <p><strong>Stress Level:</strong> <?= htmlspecialchars($stress) ?></p>
      <p><strong>Sleep:</strong> <?= htmlspecialchars($sleep) ?></p>
      <p><strong>Water Intake:</strong> <?= htmlspecialchars($water) ?></p>
    </div>

    <div class="recommendations">
      <h3>💡 Recommendations for You</h3>
      <ul>
        <?php foreach ($recommendations as $tip): ?>
          <li><?= htmlspecialchars($tip) ?></li>
        <?php endforeach; ?>
      </ul>
    </div>

    <div class="btn-container">
      <a href="quiz.html" class="btn">🧩 Retake Quiz</a>
      <a href="index.html" class="btn">🏠 Back to Home</a>
    </div>
  </div>
</body>
</html>
