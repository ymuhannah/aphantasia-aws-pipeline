<?php
ini_set('log_errors', 1);
ini_set('error_log', '/var/log/php-error.log');
error_reporting(E_ALL);

$data_array = json_decode(file_get_contents("php://input"), true);
error_log("Data array received: " . json_encode($data_array));

try {
    $db_host = 'final-project-database001.cv7jvzss5xbo.us-east-1.rds.amazonaws.com';
    $db_user = 'username';
    $db_password = 'password';
    $db_name = 'finaldata001';

    $pdo = new mysqli($db_host, $db_user, $db_password, $db_name);

    if ($pdo->connect_error) {
        die("Connection failed: " . $pdo->connect_error);
    }

    if ($data_array) {
        error_log("Data received: " . json_encode($data_array));

        $email = isset($data_array['EmailAddress']) ? $data_array['EmailAddress'] : null;
        $futureContact = isset($data_array['FutureContactConsent']) ? $data_array['FutureContactConsent'] : false;
        $age = isset($data_array['Age']) ? $data_array['Age'] : null;
        $sex = isset($data_array['Sex']) ? $data_array['Sex'] : null;
        $ethnicity = isset($data_array['Ethnicity']) ? $data_array['Ethnicity'] : null;
        $race = isset($data_array['Race']) ? $data_array['Race'] : null;
        $idealParticipation = isset($data_array['IdealParticipation']) ? $data_array['IdealParticipation'] : null;
        $attentionCheckTask = isset($data_array['AttentionCheckTask']) ? $data_array['AttentionCheckTask'] : null;

        // Log demographic information
        error_log("Demographic information - Email: $email, Age: $age, Sex: $sex, Ethnicity: $ethnicity, Race: $race, FutureContact: $futureContact");

        // Inserting/Updating EmailAddressInput table
        $result = $pdo->query("INSERT INTO EmailAddressInput (EmailAddress, FutureContactConsent) VALUES ('$email', '$futureContact') ON DUPLICATE KEY UPDATE FutureContactConsent='$futureContact'");
        if (!$result) {
            error_log("Error in EmailAddressInput query: " . $pdo->error);
        }

        // Inserting/Updating Demographics table
        $result = $pdo->query("INSERT INTO Demographics (EmailAddress, Age, Sex, Ethnicity, Race) VALUES ('$email', '$age', '$sex', '$ethnicity', '$race') ON DUPLICATE KEY UPDATE Age='$age', Sex='$sex', Ethnicity='$ethnicity', Race='$race'");
        if (!$result) {
            error_log("Error in Demographics query: " . $pdo->error);
        }

        // VVIQ data
        $vviq_q1 = isset($data_array['VVIQ_Q1']) ? $data_array['VVIQ_Q1'] : null;
        $vviq_q2 = isset($data_array['VVIQ_Q2']) ? $data_array['VVIQ_Q2'] : null;
        $vviq_q3 = isset($data_array['VVIQ_Q3']) ? $data_array['VVIQ_Q3'] : null;
        $vviq_q4 = isset($data_array['VVIQ_Q4']) ? $data_array['VVIQ_Q4'] : null;
        $vviq_q5 = isset($data_array['VVIQ_Q5']) ? $data_array['VVIQ_Q5'] : null;
        $vviq_q6 = isset($data_array['VVIQ_Q6']) ? $data_array['VVIQ_Q6'] : null;
        $vviq_q7 = isset($data_array['VVIQ_Q7']) ? $data_array['VVIQ_Q7'] : null;
        $vviq_q8 = isset($data_array['VVIQ_Q8']) ? $data_array['VVIQ_Q8'] : null;
        $vviq_q9 = isset($data_array['VVIQ_Q9']) ? $data_array['VVIQ_Q9'] : null;
        $vviq_q10 = isset($data_array['VVIQ_Q10']) ? $data_array['VVIQ_Q10'] : null;
        $vviq_q11 = isset($data_array['VVIQ_Q11']) ? $data_array['VVIQ_Q11'] : null;
        $vviq_q12 = isset($data_array['VVIQ_Q12']) ? $data_array['VVIQ_Q12'] : null;
        $vviq_q13 = isset($data_array['VVIQ_Q13']) ? $data_array['VVIQ_Q13'] : null;
        $vviq_q14 = isset($data_array['VVIQ_Q14']) ? $data_array['VVIQ_Q14'] : null;
        $vviq_q15 = isset($data_array['VVIQ_Q15']) ? $data_array['VVIQ_Q15'] : null;
        $vviq_q16 = isset($data_array['VVIQ_Q16']) ? $data_array['VVIQ_Q16'] : null;

        // Log VVIQ data
        error_log("VVIQ data - Email: $email, Q1: $vviq_q1, Q2: $vviq_q2, Q3: $vviq_q3, Q4: $vviq_q4, Q5: $vviq_q5, Q6: $vviq_q6, Q7: $vviq_q7, Q8: $vviq_q8, Q9: $vviq_q9, Q10: $vviq_q10, Q11: $vviq_q11, Q12: $vviq_q12, Q13: $vviq_q13, Q14: $vviq_q14, Q15: $vviq_q15, Q16: $vviq_q16");

        $result = $pdo->query("
            INSERT INTO VVIQResponses (EmailAddress, VVIQ_Q1, VVIQ_Q2, VVIQ_Q3, VVIQ_Q4, VVIQ_Q5, VVIQ_Q6, VVIQ_Q7, VVIQ_Q8, VVIQ_Q9, VVIQ_Q10, VVIQ_Q11, VVIQ_Q12, VVIQ_Q13, VVIQ_Q14, VVIQ_Q15, VVIQ_Q16)
            VALUES ('$email', '$vviq_q1', '$vviq_q2', '$vviq_q3', '$vviq_q4', '$vviq_q5', '$vviq_q6', '$vviq_q7', '$vviq_q8', '$vviq_q9', '$vviq_q10', '$vviq_q11', '$vviq_q12', '$vviq_q13', '$vviq_q14', '$vviq_q15', '$vviq_q16')
            ON DUPLICATE KEY UPDATE
            VVIQ_Q1='$vviq_q1', VVIQ_Q2='$vviq_q2', VVIQ_Q3='$vviq_q3', VVIQ_Q4='$vviq_q4', VVIQ_Q5='$vviq_q5', VVIQ_Q6='$vviq_q6', VVIQ_Q7='$vviq_q7', VVIQ_Q8='$vviq_q8', VVIQ_Q9='$vviq_q9', VVIQ_Q10='$vviq_q10', VVIQ_Q11='$vviq_q11', VVIQ_Q12='$vviq_q12', VVIQ_Q13='$vviq_q13', VVIQ_Q14='$vviq_q14', VVIQ_Q15='$vviq_q15', VVIQ_Q16='$vviq_q16'
        ");
        if (!$result) {
            error_log("Error in VVIQResponses query: " . $pdo->error);
        }

        // Attention check data
        $result = $pdo->query("
            INSERT INTO AttentionCheck (EmailAddress, IdealParticipation, AttentionCheckTask)
            VALUES ('$email', '$idealParticipation', '$attentionCheckTask')
            ON DUPLICATE KEY UPDATE
            IdealParticipation='$idealParticipation', AttentionCheckTask='$attentionCheckTask'
        ");
        if (!$result) {
            error_log("Error in AttentionCheck query: " . $pdo->error);
        }

        error_log("Data inserted/updated successfully.");
    }

    echo "Data saved successfully.";
} catch (Exception $e) {
    error_log('Error: ' . $e->getMessage());
    echo "Failed to save data.";
}
?>
