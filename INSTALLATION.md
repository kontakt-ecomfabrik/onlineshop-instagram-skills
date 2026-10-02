# Installation

Diese Anleitung beschreibt die Installation der sieben **EcomFabrik Instagram Skills** in Claude, Claude Code und Codex.

## Voraussetzungen

- Zugriff auf dieses GitHub-Repository
- Bei Claude: **Code execution and file creation** muss aktiviert sein
- Bei einem privaten Repository: Anmeldung bei GitHub beziehungsweise ein eingerichteter Git-Zugang

## 1. Claude im Browser oder in der Desktop-App

Claude lädt benutzerdefinierte Skills als einzelne ZIP-Dateien hoch.

### Schritt 1: Repository herunterladen

1. Klicke auf GitHub auf **Code**.
2. Wähle **Download ZIP**.
3. Entpacke das heruntergeladene Repository.

### Schritt 2: Gewünschten Skill vorbereiten

Wähle beispielsweise den Ordner `ecom-reel` und komprimiere **diesen vollständigen Ordner** als ZIP-Datei.

Die Struktur muss so aussehen:

```text
ecom-reel.zip
└── ecom-reel/
    ├── SKILL.md
    └── references/
```

Die Dateien dürfen nicht ohne den Hauptordner direkt in der ZIP liegen.

### Schritt 3: Skill hochladen

1. Öffne in Claude **Customize → Skills**.
2. Klicke auf **+** und anschließend auf **Create skill**.
3. Wähle **Upload a skill**.
4. Lade die ZIP-Datei hoch.
5. Aktiviere den Skill über den Schalter.

Wiederhole den Vorgang für alle Skills, die du verwenden möchtest.

