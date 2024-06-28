<?php
ini_set('log_errors', 1);
ini_set('error_log', '/var/log/php-error.log');
error_reporting(E_ALL);

error_log("Starting run_python_script.php execution.");

$script_path = '/var/www/html/generate_data.py'; // Absolute path to the script

try {
    $output = [];
    $return_var = 0;
    exec("python3 $script_path 2>&1", $output, $return_var);
    error_log("Exec return value: $return_var");
    error_log("Exec output: " . implode("\n", $output));
    
    if ($return_var !== 0) {
        error_log('Error executing Python script: ' . implode("\n", $output));
        echo "Error executing Python script.";
    } else {
        echo "Python script executed successfully.";
    }
} catch (Exception $e) {
    error_log('An error occurred: ' . $e->getMessage());
    echo "Error executing Python script.";
}
?>
