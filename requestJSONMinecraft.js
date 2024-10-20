// Eine Anfrage an die JSON-Datei senden
fetch("c:\Users\Kayaba92\Desktop\Tests1\HTML test\requestJSONDiscord.js")
  .then(response => response.json())
  .then(data => {
    // Hier kannst du die Daten verwenden
    console.log(data); // Gibt die Daten in der Konsole aus
  })
  .catch(error => {
    console.error("Fehler beim Abrufen der Minecraft-Widget-Daten: " + error);
  });
