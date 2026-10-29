# Testbericht – EcomFabrik Instagram Skills v2

Stand: 28.10.2026

## Automatisch ausgeführte Prüfungen (GitHub Actions)

- Erwartete neun eigenständige Skill-Verzeichnisse vorhanden.
- YAML-Frontmatter mit passendem Skill-Namen und kurzer Beschreibung.
- Interne referenzierte Dateien vorhanden.
- ZIP-Roundtrip für neun Skills: jede einzeln in einer ZIP mit richtigem obersten Ordner, nach dem Entpacken mit SKILL.md.
- Drei bewusst defekte Testkopien müssen vom Validator abgelehnt werden: fehlende Referenz, falscher Name, fehlender Skill.
- Positivtest: unveränderte Kopie besteht den Validator.

Die GitHub-Action zeigt den tatsächlich ausgeführten Status. Wenn die Tests fehlschlagen, ist die Änderung nicht als technisch bestanden zu bewerten.

## Nicht automatisch getestet

- Upload in claude.ai, Auswahl durch Claude oder Codex, Qualität realer Modellantworten.
- Plattformfunktionen eines konkreten Instagram-Kontos.
- Tatsächliche Bild-, Audio-, Musiklizenz- oder Rechtsprüfung.
- Ob ein finales Markenprofil in einem anderen Chat dauerhaft verfügbar ist.

Diese offenen Tests müssen in Claude/Codex mit [ACCEPTANCE.md](ACCEPTANCE.md) ausgeführt werden. Die dokumentierten 14 Szenarien sind **Testpläne**, keine Behauptung bereits erfolgreicher Modellläufe.

## Beobachtete Korrekturen während der Prüfung

- ZIP-Struktur wird jetzt automatisch erstellt, entpackt und überprüft, statt nur beschrieben zu werden.
- Der Validator wird mit absichtlich beschädigten Testdateien getestet (Negativtests).
- GitHub-Action nutzt checkout@v5 statt der älteren Node-20-Version.
- Die veraltete Instagram-Handle-Angabe in README und das Changelog-Datum wurden korrigiert.
