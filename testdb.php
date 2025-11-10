<?php
// testdb.php — test the database connection
error_reporting(E_ALL);
ini_set('display_errors', 1);

require_once 'db.php';

if ($mysqli->connect_errno) {
    echo "❌ Database connection failed: " . $mysqli->connect_error;
} else {
    echo "✅ Database connected successfully!<br><br>";

    // show current database
    $res = $mysqli->query("SELECT DATABASE() AS dbname");
    $row = $res->fetch_assoc();
    echo "Current database: <b>" . htmlspecialchars($row['dbname']) . "</b><br><br>";

    // show all tables
    $tables = $mysqli->query("SHOW TABLES");
    echo "Tables found:<ul>";
    while ($table = $tables->fetch_array()) {
        echo "<li>" . htmlspecialchars($table[0]) . "</li>";
    }
    echo "</ul>";
}
?>
