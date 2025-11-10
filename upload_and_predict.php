<?php
// upload_and_predict.php
// Receives an uploaded image (field name 'image') and optional 'quiz' JSON string.
// Forwards file + quiz to the Flask model at http://127.0.0.1:5000/predict and returns the JSON.

header('Content-Type: application/json; charset=utf-8');
error_reporting(E_ALL);
ini_set('display_errors', 1);

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    echo json_encode(['error' => 'Only POST allowed']);
    exit;
}

// Check file (either uploaded from file input or camera blob)
if (!isset($_FILES['image'])) {
    echo json_encode(['error' => 'No image uploaded (field name must be "image")']);
    exit;
}

$imageTmp = $_FILES['image']['tmp_name'];
if (!is_uploaded_file($imageTmp)) {
    echo json_encode(['error' => 'Upload failed or temporary file missing']);
    exit;
}

$mime = $_FILES['image']['type'] ?? 'image/jpeg';
$quizJson = $_POST['quiz'] ?? '{}';

// Build curl to Flask API
$curl = curl_init();
$cfile = new CURLFile($imageTmp, $mime, basename($_FILES['image']['name']));
$post = ['image' => $cfile, 'quiz' => $quizJson];

curl_setopt_array($curl, [
    CURLOPT_URL => 'http://127.0.0.1:5000/predict',
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST => true,
    CURLOPT_POSTFIELDS => $post,
    CURLOPT_TIMEOUT => 30
]);

$response = curl_exec($curl);
$err = curl_error($curl);
$httpcode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
curl_close($curl);

if ($err) {
    echo json_encode(['error' => 'Curl error: ' . $err]);
    exit;
}

// Forward Flask response
http_response_code($httpcode ?: 200);
echo $response;
