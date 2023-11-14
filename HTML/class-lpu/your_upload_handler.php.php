<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload Handler</title>
</head>
<body>
    <h1>File Upload Results</h1>
    <?php
    if ($_SERVER["REQUEST_METHOD"] === "POST") {
        // Check if a file was uploaded
        if (isset($_FILES["file"])) {
            $file = $_FILES["file"];
            $uploadDir = "uploads/"; // Create an "uploads" directory to store uploaded files

            // Check for file upload errors
            if ($file["error"] === 0) {
                $fileName = $uploadDir . $file["name"];
                if (move_uploaded_file($file["tmp_name"], $fileName)) {
                    echo "File uploaded successfully.<br>";
                } else {
                    echo "Error uploading the file.<br>";
                }
            } else {
                echo "Error: " . $file["error
