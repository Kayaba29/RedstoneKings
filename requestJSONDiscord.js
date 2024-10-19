// Eine Anfrage an die JSON-Datei senden
fetch("https://discord.com/api/guilds/644136856526782484/widget.json")
  .then(response => response.json())
  .then(data => {
    // Hier kannst du die Daten verwenden
    console.log(data); // Gibt die Daten in der Konsole aus
  })
  .catch(error => {
    console.error("Fehler beim Abrufen der Discord-Widget-Daten: " + error);
  });
