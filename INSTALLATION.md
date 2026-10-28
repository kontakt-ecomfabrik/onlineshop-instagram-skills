# Installation – EcomFabrik Instagram Skills (9 Skills)

Alle Skills liegen in eigenständigen Ordnern mit `SKILL.md` und lokalen `references/`. Du kannst nur die benötigten Skills installieren. Zur Nutzung von Claude/Codex brauchst du Zugang zum jeweiligen Dienst; Instagram-Anmeldung oder API ist **nicht** erforderlich.

## Claude im Browser oder Desktop

1. Im [Repository](https://github.com/kontakt-ecomfabrik/onlineshop-instagram-skills) **Code → Download ZIP** wählen und die Datei entpacken.
2. Gewünschten Ordner, etwa `ecom-brand-voice/`, **einzeln vollständig** zippen. In der ZIP muss ein oberster Ordner `ecom-brand-voice/` liegen, darin direkt `SKILL.md` und ggf. `references/`.
3. In Claude **Customize → Skills** öffnen und über **+ / Create skill / Upload a skill** die ZIP hochladen und aktivieren (UI-Bezeichnungen können sich ändern).
4. Für weitere Skills wiederholen. Für GitHub-Updates die ZIP erneut hochladen/ersetzen – **keine automatische Synchronisierung**.

Aktuelle Voraussetzungen: [Claude Help Center](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

## Claude Code – Benutzerinstallation

```bash
git clone https://github.com/kontakt-ecomfabrik/onlineshop-instagram-skills.git
mkdir -p ~/.claude/skills
cp -R onlineshop-instagram-skills/ecom-* ~/.claude/skills/
```

Für ein einzelnes Projekt nach `.claude/skills/` kopieren. Skills nach Umgebung automatisch wählen lassen oder explizit z. B. `/ecom-content-review` aufrufen.

## Codex – Benutzerinstallation

```bash
git clone https://github.com/kontakt-ecomfabrik/onlineshop-instagram-skills.git
mkdir -p ~/.agents/skills
cp -R onlineshop-instagram-skills/ecom-* ~/.agents/skills/
```

Für ein Projekt nach `.agents/skills/` kopieren. In Codex z. B. `$ecom-brand-voice` auswählen. Bei ausbleibender Aktualisierung Codex neu starten. [Offizielle Codex-Anleitung](https://learn.chatgpt.com/de-DE/docs/build-skills).

## Windows ohne Terminal

Die neun Ordner manuell nach `C:\Users\DEIN-NAME\.claude\skills\` (Claude Code) oder `C:\Users\DEIN-NAME\.agents\skills\` (Codex) kopieren. Fehlende Ordner anlegen.

## Kurztest

- `ecom-brand-voice`: „Entwickle zwei Instagram-Stimmen für meinen Shop ohne bisherige Captions. Kennzeichne Vorschläge als vorläufig.“
- `ecom-content-review`: „Prüfe nur den Text dieser Caption, ich habe kein Video hochgeladen. Erfinde keine Produktfakten: …“

Erwartung: Kein vorgetäuschter Zugriff auf Konto oder Medien, keine erfundenen Produktergebnisse, sinnvoller nutzbarer Text. Strukturprüfung für Entwickler: `python3 scripts/validate_skills.py`. Verhalten anhand [manueller Tests](tests/ACCEPTANCE.md) prüfen.

**ChatGPT-Hinweis:** Eine ZIP als Chat-Anhang ist nicht gleichbedeutend mit der Installation eines Skills. Skill-Auswahl und Einbindung unterscheiden sich je nach ChatGPT-Produkt bzw. Codex-Umgebung; keine allgemeine `@`-Aktivierung behaupten.

**Probleme:** Wird ein Skill nicht erkannt, Ordnerpfad/`SKILL.md` prüfen, Aktivierung im KI-Dienst bestätigen und Anwendung ggf. neu starten. Bei doppeltem ZIP-Ordner nur den inneren Ordner mit `SKILL.md` verwenden. Für Markenpassung ein bestätigtes `brand-voice.md` erneut bereitstellen; die Skills speichern es nicht dauerhaft.
