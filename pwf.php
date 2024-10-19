<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Benutzer-E-Mail-Adresse aus dem Formular abrufen
    $email = $_POST["email"];

    // Generiere einen zufälligen Zurücksetzungscode (hier als Beispiel)
    $resetCode = bin2hex(random_bytes(16)); // Dies erstellt einen 32-stelligen hexadezimalen Code

    // Speichern Sie den Zurücksetzungscode in Ihrer Datenbank (hier als Beispiel nicht implementiert)

    // Senden Sie eine E-Mail mit dem Zurücksetzungslink
    $subject = "Passwort zurücksetzen";
    $message = "Um Ihr Passwort zurückzusetzen, klicken Sie auf folgenden Link: https://www.example.com/reset_password.php?code=$resetCode";
    $headers = "From: webmaster@example.com";

    // Verwenden Sie die PHP mail() Funktion oder eine E-Mail-Bibliothek, um die E-Mail zu senden
    $mailSent = mail($email, $subject, $message, $headers);

    if ($mailSent) {
        echo "Eine E-Mail zum Zurücksetzen Ihres Passworts wurde an $email gesendet. Überprüfen Sie Ihren Posteingang.";
    } else {
        echo "Fehler beim Senden der E-Mail. Bitte versuchen Sie es später erneut.";
    }
}
?>
