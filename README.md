
# Adventskalender Gewinnzahlen Checker

Ein Python-Skript, um die Gewinnzahlen eines Adventskalenders zu überprüfen. Das Skript kann entweder den aktuellen Tag oder alle Tage (1–24) durchsuchen und gibt aus, ob eine bestimmte Gewinnnummer gewonnen hat.

## Funktionen

- **Abrufen von Gewinnzahlen**: Die Gewinnzahlen werden von der Webseite des Adventskalenders geladen.
- **Tägliche oder komplette Prüfung**: Überprüft entweder nur den aktuellen Tag oder alle Tage (1–24).
- **Ergebnis anzeigen**: Gibt an, ob und an welchen Tagen die angegebene Gewinnnummer gewonnen hat.

## Voraussetzungen

Stelle sicher, dass Python (Version 3.6 oder höher) auf deinem System installiert ist. Zudem müssen die folgenden Bibliotheken installiert sein:

```bash
pip install requests beautifulsoup4
```

## Nutzung

1. **Skript ausführen**:
   - Lade die Dateien aus diesem Repository herunter.
   - Führe das Skript aus dem Terminal oder der Kommandozeile aus.

2. **Argumente**:
   - **Gewinnnummer**: Die zu überprüfende Gewinnnummer (erforderlich).
   - **Option `--alle_tage`**: Optional, um alle Tage (1–24) zu überprüfen.

### Beispiele

- **Nur den aktuellen Tag prüfen**:
   ```bash
   python checker.py 4550
   ```

- **Alle Tage prüfen**:
   ```bash
   python checker.py 4550 --alle_tage
   ```

## Funktionsweise

Das Skript:

1. Ruft die Gewinnzahlen von der Webseite des Adventskalenders ab.
2. Analysiert die HTML-Seite und extrahiert die Gewinnzahlen aus den entsprechenden HTML-Attributen.
3. Überprüft, ob die angegebene Gewinnnummer in den Gewinnzahlen enthalten ist.
4. Gibt das Ergebnis in der Konsole aus.

## Fehlerbehandlung

- **Keine Verbindung zur Webseite**: Falls die Webseite nicht erreichbar ist, wird eine entsprechende Fehlermeldung angezeigt.
- **Keine Gewinnzahlen gefunden**: Wenn die Struktur der Webseite unerwartet ist, wird darauf hingewiesen, dass Anpassungen am Skript erforderlich sein könnten.

## Hinweis

Das Skript basiert auf der aktuellen Struktur der Webseite des Adventskalenders. Sollten sich Änderungen an der Webseite ergeben, kann eine Anpassung des HTML-Selektors in der Funktion `get_gewinnzahlen` erforderlich sein.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen findest du in der [LICENSE](LICENSE)-Datei.

---

Falls du Fragen oder Verbesserungsvorschläge hast, erstelle gerne ein Issue oder einen Pull Request. Viel Erfolg beim Überprüfen deiner Gewinnnummer! 😊