Offizielle Anleitung: [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## 2. Claude Code

### Persönliche Installation für alle Projekte

```bash
git clone https://github.com/kontakt-ecomfabrik/onlineshop-instagram-skills.git
mkdir -p ~/.claude/skills
cp -R onlineshop-instagram-skills/ecom-* ~/.claude/skills/
```

Danach Claude Code neu starten. Die Skills können automatisch passend zur Aufgabe aktiviert oder direkt aufgerufen werden, zum Beispiel:

```text
/ecom-reel
/ecom-carousel
/ecom-caption
```

### Installation nur für ein Projekt

Kopiere die sieben Ordner in deinem Projekt nach:

```text
.claude/skills/
```

Beispiel:

```text
mein-projekt/
└── .claude/
    └── skills/
        ├── ecom-content/
        ├── ecom-content-strategy/
        ├── ecom-content-ideas/
        ├── ecom-reel/
        ├── ecom-carousel/
        ├── ecom-story/
        └── ecom-caption/
```

## 3. Codex

Aktuelle Codex-Versionen lesen persönliche Skills aus `$HOME/.agents/skills`.

### Persönliche Installation für alle Projekte

```bash
git clone https://github.com/kontakt-ecomfabrik/onlineshop-instagram-skills.git
mkdir -p ~/.agents/skills
cp -R onlineshop-instagram-skills/ecom-* ~/.agents/skills/
```

### Installation nur für ein Projekt

Kopiere die Skill-Ordner in:

```text
.agents/skills/
```

Danach Codex neu starten, falls die Skills nicht sofort erscheinen.

Skills lassen sich in Codex direkt mit `$` auswählen oder über `/skills` anzeigen, zum Beispiel:

```text
$ecom-content
$ecom-reel
$ecom-carousel
```

Offizielle Anleitung: [Build skills – OpenAI](https://learn.chatgpt.com/docs/build-skills)

## 4. Windows ohne Terminal

### Für Claude Code

Kopiere alle sieben `ecom-*`-Ordner nach:

```text
C:\Users\DEIN-NAME\.claude\skills\
```

### Für Codex

Kopiere alle sieben `ecom-*`-Ordner nach:

```text
C:\Users\DEIN-NAME\.agents\skills\
```

Falls der Ordner `.claude`, `.agents` oder `skills` nicht existiert, lege ihn manuell an.

## 5. Installation prüfen

Die erste Zeile aktiviert den Skill direkt. Verwende in Claude Code `/` und in Codex `# Installation

Diese Anleitung beschreibt die Installation der sieben **EcomFabrik Instagram Skills** in Claude, Claude Code und Codex.

## Voraussetzungen

- Zugriff auf dieses GitHub-Repository
- Bei Claude: **Code execution and file creation** muss aktiviert sein
- Bei einem privaten Repository: Anmeldung bei GitHub beziehungsweise ein eingerichteter Git-Zugang

## 1. Claude im Browser oder in der Desktop-App

Claude lädt benutzerdefinierte Skills als einzelne ZIP-Dateien hoch.

### Schritt 1: Repository herunterladen

1. Klicke auf GitHub auf **Code**.
2. Wähle **Download ZIP**.
3. Entpacke das heruntergeladene Repository.

### Schritt 2: Gewünschten Skill vorbereiten

Wähle beispielsweise den Ordner `ecom-reel` und komprimiere **diesen vollständigen Ordner** als ZIP-Datei.

Die Struktur muss so aussehen:

```text
ecom-reel.zip
└── ecom-reel/
    ├── SKILL.md
    └── references/
```

Die Dateien dürfen nicht ohne den Hauptordner direkt in der ZIP liegen.

### Schritt 3: Skill hochladen

1. Öffne in Claude **Customize → Skills**.
2. Klicke auf **+** und anschließend auf **Create skill**.
3. Wähle **Upload a skill**.
4. Lade die ZIP-Datei hoch.
5. Aktiviere den Skill über den Schalter.

Wiederhole den Vorgang für alle Skills, die du verwenden möchtest.

Offizielle Anleitung: [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## 2. Claude Code

### Persönliche Installation für alle Projekte

```bash
git clone https://github.com/kontakt-ecomfabrik/onlineshop-instagram-skills.git
mkdir -p ~/.claude/skills
cp -R onlineshop-instagram-skills/ecom-* ~/.claude/skills/
```

Danach Claude Code neu starten. Die Skills können automatisch passend zur Aufgabe aktiviert oder direkt aufgerufen werden, zum Beispiel:

```text
/ecom-reel
/ecom-carousel
/ecom-caption
```

### Installation nur für ein Projekt

Kopiere die sieben Ordner in deinem Projekt nach:

```text
.claude/skills/
```

Beispiel:

```text
mein-projekt/
└── .claude/
    └── skills/
        ├── ecom-content/
        ├── ecom-content-strategy/
        ├── ecom-content-ideas/
        ├── ecom-reel/
        ├── ecom-carousel/
        ├── ecom-story/
        └── ecom-caption/
```

## 3. Codex

Aktuelle Codex-Versionen lesen persönliche Skills aus `$HOME/.agents/skills`.

### Persönliche Installation für alle Projekte

```bash
git clone https://github.com/kontakt-ecomfabrik/onlineshop-instagram-skills.git
mkdir -p ~/.agents/skills
cp -R onlineshop-instagram-skills/ecom-* ~/.agents/skills/
```

### Installation nur für ein Projekt

Kopiere die Skill-Ordner in:

```text
.agents/skills/
```

Danach Codex neu starten, falls die Skills nicht sofort erscheinen.

Skills lassen sich in Codex direkt mit `$` auswählen oder über `/skills` anzeigen, zum Beispiel:

```text
$ecom-content
$ecom-reel
$ecom-carousel
```

Offizielle Anleitung: [Build skills – OpenAI](https://learn.chatgpt.com/docs/build-skills)

## 4. Windows ohne Terminal

### Für Claude Code

Kopiere alle sieben `ecom-*`-Ordner nach:

```text
C:\Users\DEIN-NAME\.claude\skills\
```

### Für Codex

Kopiere alle sieben `ecom-*`-Ordner nach:

```text
C:\Users\DEIN-NAME\.agents\skills\
```

Falls der Ordner `.claude`, `.agents` oder `skills` nicht existiert, lege ihn manuell an.

.

### Beispiel für Claude Code

```text
/ecom-reel

Erstelle ein 20-sekündiges Reel für [PRODUKT].
Zielgruppe: [ZIELGRUPPE]
Ziel: [REICHWEITE/VERTRAUEN/KAUF]
```

### Dasselbe Beispiel in Codex

```text
$ecom-reel

Erstelle ein 20-sekündiges Reel für [PRODUKT].
Zielgruppe: [ZIELGRUPPE]
Ziel: [REICHWEITE/VERTRAUEN/KAUF]
```

Weiteres Beispiel für Claude Code:

```text
/ecom-content-strategy

Entwickle eine realistische Instagram-Strategie für meinen Onlineshop.
Frage zuerst nur nach Informationen, die das Ergebnis wesentlich verändern.
```

In Claude im Browser aktivierst du den gewünschten Skill unter **Customize → Skills** und verwendest den Auftrag ohne die erste Befehlszeile.

## Fehlerbehebung

### Der Skill wird nicht angezeigt

- Prüfe, ob der Ordner eine Datei namens `SKILL.md` enthält.
- Prüfe, ob der Ordnername dem Skill-Namen entspricht.
- Starte Claude Code oder Codex neu.
- Aktiviere den Skill in Claude unter **Customize → Skills**.
- Prüfe bei Claude, ob **Code execution and file creation** aktiviert ist.

### Claude oder Codex verwendet den falschen Skill

Rufe den gewünschten Skill ausdrücklich auf:

- Claude Code: `/ecom-reel`
- Codex: `$ecom-reel`
- ChatGPT mit aktivierten Skills: Skill über `@` auswählen

### GitHub-Download erzeugt doppelte Ordner

Wenn nach dem Entpacken beispielsweise `ecom-reel/ecom-reel/` erscheint, verwende für die Installation den **inneren Ordner**, der direkt die Datei `SKILL.md` enthält.
